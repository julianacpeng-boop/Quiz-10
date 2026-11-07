"""Gera vídeos do Juh Quiz com uma questão de concurso por vídeo."""
import argparse
import asyncio
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unicodedata

from PIL import Image, ImageDraw, ImageFont, ImageOps
from dados_quiz import CAPA_SEGUNDOS, QUIZZES, LEGENDAS

W, H, FPS = 1080, 1920, 30
# Amarelo, branco e turquesa; preto é usado para leitura e contorno.
AMARELO = '#FFE15A'
BRANCO = '#FFFFFF'
TURQUESA = '#46D4D8'
PRETO = '#111111'
RAIZ = Path(__file__).resolve().parent
FONTE = os.getenv('QUIZ_FONT', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
VOZ = 'pt-BR-AntonioNeural'
VELOCIDADE_VOZ = '+10%'


def executar(*cmd):
    subprocess.run([str(c) for c in cmd], check=True)


def modelo(indice):
    """Uma variação de layout a cada três vídeos; depois repete as três."""
    if indice < 1:
        raise ValueError('O número do vídeo começa em 1.')
    return ((indice - 1) // 3) % 3


def slug(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-zA-Z0-9]+', '-', texto).strip('-').lower()[:75] or 'quiz'


def fonte(tamanho):
    return ImageFont.truetype(FONTE, tamanho)


def linhas_ajustadas(draw, texto, largura, altura, tamanho_maximo, tamanho_minimo=30, espacamento=1.2):
    for tamanho in range(tamanho_maximo, tamanho_minimo - 1, -2):
        f = fonte(tamanho)
        linhas, atual, palavra_grande = [], '', False
        for palavra in texto.split():
            if draw.textlength(palavra, font=f) > largura:
                palavra_grande = True
            teste = (atual + ' ' + palavra).strip()
            if atual and draw.textlength(teste, font=f) > largura:
                linhas.append(atual)
                atual = palavra
            else:
                atual = teste
        if atual:
            linhas.append(atual)
        passo = int(tamanho * espacamento)
        if not palavra_grande and len(linhas) * passo <= altura:
            return linhas, f, passo
    raise ValueError(f'Texto não cabe no espaço do vídeo: {texto[:90]}')


def texto_central(draw, texto, caixa, tamanho_maximo=66, cor=PRETO, tamanho_minimo=30, espacamento=1.2):
    x1, y1, x2, y2 = caixa
    linhas, f, passo = linhas_ajustadas(draw, texto, x2 - x1, y2 - y1,
                                        tamanho_maximo, tamanho_minimo, espacamento)
    y = y1 + ((y2 - y1) - len(linhas) * passo) / 2
    for linha in linhas:
        draw.text(((x1 + x2) / 2, y), linha, anchor='mt', font=f, fill=cor)
        y += passo


def texto_esquerda(draw, texto, caixa, tamanho_maximo=72, cor=PRETO,
                   tamanho_minimo=34, espacamento=1.22):
    x1, y1, x2, y2 = caixa
    linhas, f, passo = linhas_ajustadas(draw, texto, x2 - x1, y2 - y1,
                                        tamanho_maximo, tamanho_minimo, espacamento)
    y = y1 + ((y2 - y1) - len(linhas) * passo) / 2
    for linha in linhas:
        draw.text((x1, y), linha, anchor='lt', font=f, fill=cor)
        y += passo


def fundo(indice):
    # Amarelo contínuo para reproduzir o fundo da imagem de referência.
    return Image.new('RGB', (W, H), AMARELO)


def desenhar_base(indice, tema, numero, pergunta, estado='pergunta', contagem=None):
    m = modelo(indice)
    img = fundo(indice)
    d = ImageDraw.Draw(img)
    margem = 70 if m != 2 else 92

    # Tema turquesa e cronômetro branco, como na referência enviada.
    if m == 1:
        badge = (margem, 72, W - margem - 190, 218)
        timer = (W - margem - 170, 82, W - margem, 205)
    elif m == 2:
        badge = (margem, 90, W - margem - 205, 235)
        timer = (W - margem - 175, 95, W - margem, 218)
    else:
        badge = (margem, 82, W - margem - 195, 225)
        timer = (W - margem - 175, 92, W - margem, 215)

    d.rounded_rectangle(badge, 85, fill=TURQUESA, outline=PRETO, width=5)
    texto_central(d, tema.upper(), (badge[0] + 20, badge[1] + 8, badge[2] - 20, badge[3] - 8),
                  46, cor=PRETO, tamanho_minimo=26)
    d.rounded_rectangle(timer, 8 if m == 1 else 26, fill=BRANCO, outline=PRETO, width=4)
    if contagem is not None:
        timer_texto = f'0:0{contagem}'
    elif estado == 'resposta':
        timer_texto = '✓'
    elif estado == 'comentario':
        timer_texto = '✓'
    else:
        timer_texto = ''
    texto_central(d, timer_texto, (timer[0] + 2, timer[1] + 3, timer[2] - 2, timer[3] - 3),
                  72, cor=PRETO, tamanho_minimo=38)

    # Área da questão em texto grande, mantendo o fundo amarelo da referência.
    if estado in ('comentario', 'resposta'):
        titulo = 'COMENTÁRIO' if estado == 'comentario' else 'GABARITO'
        d.rounded_rectangle((margem, 300, W - margem, 410), 42,
                            fill=TURQUESA, outline=PRETO, width=4)
        texto_central(d, titulo, (margem + 10, 307, W - margem - 10, 403), 49,
                      cor=PRETO, tamanho_minimo=32)

    if estado == 'comentario':
        texto_esquerda(d, pergunta['explicacao'], (margem, 470, W - margem, 1470),
                       65, cor=PRETO, tamanho_minimo=37, espacamento=1.28)
        cta = 'Agora conte seu gabarito nos comentários!'
        texto_central(d, cta, (margem, 1570, W - margem, 1715), 43, cor=PRETO, tamanho_minimo=30)
    else:
        q = pergunta['pergunta']
        texto_esquerda(d, q, (margem, 345, W - margem, 990),
                       72, cor=PRETO, tamanho_minimo=38, espacamento=1.25)

        for i, alternativa in enumerate(pergunta['alternativas']):
            y1 = 1055 + i * 195
            correta = estado == 'resposta' and i == pergunta['correta']
            marca = '✓' if correta else ' '
            linha = f'({marca}) {"ABC"[i]}. {alternativa}'
            if correta:
                d.rounded_rectangle((margem - 12, y1 - 10, W - margem + 12, y1 + 148),
                                    22, outline=TURQUESA, width=8)
            texto_esquerda(d, linha, (margem, y1, W - margem, y1 + 140),
                           48, cor=PRETO, tamanho_minimo=30, espacamento=1.12)

        if estado == 'pergunta':
            texto_central(d, 'Pense e escolha: A, B ou C', (margem, 1685, W - margem, 1770),
                          37, cor=PRETO, tamanho_minimo=29)
        else:
            correta_texto = pergunta['alternativas'][pergunta['correta']]
            texto_central(d, f'Resposta correta: {"ABC"[pergunta["correta"]]} — {correta_texto}',
                          (margem, 1665, W - margem, 1775), 34, cor=PRETO, tamanho_minimo=27)

    # Marca pequena apenas no canto inferior, conforme pedido.
    d.text((margem, 1820), 'Juh Quiz', font=fonte(34), fill=PRETO)
    return img


def validar():
    if len(QUIZZES) != 15:
        raise ValueError('O lote deve conter 15 temas de Enfermagem para o concurso EBSERH.')
    vistos = 0
    for tema, perguntas in QUIZZES.items():
        if not tema.strip() or len(perguntas) != 1:
            raise ValueError(f'Cada vídeo precisa conter uma questão: {tema}')
        if not LEGENDAS.get(tema, '').strip():
            raise ValueError(f'Legenda ausente para {tema}.')
        quantidade_hashtags = len(re.findall(r'(?<!\w)#\w+', LEGENDAS[tema]))
        if quantidade_hashtags > 4:
            raise ValueError(f'A legenda de {tema} tem mais de quatro hashtags.')
        for p in perguntas:
            vistos += 1
            if not p.get('pergunta') or len(p.get('alternativas', [])) != 3:
                raise ValueError('Cada questão precisa de enunciado e três alternativas.')
            if p.get('correta') not in (0, 1, 2):
                raise ValueError('correta precisa ser 0, 1 ou 2.')
            if not p.get('explicacao', '').strip():
                raise ValueError('Toda questão precisa de explicação para a página de comentário.')
    if vistos != 15:
        raise ValueError(f'Esperadas 15 questões; encontradas {vistos}.')


_EDGE_CONFIGURADO = False


def configurar_edge():
    global _EDGE_CONFIGURADO
    import edge_tts
    import edge_tts.communicate as comunicacao
    import edge_tts.voices as vozes
    for modulo in (comunicacao, vozes):
        contexto = getattr(modulo, '_SSL_CTX', None)
        if contexto is not None:
            contexto.load_default_certs()
    _EDGE_CONFIGURADO = True
    print(f'Voz preservada do Quiz-10: {VOZ}, velocidade {VELOCIDADE_VOZ}.', flush=True)


async def narrar(texto, caminho):
    import edge_tts
    from aiohttp import ClientError
    if not _EDGE_CONFIGURADO:
        await asyncio.to_thread(configurar_edge)
    caminho = Path(caminho)
    temporario = caminho.with_name(caminho.name + '.parcial.mp3')
    esperas = (5, 10, 20)
    for tentativa in range(len(esperas) + 1):
        try:
            temporario.unlink(missing_ok=True)
            await edge_tts.Communicate(texto, VOZ, rate=VELOCIDADE_VOZ,
                                       connect_timeout=30, receive_timeout=90).save(str(temporario))
            if not temporario.exists() or temporario.stat().st_size == 0 or duracao(temporario) <= 0:
                raise edge_tts.exceptions.NoAudioReceived('Áudio vazio ou sem duração.')
            temporario.replace(caminho)
            return
        except (ClientError, asyncio.TimeoutError, edge_tts.exceptions.NoAudioReceived) as erro:
            temporario.unlink(missing_ok=True)
            if tentativa == len(esperas):
                raise RuntimeError('A voz do Quiz-10 não concluiu o áudio após quatro tentativas.') from erro
            await asyncio.sleep(esperas[tentativa])
        except Exception:
            temporario.unlink(missing_ok=True)
            raise


def duracao(path):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                          '-of', 'default=nw=1:nk=1', str(path)], text=True))


