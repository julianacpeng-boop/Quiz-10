"""Juh Quiz: três perguntas por vídeo, dez modelos, MP4 vertical e TXT."""
import argparse
import asyncio
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time
import unicodedata

from PIL import Image, ImageDraw, ImageFont, ImageOps
from dados_quiz import QUIZZES, LEGENDAS

W, H, FPS = 1080, 1920, 30
PALETAS = [
    ('#20cbd1', '#ff726b', '#ffe248'),
    ('#ffe322', '#7022d9', '#ffe322'),
    ('#8527e9', '#ffd83c', '#ffd83c'),
    ('#129cef', '#ff726b', '#ffe248'),
    ('#bcf431', '#7927df', '#ffe248'),
    ('#f63999', '#124198', '#ffe248'),
    ('#ff811c', '#16cbd0', '#ffe248'),
    ('#1341bd', '#ff6b70', '#ffe248'),
    ('#23dca9', '#ff7380', '#ffe248'),
    ('#ffe322', '#ff3145', '#1246d6'),
]
RAIZ = Path(__file__).resolve().parent
FONTE = os.getenv('QUIZ_FONT', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')

def executar(*cmd):
    subprocess.run([str(c) for c in cmd], check=True)

def modelo(indice):
    if indice < 1:
        raise ValueError('O número do vídeo começa em 1.')
    return ((indice - 1) // 3) % 10

def slug(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-zA-Z0-9]+', '-', texto).strip('-').lower()[:90] or 'quiz'

def texto_caixa(draw, texto, box, max_size=66, fill='#171725', stroke=0):
    x1, y1, x2, y2 = box
    for tamanho in range(max_size, 21, -2):
        fonte = ImageFont.truetype(FONTE, tamanho)
        linhas, atual = [], ''
        largo = False
        for palavra in texto.split():
            if draw.textlength(palavra, font=fonte) > x2-x1:
                largo = True
            tentativa = (atual + ' ' + palavra).strip()
            if atual and draw.textlength(tentativa, font=fonte) > x2-x1:
                linhas.append(atual)
                atual = palavra
            else:
                atual = tentativa
        if atual:
            linhas.append(atual)
        altura = tamanho * 1.27
        if not largo and altura * len(linhas) <= y2-y1:
            break
    else:
        raise ValueError(f'Texto grande demais para o layout: {texto[:80]}')
    y = y1 + ((y2-y1) - altura*len(linhas))/2
    for linha in linhas:
        draw.text(((x1+x2)/2, y), linha, anchor='mt', font=fonte, fill=fill,
                  stroke_width=stroke, stroke_fill='#171725')
        y += altura

def fundo(m):
    bg, accent, yellow = PALETAS[m]
    img = Image.new('RGB', (W, H), bg)
    d = ImageDraw.Draw(img)
    # Raios suaves, sem disputar atenção com as perguntas.
    rgb = tuple(int(bg[i:i+2], 16) for i in (1, 3, 5))
    light = tuple(min(255, int(c*.86+255*.14)) for c in rgb)
    cx, cy = W/2, H*.48
    for i in range(0, 32, 2):
        a, b = i*math.pi/16, (i+1)*math.pi/16
        d.polygon([(cx, cy), (cx+2600*math.cos(a), cy+2600*math.sin(a)),
                   (cx+2600*math.cos(b), cy+2600*math.sin(b))], fill=light)
    for x, y in [(-110, -90), (1000, 1750)]:
        d.ellipse((x, y, x+280, y+280), fill=accent)
    # Marca desenhada pelo código para permanecer consistente nos dez modelos.
    d.rounded_rectangle((275, 70, 805, 305), 80, fill=accent)
    texto_caixa(d, 'Juh', (300, 65, 690, 180), 112, 'white', 7)
    texto_caixa(d, 'Quiz', (300, 175, 750, 300), 110, '#ffe248', 7)
    d.ellipse((690, 60, 820, 185), fill='white', outline='#171725', width=7)
    texto_caixa(d, '?', (705, 72, 805, 167), 88, accent)
    return img

def desenhar(tema, pergunta, numero, m, contagem=None, resposta=False):
    img = fundo(m)
    d = ImageDraw.Draw(img)
    _, accent, yellow = PALETAS[m]
    raio = [34, 40, 28, 42, 32, 40, 26, 35, 40, 28][m]
    d.rounded_rectangle((65, 330, 1015, 445), raio, fill=accent, outline='#171725', width=5)
    texto_caixa(d, tema.upper(), (85, 345, 995, 425), 49, 'white', 1)
    d.rounded_rectangle((65, 480, 1015, 1030), raio, fill='white', outline='#171725', width=5)
    texto_caixa(d, f'PERGUNTA {numero}/3', (90, 497, 990, 545), 28, '#555563')
    caminho = pergunta.get('imagem')
    if caminho:
        path = (RAIZ / caminho).resolve()
        if not path.is_relative_to(RAIZ / 'imagens_perguntas'):
            raise ValueError('Imagens devem ficar em imagens_perguntas/.')
        with Image.open(path) as original:
            figura = ImageOps.contain(original.convert('RGB'), (810, 250))
        texto_caixa(d, pergunta['pergunta'], (100, 560, 980, 730), 64)
        img.paste(figura, ((W-figura.width)//2, 745+(250-figura.height)//2))
    else:
        texto_caixa(d, pergunta['pergunta'], (110, 580, 970, 890), 74)
    texto_caixa(d, '@juhquiz', (330, 975, 750, 1012), 30)
    for i, alternativa in enumerate(pergunta['alternativas']):
        y = 1070 + i*155
        cor = '#9be582' if resposta and i == pergunta['correta'] else 'white'
        d.rounded_rectangle((90, y, 990, y+130), raio, fill=cor, outline='#171725', width=5)
        d.ellipse((100, y+8, 214, y+122), fill=accent, outline='#171725', width=5)
        texto_caixa(d, 'ABC'[i], (112, y+15, 202, y+108), 72, 'white', 2)
        texto_caixa(d, alternativa, (235, y+8, 965, y+118), 55)
    d.ellipse((457, 1570, 623, 1736), fill='#17234a', outline=yellow, width=9)
    texto_caixa(d, str(contagem) if contagem is not None else ('OK' if resposta else '?'),
                (470, 1584, 610, 1716), 83 if not resposta else 57, 'white')
    d.rounded_rectangle((90, 1775, 990, 1860), 36, fill='#ffe248', outline='#171725', width=4)
    texto_caixa(d, 'Responda nos comentários!', (110, 1785, 970, 1845), 43)
    return img

def validar():
    if not QUIZZES:
        raise ValueError('Preencha QUIZZES em dados_quiz.py.')
    for tema, perguntas in QUIZZES.items():
        if not isinstance(tema, str) or not tema.strip() or len(perguntas) != 3:
            raise ValueError(f'Cada vídeo precisa de um tema e exatamente 3 perguntas: {tema}')
        if not LEGENDAS.get(tema, '').strip():
            raise ValueError(f'Preencha a legenda do tema {tema}.')
        for p in perguntas:
            if not isinstance(p.get('pergunta'), str) or not p['pergunta'].strip():
                raise ValueError('Pergunta vazia.')
            if len(p.get('alternativas', [])) != 3 or not all(isinstance(a, str) and a.strip() for a in p['alternativas']):
                raise ValueError('Cada pergunta precisa de 3 alternativas preenchidas.')
            if type(p.get('correta')) is not int or p['correta'] not in (0, 1, 2):
                raise ValueError('correta deve ser 0 (A), 1 (B) ou 2 (C).')
            # Validação visual de todo o lote antes de gastar tempo gerando.
            for m in range(10):
                desenhar(tema, p, 1, m)

async def narrar(texto, caminho):
    import edge_tts
    for tentativa in range(3):
        try:
            await edge_tts.Communicate(texto, 'pt-BR-AntonioNeural', rate='+10%').save(str(caminho))
            return
        except Exception:
            if tentativa == 2:
                raise
            await asyncio.sleep(2*(tentativa+1))

def duracao(path):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries',
        'format=duration', '-of', 'default=nw=1:nk=1', str(path)], text=True))

def clipe(img, nome, work, audio=None, segundos=1):
    png, mp4 = work/f'{nome}.png', work/f'{nome}.mp4'
    img.save(png)
    cmd = ['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', str(FPS), '-i', str(png)]
    if audio:
        cmd += ['-i', str(audio)]
    else:
        cmd += ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']
    cmd += ['-t', str(segundos), '-vf', f'scale={W}:{H},setsar=1,fps={FPS}', '-c:v', 'libx264',
            '-preset', 'veryfast', '-crf', '23', '-pix_fmt', 'yuv420p', '-threads', '2',
            '-af', 'apad,aresample=48000', '-ac', '2', '-c:a', 'aac', '-b:a', '128k', str(mp4)]
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
    destino = f'destino:saida/Juh-Quiz-10/{lote}'
    for arquivo in (video, video.with_suffix('.txt')):
        executar('rclone', 'copyto', arquivo, f'{destino}/{arquivo.name}', '--retries', '3')
    executar('rclone', 'check', video.parent, destino, '--include', video.name,
             '--include', video.with_suffix('.txt').name, '--one-way')
    print(f'Enviados e conferidos no Drive: {video.name} e TXT.', flush=True)

def gerar(indice, tema, perguntas, out, sem_voz=False, teste=False):
    m = modelo(indice)
    video = out/f'{indice:03d}_modelo_{m+1:02d}_{slug(tema)}.mp4'
    with tempfile.TemporaryDirectory(prefix='quiz10_') as temp:
        work = Path(temp)
        clips = []
        for n, pergunta in enumerate(perguntas, 1):
            audio = None
            segundos = 0.2 if teste else 5
            if not sem_voz:
                audio = work/f'q{n}.mp3'
                fala = pergunta['pergunta'] + '. ' + '. '.join(f'{"ABC"[i]}. {a}' for i,a in enumerate(pergunta['alternativas']))
                asyncio.run(narrar(fala, audio))
                segundos = duracao(audio)+0.5
            clips.append(clipe(desenhar(tema, pergunta, n, m), f'q{n}', work, audio, segundos))
            for t in range(5, 0, -1):
                clips.append(clipe(desenhar(tema, pergunta, n, m, contagem=t), f'q{n}_{t}', work,
                                   segundos=0.1 if teste else 1))
            audio = None
            segundos = 0.2 if teste else 3
            if not sem_voz:
                audio = work/f'a{n}.mp3'
                asyncio.run(narrar(f'A resposta correta é: {pergunta["alternativas"][pergunta["correta"]]}.', audio))
                segundos = duracao(audio)+0.7
            clips.append(clipe(desenhar(tema, pergunta, n, m, resposta=True), f'a{n}', work, audio, segundos))
        tela = fundo(m)
        d = ImageDraw.Draw(tela)
        d.rounded_rectangle((65, 620, 1015, 1270), 45, fill='white', outline='#171725', width=5)
        texto_caixa(d, 'Quantas você acertou?', (110, 700, 970, 930), 78)
        texto_caixa(d, 'Comente seu resultado: 0, 1, 2 ou 3!', (110, 1000, 970, 1210), 52)
        clips.append(clipe(tela, 'fim', work, segundos=0.2 if teste else 2))
        lista = work/'concat.txt'
        lista.write_text(''.join(f"file '{p.as_posix()}'\n" for p in clips), encoding='utf-8')
        executar('ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lista,
                 '-c', 'copy', '-movflags', '+faststart', video)
    length = verificar_video(video)
    video.with_suffix('.txt').write_text(LEGENDAS[tema].strip()+'\n', encoding='utf-8')
    print(f'Vídeo {indice}: modelo {m+1:02d}, 1080×1920, {length:.1f}s.', flush=True)
    return video

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--inicio', type=int, default=1)
    p.add_argument('--quantidade', type=int, default=30)
    p.add_argument('--lote', default='local')
    p.add_argument('--enviar-drive', action='store_true')
    p.add_argument('--previews', action='store_true')
    p.add_argument('--sem-voz', action='store_true', help='Teste local; a geração normal tem narração.')
    p.add_argument('--teste-rapido', action='store_true', help='Somente teste local: reduz duração.')
    args = p.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,80}', args.lote):
        p.error('Use apenas letras, números, hífen e sublinhado no lote.')
    if args.inicio < 1 or args.quantidade < 1 or args.inicio+args.quantidade-1 > len(QUIZZES):
        p.error(f'Informe um intervalo de vídeos entre 1 e {len(QUIZZES)}.')
    if args.enviar_drive and (args.sem_voz or args.teste_rapido or args.previews):
        p.error('Não envie testes ou previews ao Drive.')
    validar()
    out = RAIZ/'saida'/args.lote
    out.mkdir(parents=True, exist_ok=True)
    entradas = list(QUIZZES.items())
    if args.previews:
        tema, perguntas = entradas[0]
        for m in range(10):
            desenhar(tema, perguntas[0], 1, m, 5).save(out/f'modelo_{m+1:02d}.png')
        return
    if args.enviar_drive:
        executar('rclone', 'lsf', 'destino:', '--max-depth', '1')
    resumo = []
    for indice in range(args.inicio, args.inicio+args.quantidade):
        tema, perguntas = entradas[indice-1]
        video = gerar(indice, tema, perguntas, out, args.sem_voz, args.teste_rapido)
        if args.enviar_drive:
            enviar_drive(video, args.lote)
        resumo.append({'video': indice, 'modelo': modelo(indice)+1, 'arquivo': video.name,
                       'drive_conferido': args.enviar_drive})
        (out/'resumo.json').write_text(json.dumps(resumo, ensure_ascii=False, indent=2), encoding='utf-8')

if __name__ == '__main__':
    main()
