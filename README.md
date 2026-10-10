# Juh Quiz — 10 modelos

Vídeos verticais 1080×1920 (9:16), com três perguntas e três alternativas por pergunta,
narração em português, contagem de 5 segundos e revelação da resposta.
Um TXT com a legenda e hashtags acompanha cada MP4.

Os dez modelos são recriações pelo código dos layouts aprovados: mesma marca Juh Quiz,
painel branco, alternativas grandes, fundos radiais e as dez combinações de cores.
As imagens de apresentação não são usadas como fundos prontos, pois já contêm perguntas.
As fotografias/ilustrações de cada pergunta são opcionais e precisam ser adicionadas.

## Subir os arquivos

Extraia o ZIP. Copie o CONTEÚDO da pasta Quiz-10 para a raiz deste repositório.
Inclua a pasta .github/workflows: ela contém o botão de geração no Actions.
Se o celular esconder a pasta .github, crie no GitHub o arquivo
`.github/workflows/gerar-quiz.yml` e cole o conteúdo do arquivo correspondente.

## Autorizar o Drive uma vez

Abra Settings → Secrets and variables → Actions → New repository secret.
Nome: `RCLONE_DRIVE_TOKEN`.
Valor: o mesmo JSON completo da autorização de Drive já usada no outro repositório.
O GitHub não permite ver o valor de um Secret antigo: use a cópia original do token.
Se você não tiver essa cópia, será preciso gerar outra autorização.
Não cole o token em arquivos, commits, comentários ou conversas.

A autorização não precisa ser refeita por repositório quando você possui o mesmo
token válido e adiciona esse Secret. O workflow renova o acesso durante a execução.
A pasta de destino é a mesma configurada em Capitulos-Automaticos:
https://drive.google.com/drive/folders/1IeWfSGxVOgY4nwLQwGxzPZMqRCO81i8B
O par MP4/TXT vai para `saida/Juh-Quiz-10/execucao-NUMERO/`.
Cada nova execução tem sua própria pasta; uma reexecução do mesmo run reutiliza a pasta.

## Gerar

Abra Actions → Gerar Juh Quiz e salvar no Drive → Run workflow.
Para testar: início 1 e quantidade 1. Para o lote completo: início 1 e quantidade 30.
O computador e o celular podem ser desligados após a execução iniciar no GitHub.
Os vídeos também ficam disponíveis em Artifacts por 14 dias.

## Sequência dos modelos

1–3: modelo 01; 4–6: 02; 7–9: 03; 10–12: 04; 13–15: 05;
16–18: 06; 19–21: 07; 22–24: 08; 25–27: 09; 28–30: 10.
O vídeo 31 volta ao modelo 01, se forem acrescentados mais temas.
A numeração é a posição do tema em dados_quiz.py, e não um contador entre execuções.
Se gerar só do vídeo 16 em diante, a sequência já começa no modelo 06.

## Editar conteúdo

Em dados_quiz.py, QUIZZES reúne os temas na ordem dos vídeos; cada tema contém
exatamente três perguntas. `correta` vale 0 para A, 1 para B e 2 para C.
LEGENDAS reúne a legenda e hashtags de cada tema. Não repita nomes de temas,
pois chaves iguais em um dicionário Python substituem a entrada anterior.
Para usar uma imagem, coloque o arquivo em imagens_perguntas/ e acrescente
`"imagem": "imagens_perguntas/arquivo.jpg"` à pergunta.

## Executar localmente

Instale Python 3.11, FFmpeg e a fonte DejaVu Sans Bold.
`pip install -r requirements.txt`
`python gerar_quiz.py --inicio 1 --quantidade 1 --lote teste`
Sem --enviar-drive, salva apenas na pasta saida/teste.
`python gerar_quiz.py --previews` cria uma amostra de cada modelo.
`--sem-voz --teste-rapido` é apenas para verificação local, nunca para publicação.

## Limites

A narração requer acesso à internet ao serviço de voz do Edge.
O envio só funciona com token válido e acesso à pasta do Drive.
Se um vídeo falhar, os pares já conferidos continuam no Drive, e o lote para com erro.
Imagens inexistentes e textos que não cabem são rejeitados antes da renderização.