def criar_beep(path):
    executar('ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i',
             'sine=frequency=880:sample_rate=48000:duration=0.20', '-ar', '48000', '-ac', '2',
             '-c:a', 'libmp3lame', '-q:a', '4', path)


def clipe(imagem, nome, work, audio=None, segundos=1):
    png, mp4 = work / f'{nome}.png', work / f'{nome}.mp4'
    imagem.save(png)
    cmd = ['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', str(FPS), '-i', str(png)]
    if audio:
        cmd += ['-i', str(audio)]
    else:
        cmd += ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']
    cmd += ['-t', f'{segundos:.3f}', '-vf', f'scale={W}:{H},setsar=1,fps={FPS}',
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-pix_fmt', 'yuv420p',
            '-threads', '2', '-af', 'apad,aresample=48000', '-ac', '2', '-c:a', 'aac',
            '-b:a', '128k', str(mp4)]
    executar(*cmd)
    return mp4


def verificar_video(path):
    data = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_streams',
                                               '-show_format', '-of', 'json', str(path)]))
    v = next(s for s in data['streams'] if s['codec_type'] == 'video')
    if (v['width'], v['height']) != (W, H) or v.get('sample_aspect_ratio') != '1:1':
        raise ValueError('O vídeo não ficou em 1080×1920 com pixels quadrados.')
    return float(data['format']['duration'])


def enviar_drive(video, lote):
    destino = f'destino:saida/Juh-Quiz-Concurso-1/{lote}'
    legenda = video.with_suffix('.txt')
    for arquivo in (video, legenda):
        executar('rclone', 'copyto', arquivo, f'{destino}/{arquivo.name}', '--retries', '3')
    executar('rclone', 'check', video.parent, destino, '--include', video.name,
             '--include', legenda.name, '--one-way')
    print(f'Enviados e conferidos no Drive: {video.name} e {legenda.name}.', flush=True)


def gerar(indice, tema, pergunta, out):
    m = modelo(indice)
    video = out / f'{indice:03d}_layout_{m + 1}_{slug(tema)}.mp4'
    with tempfile.TemporaryDirectory(prefix='quiz10_') as temp:
        work = Path(temp)
        clips = []
        pergunta_audio = work / 'pergunta.mp3'
        alternativas = pergunta['alternativas']
        fala = (f'Questão. {pergunta["pergunta"]} '
                f'Alternativa A: {alternativas[0]}. '
                f'Alternativa B: {alternativas[1]}. '
                f'Alternativa C: {alternativas[2]}.')
        asyncio.run(narrar(fala, pergunta_audio))
        clips.append(clipe(desenhar_base(indice, tema, indice, pergunta, 'pergunta'),
                           'pergunta', work, pergunta_audio, duracao(pergunta_audio) + 0.35))

        beep = work / 'beep.mp3'
        criar_beep(beep)
        for segundo in (3, 2, 1):
            quadro = desenhar_base(indice, tema, indice, pergunta, 'pergunta', contagem=segundo)
            clips.append(clipe(quadro, f'tempo_{segundo}', work, beep, 1.0))

        resposta_audio = work / 'resposta.mp3'
        letra = 'ABC'[pergunta['correta']]
        texto_correto = alternativas[pergunta['correta']]
        asyncio.run(narrar(f'A resposta correta é a alternativa {letra}: {texto_correto}.', resposta_audio))
        clips.append(clipe(desenhar_base(indice, tema, indice, pergunta, 'resposta'),
                           'resposta', work, resposta_audio, duracao(resposta_audio) + 0.4))

        comentario_audio = work / 'comentario.mp3'
        asyncio.run(narrar('Comentário. ' + pergunta['explicacao'], comentario_audio))
        clips.append(clipe(desenhar_base(indice, tema, indice, pergunta, 'comentario'),
                           'comentario', work, comentario_audio, duracao(comentario_audio) + 1.3))

        lista = work / 'concat.txt'
        lista.write_text(''.join(f"file '{p.as_posix()}'\n" for p in clips), encoding='utf-8')
        executar('ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lista,
                 '-c', 'copy', '-movflags', '+faststart', video)

    tempo = verificar_video(video)
    # O TXT individual mantém a duração da capa no padrão dos outros quizzes,
    # seguida da legenda pronta para copiar, com até quatro hashtags.
    texto_legenda = f'CAPA_SEGUNDOS={CAPA_SEGUNDOS}\n{LEGENDAS[tema].strip()}\n'
    video.with_suffix('.txt').write_text(texto_legenda, encoding='utf-8')
    print(f'Vídeo {indice}: uma questão, layout {m + 1}, 1080×1920, {tempo:.1f}s.', flush=True)
    return video


def main():
    parser = argparse.ArgumentParser(description='Gera uma questão de concurso em cada vídeo.')
    parser.add_argument('--inicio', type=int, default=1)
    parser.add_argument('--quantidade', type=int, default=1)
    parser.add_argument('--lote', default='local')
    parser.add_argument('--enviar-drive', action='store_true')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,80}', args.lote):
        parser.error('Use apenas letras, números, hífen e sublinhado no nome do lote.')

    validar()
    entradas = [(tema, pergunta) for tema, questoes in QUIZZES.items() for pergunta in questoes]
    if args.inicio < 1 or args.quantidade < 1 or args.inicio + args.quantidade - 1 > len(entradas):
        parser.error(f'Informe um intervalo entre 1 e {len(entradas)}.')
    if args.enviar_drive:
        executar('rclone', 'lsf', 'destino:', '--max-depth', '1')

    out = RAIZ / 'saida' / args.lote
    out.mkdir(parents=True, exist_ok=True)
    resumo = []
    for indice in range(args.inicio, args.inicio + args.quantidade):
        tema, pergunta = entradas[indice - 1]
        video = gerar(indice, tema, pergunta, out)
        if args.enviar_drive:
            enviar_drive(video, args.lote)
        resumo.append({'video': indice, 'pergunta': pergunta['pergunta'], 'tema': tema,
                       'layout': modelo(indice) + 1, 'drive_conferido': args.enviar_drive})
        (out / 'resumo.json').write_text(json.dumps(resumo, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
