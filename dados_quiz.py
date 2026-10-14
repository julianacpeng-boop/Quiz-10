# -*- coding: utf-8 -*-
"""Quiz-10 — lote 4: 30 temas, 90 perguntas e 30 montagens em caricatura.
As imagens dos vídeos 1–10 mostram A, B e C da esquerda para a direita.
"""

QUIZZES = {'Aves e suas curiosidades': [{'pergunta': 'Qual destas aves costuma procurar alimento à noite?',
                               'alternativas': ['Galinha', 'Pato', 'Coruja'],
                               'correta': 2,
                               'imagem': 'imagens_perguntas/lote4_caricatura_v01_p01.png'},
                              {'pergunta': 'Qual destas aves não voa e é nativa da Antártida?',
                               'alternativas': ['Flamingo', 'Pinguim-imperador', 'Pavão'],
                               'correta': 1,
                               'imagem': 'imagens_perguntas/lote4_caricatura_v01_p02.png'},
                              {'pergunta': 'Qual destas aves é conhecida por imitar a voz humana?',
                               'alternativas': ['Papagaio', 'Tucano', 'Coruja'],
                               'correta': 0,
                               'imagem': 'imagens_perguntas/lote4_caricatura_v01_p03.png'}],
 'Répteis e suas características': [{'pergunta': 'Qual destes répteis é terrestre e pertence ao grupo dos '
                                                 'quelônios?',
                                     'alternativas': ['Jabuti', 'Jacaré', 'Iguana'],
                                     'correta': 0,
                                     'imagem': 'imagens_perguntas/lote4_caricatura_v02_p01.png'},
                                    {'pergunta': 'Qual destes répteis pode mudar de cor?',
                                     'alternativas': ['Iguana', 'Camaleão', 'Jabuti'],
                                     'correta': 1,
                                     'imagem': 'imagens_perguntas/lote4_caricatura_v02_p02.png'},
                                    {'pergunta': 'Qual destes répteis captura presas usando constrição?',
                                     'alternativas': ['Jacaré', 'Lagarto', 'Jiboia'],
                                     'correta': 2,
                                     'imagem': 'imagens_perguntas/lote4_caricatura_v02_p03.png'}],
 'Insetos e pequenos bichos': [{'pergunta': 'Qual destes insetos passa por uma fase de lagarta?',
                                'alternativas': ['Libélula', 'Borboleta', 'Gafanhoto'],
                                'correta': 1,
                                'imagem': 'imagens_perguntas/lote4_caricatura_v03_p01.png'},
                               {'pergunta': 'Qual destes insetos produz mel?',
                                'alternativas': ['Abelha', 'Formiga', 'Grilo'],
                                'correta': 0,
                                'imagem': 'imagens_perguntas/lote4_caricatura_v03_p02.png'},
                               {'pergunta': 'Qual destes animais é um aracnídeo?',
                                'alternativas': ['Besouro', 'Borboleta', 'Aranha'],
                                'correta': 2,
                                'imagem': 'imagens_perguntas/lote4_caricatura_v03_p03.png'}],
 'Legumes e verduras': [{'pergunta': 'Qual destes alimentos tem variedades chamadas americana e crespa?',
                         'alternativas': ['Alface', 'Batata', 'Beterraba'],
                         'correta': 0,
                         'imagem': 'imagens_perguntas/lote4_caricatura_v04_p01.png'},
                        {'pergunta': 'Qual destes alimentos é a raiz da planta?',
                         'alternativas': ['Brócolis', 'Cenoura', 'Alface'],
                         'correta': 1,
                         'imagem': 'imagens_perguntas/lote4_caricatura_v04_p02.png'},
                        {'pergunta': 'Qual destes alimentos é um tubérculo?',
                         'alternativas': ['Pepino', 'Abobrinha', 'Batata'],
                         'correta': 2,
                         'imagem': 'imagens_perguntas/lote4_caricatura_v04_p03.png'}],
 'Comidas típicas brasileiras': [{'pergunta': 'Qual destas comidas é feita tradicionalmente com polvilho e '
                                              'queijo?',
                                  'alternativas': ['Pão de queijo', 'Tapioca', 'Cuscuz de milho'],
                                  'correta': 0,
                                  'imagem': 'imagens_perguntas/lote4_caricatura_v05_p01.png'},
                                 {'pergunta': 'Qual destas comidas é feita com goma de mandioca hidratada?',
                                  'alternativas': ['Coxinha', 'Pamonha', 'Tapioca'],
                                  'correta': 2,
                                  'imagem': 'imagens_perguntas/lote4_caricatura_v05_p02.png'},
                                 {'pergunta': 'Qual destes pratos leva tradicionalmente feijão-preto e '
                                              'carnes?',
                                  'alternativas': ['Acarajé', 'Feijoada', 'Pão de queijo'],
                                  'correta': 1,
                                  'imagem': 'imagens_perguntas/lote4_caricatura_v05_p03.png'}],
 'Objetos antigos do cotidiano': [{'pergunta': 'Qual destes objetos era usado para datilografar documentos?',
                                   'alternativas': ['Máquina de escrever',
                                                    'Telefone de disco',
                                                    'Rádio de válvulas'],
                                   'correta': 0,
                                   'imagem': 'imagens_perguntas/lote4_caricatura_v06_p01.png'},
                                  {'pergunta': 'Qual destes objetos usa carvão como fonte de calor?',
                                   'alternativas': ['Gramofone', 'Telefone de disco', 'Ferro a carvão'],
                                   'correta': 2,
                                   'imagem': 'imagens_perguntas/lote4_caricatura_v06_p02.png'},
                                  {'pergunta': 'Qual destes objetos reproduz som a partir de um disco?',
                                   'alternativas': ['Máquina de escrever', 'Gramofone', 'Ferro a carvão'],
                                   'correta': 1,
                                   'imagem': 'imagens_perguntas/lote4_caricatura_v06_p03.png'}],
 'Aparelhos domésticos': [{'pergunta': 'Qual destes aparelhos conserva alimentos pelo resfriamento?',
                           'alternativas': ['Forno elétrico', 'Geladeira', 'Máquina de lavar'],
                           'correta': 1,
                           'imagem': 'imagens_perguntas/lote4_caricatura_v07_p01.png'},
                          {'pergunta': 'Qual destes aparelhos é usado para passar roupas?',
                           'alternativas': ['Batedeira', 'Torradeira', 'Ferro de passar'],
                           'correta': 2,
                           'imagem': 'imagens_perguntas/lote4_caricatura_v07_p02.png'},
                          {'pergunta': 'Qual destes aparelhos remove poeira por sucção?',
                           'alternativas': ['Aspirador de pó', 'Ventilador', 'Liquidificador'],
                           'correta': 0,
                           'imagem': 'imagens_perguntas/lote4_caricatura_v07_p03.png'}],
 'Brinquedos tradicionais': [{'pergunta': 'Qual destes brinquedos sobe ao céu preso a uma linha?',
                              'alternativas': ['Pipa', 'Ioiô', 'Bola de gude'],
                              'correta': 0,
                              'imagem': 'imagens_perguntas/lote4_caricatura_v08_p01.png'},
                             {'pergunta': 'Qual destes brinquedos gira apoiado em uma ponta?',
                              'alternativas': ['Pipa', 'Pião', 'Peteca'],
                              'correta': 1,
                              'imagem': 'imagens_perguntas/lote4_caricatura_v08_p02.png'},
                             {'pergunta': 'Qual destes brinquedos é feito de uma pequena esfera de vidro?',
                              'alternativas': ['Pião', 'Peteca', 'Bola de gude'],
                              'correta': 2,
                              'imagem': 'imagens_perguntas/lote4_caricatura_v08_p03.png'}],
 'Chapéus e acessórios': [{'pergunta': 'Qual destes acessórios é muito associado às festas juninas '
                                       'brasileiras?',
                           'alternativas': ['Chapéu de palha', 'Boné', 'Boina'],
                           'correta': 0,
                           'imagem': 'imagens_perguntas/lote4_caricatura_v09_p01.png'},
                          {'pergunta': 'Qual destes acessórios é usado no pescoço para proteger do frio?',
                           'alternativas': ['Luvas', 'Cinto', 'Cachecol'],
                           'correta': 2,
                           'imagem': 'imagens_perguntas/lote4_caricatura_v09_p02.png'},
                          {'pergunta': 'Qual destes acessórios costuma cobrir as orelhas no frio?',
                           'alternativas': ['Boné', 'Gorro', 'Viseira'],
                           'correta': 1,
                           'imagem': 'imagens_perguntas/lote4_caricatura_v09_p03.png'}],
 'Objetos de costura': [{'pergunta': 'Qual destes objetos corta tecidos?',
                         'alternativas': ['Agulha', 'Alfinete', 'Tesoura'],
                         'correta': 2,
                         'imagem': 'imagens_perguntas/lote4_caricatura_v10_p01.png'},
                        {'pergunta': 'Qual destes objetos mede o corpo para ajustar uma roupa?',
                         'alternativas': ['Dedal', 'Fita métrica', 'Agulha'],
                         'correta': 1,
                         'imagem': 'imagens_perguntas/lote4_caricatura_v10_p02.png'},
                        {'pergunta': 'Qual destes objetos protege o dedo ao empurrar a agulha?',
                         'alternativas': ['Dedal', 'Carretel de linha', 'Tesoura'],
                         'correta': 0,
                         'imagem': 'imagens_perguntas/lote4_caricatura_v10_p03.png'}],
 'Curiosidades sobre o sono': [{'pergunta': 'Em qual fase do sono os sonhos vívidos são mais frequentes?',
                                'alternativas': ['Sono REM', 'Sono leve N1', 'Vigília'],
                                'correta': 0},
                               {'pergunta': 'Qual hormônio ajuda a sinalizar ao corpo que chegou a noite?',
                                'alternativas': ['Insulina', 'Melatonina', 'Cortisol'],
                                'correta': 1},
                               {'pergunta': 'O que acontece com o cérebro durante o sono?',
                                'alternativas': ['Continua ativo',
                                                 'Só funciona durante sonhos',
                                                 'Desliga completamente'],
                                'correta': 0}],
 'Como funciona a memória?': [{'pergunta': 'Qual região do cérebro participa da formação de novas memórias?',
                               'alternativas': ['Cerebelo', 'Hipocampo', 'Tronco encefálico'],
                               'correta': 1},
                              {'pergunta': 'Qual prática costuma ajudar a lembrar um conteúdo estudado?',
                               'alternativas': ['Ler uma única vez',
                                                'Nunca revisar',
                                                'Revisar em intervalos'],
                               'correta': 2},
                              {'pergunta': 'A memória de trabalho permite fazer o quê?',
                               'alternativas': ['Manter informações por pouco tempo para usá-las',
                                                'Guardar tudo para sempre',
                                                'Armazenar apenas a infância'],
                               'correta': 0}],
 'Por que sentimos cócegas?': [{'pergunta': 'As cócegas são percebidas principalmente por qual sistema?',
                                'alternativas': ['Sistema nervoso',
                                                 'Sistema circulatório',
                                                 'Sistema digestório'],
                                'correta': 0},
                               {'pergunta': 'Por que fazer cócegas em si mesmo costuma ter menos efeito?',
                                'alternativas': ['A pele fica dormente',
                                                 'O cérebro prevê o próprio toque',
                                                 'O toque próprio é sempre mais fraco'],
                                'correta': 1},
                               {'pergunta': 'A sensibilidade a cócegas é igual em todas as pessoas?',
                                'alternativas': ['Só depende da idade',
                                                 'Não, varia entre as pessoas',
                                                 'Sim, sempre'],
                                'correta': 1}],
 'Por que bocejamos?': [{'pergunta': 'O bocejo é um movimento de qual tipo?',
                         'alternativas': ['Sempre planejado', 'Involuntário', 'Exclusivo do sono'],
                         'correta': 1},
                        {'pergunta': 'Em qual situação o bocejo costuma aparecer?',
                         'alternativas': ['Só durante exercício', 'Durante sonolência', 'Só depois de comer'],
                         'correta': 1},
                        {'pergunta': 'O que significa dizer que um bocejo é contagioso?',
                         'alternativas': ['Ver alguém bocejar pode provocar outro bocejo',
                                          'Ele transmite um vírus',
                                          'Ele ocorre apenas em grupos'],
                         'correta': 0}],
 'Como percebemos os sabores?': [{'pergunta': 'Quais estruturas contêm células que detectam sabores?',
                                  'alternativas': ['Cordas vocais',
                                                   'Glândulas salivares',
                                                   'Botões gustativos'],
                                  'correta': 2},
                                 {'pergunta': 'Qual destes é um dos cinco sabores básicos?',
                                  'alternativas': ['Refrescante', 'Picante', 'Umami'],
                                  'correta': 2},
                                 {'pergunta': 'Qual sentido também contribui muito para o sabor dos '
                                              'alimentos?',
                                  'alternativas': ['Olfato', 'Audição', 'Tato apenas'],
                                  'correta': 0}],
 'Como sentimos os cheiros?': [{'pergunta': 'Por onde moléculas de odor chegam aos receptores olfativos?',
                                'alternativas': ['Ouvido interno', 'Cavidade nasal', 'Esôfago'],
                                'correta': 1},
                               {'pergunta': 'Qual órgão interpreta os sinais relacionados aos cheiros?',
                                'alternativas': ['Pulmão', 'Língua', 'Cérebro'],
                                'correta': 2},
                               {'pergunta': 'Por que um cheiro pode parecer mais fraco após algum tempo?',
                                'alternativas': ['Pode ocorrer adaptação olfativa',
                                                 'O cheiro sempre desaparece',
                                                 'O nariz deixa de respirar'],
                                'correta': 0}],
 'Por que nossa voz muda em gravações?': [{'pergunta': 'Ao falar, como ouvimos parte da nossa própria voz?',
                                           'alternativas': ['Apenas pelo eco do ambiente',
                                                            'Também pela vibração dos ossos',
                                                            'Só pelo ar'],
                                           'correta': 1},
                                          {'pergunta': 'Uma gravação comum capta principalmente o som que '
                                                       'viaja por onde?',
                                           'alternativas': ['Pelos ossos do crânio',
                                                            'Pelo contato com a pele',
                                                            'Pelo ar'],
                                           'correta': 2},
                                          {'pergunta': 'A voz gravada costuma parecer diferente para quem?',
                                           'alternativas': ['Para a própria pessoa que fala',
                                                            'Somente para os ouvintes',
                                                            'Para ninguém'],
                                           'correta': 0}],
 'Como os animais se comunicam?': [{'pergunta': 'Como as abelhas podem indicar a direção de uma fonte de '
                                                'alimento?',
                                    'alternativas': ['Por batidas na água',
                                                     'Somente mudando de cor',
                                                     'Com movimentos de dança'],
                                    'correta': 2},
                                   {'pergunta': 'Qual destes animais é conhecido por emitir uivos?',
                                    'alternativas': ['Tartaruga', 'Caracol', 'Lobo'],
                                    'correta': 2},
                                   {'pergunta': 'O que são feromônios?',
                                    'alternativas': ['Órgãos de audição',
                                                     'Tipos de canto',
                                                     'Substâncias usadas na comunicação química'],
                                    'correta': 2}],
 'Animais que vivem em sociedade': [{'pergunta': 'Qual destes animais vive em colônias organizadas?',
                                     'alternativas': ['Formiga', 'Tigre', 'Polvo'],
                                     'correta': 0},
                                    {'pergunta': 'Como se chama um grupo de abelhas?',
                                     'alternativas': ['Manada', 'Enxame', 'Cardume'],
                                     'correta': 1},
                                    {'pergunta': 'Em muitas espécies de formigas, qual é uma função das '
                                                 'operárias?',
                                     'alternativas': ['Cuidar apenas de si mesmas',
                                                      'Botar todos os ovos da colônia',
                                                      'Buscar alimento e cuidar da colônia'],
                                     'correta': 2}],
 'Como as plantas espalham suas sementes?': [{'pergunta': 'Qual agente pode transportar sementes leves com '
                                                          'estruturas semelhantes a paraquedas?',
                                              'alternativas': ['Magnetismo', 'Vento', 'Calor do solo'],
                                              'correta': 1},
                                             {'pergunta': 'Como animais podem espalhar sementes?',
                                              'alternativas': ['Transformando sementes em frutos',
                                                               'Carregando-as ou eliminando-as nas fezes',
                                                               'Somente enterrando todas elas'],
                                              'correta': 1},
                                             {'pergunta': 'O que pode acontecer quando um fruto seco se abre '
                                                          'de forma brusca?',
                                              'alternativas': ['As sementes são lançadas para longe',
                                                               'As sementes sempre ficam presas',
                                                               'As sementes viram raízes na hora'],
                                              'correta': 0}],
 'Plantas que vivem no deserto': [{'pergunta': 'Qual estrutura de muitos cactos armazena água?',
                                   'alternativas': ['Caule', 'Pétala', 'Espinho apenas'],
                                   'correta': 0},
                                  {'pergunta': 'Qual característica ajuda a reduzir a perda de água em '
                                               'muitas plantas do deserto?',
                                   'alternativas': ['Raízes ausentes',
                                                    'Cutícula espessa',
                                                    'Folhas sempre enormes'],
                                   'correta': 1},
                                  {'pergunta': 'O que caracteriza uma planta suculenta?',
                                   'alternativas': ['Viver apenas na areia',
                                                    'Armazenar água em tecidos',
                                                    'Não precisar de luz'],
                                   'correta': 1}],
 'Curiosidades sobre os bambus': [{'pergunta': 'O bambu pertence à mesma família de qual planta?',
                                   'alternativas': ['Grama', 'Pinheiro', 'Roseira'],
                                   'correta': 0},
                                  {'pergunta': 'Como se chamam as divisões visíveis ao longo do caule do '
                                               'bambu?',
                                   'alternativas': ['Nós', 'Anéis de casca', 'Pétalas'],
                                   'correta': 0},
                                  {'pergunta': 'Como muitos bambus produzem novos brotos?',
                                   'alternativas': ['Por bulbos aéreos',
                                                    'Por raízes sem caule',
                                                    'Por rizomas subterrâneos'],
                                   'correta': 2}],
 'A história dos números': [{'pergunta': 'Qual civilização usava um sistema de numeração de base 60?',
                             'alternativas': ['Babilônica', 'Inca', 'Viking'],
                             'correta': 0},
                            {'pergunta': 'Qual símbolo representa cinco nos algarismos romanos?',
                             'alternativas': ['V', 'X', 'L'],
                             'correta': 0},
                            {'pergunta': 'No sistema decimal, qual é a base da numeração?',
                             'alternativas': ['Dois', 'Sessenta', 'Dez'],
                             'correta': 2}],
 'A origem do alfabeto': [{'pergunta': 'Qual povo difundiu um alfabeto que influenciou o grego?',
                           'alternativas': ['Astecas', 'Fenícios', 'Incas'],
                           'correta': 1},
                          {'pergunta': 'Qual inovação os gregos fizeram ao adaptar o alfabeto fenício?',
                           'alternativas': ['Usaram letras para vogais',
                                            'Retiraram todos os sons',
                                            'Usaram somente desenhos'],
                           'correta': 0},
                          {'pergunta': 'Qual alfabeto é usado para escrever português?',
                           'alternativas': ['Grego', 'Cirílico', 'Latino'],
                           'correta': 2}],
 'Como surgiram os jogos de tabuleiro?': [{'pergunta': 'Qual jogo de tabuleiro é associado ao Egito Antigo?',
                                           'alternativas': ['Uno', 'Senet', 'Banco Imobiliário'],
                                           'correta': 1},
                                          {'pergunta': 'Qual país é associado à origem do chaturanga, '
                                                       'ancestral do xadrez?',
                                           'alternativas': ['Índia', 'Canadá', 'Brasil'],
                                           'correta': 0},
                                          {'pergunta': 'Em jogos de tabuleiro, para que dados costumam ser '
                                                       'usados?',
                                           'alternativas': ['Para introduzir resultados aleatórios',
                                                            'Para registrar a pontuação sempre',
                                                            'Para definir o tema do jogo'],
                                           'correta': 0}],
 'A história do cinema': [{'pergunta': 'Como filmes criam a impressão de movimento?',
                           'alternativas': ['Usando uma única foto parada',
                                            'Movendo apenas a tela',
                                            'Exibindo imagens em sequência'],
                           'correta': 2},
                          {'pergunta': 'Quais irmãos ficaram conhecidos por sessões públicas de cinema em '
                                       '1895?',
                           'alternativas': ['Irmãos Lumière', 'Irmãos Wright', 'Irmãos Grimm'],
                           'correta': 0},
                          {'pergunta': 'Como eram chamados filmes sem diálogos gravados sincronizados?',
                           'alternativas': ['Filmes mudos', 'Filmes sem música', 'Filmes em preto e branco'],
                           'correta': 0}],
 'Como o rádio transmite o som?': [{'pergunta': 'Qual tipo de onda leva o sinal de uma transmissão de rádio?',
                                    'alternativas': ['Corrente de ar',
                                                     'Onda sonora pelo espaço',
                                                     'Onda eletromagnética'],
                                    'correta': 2},
                                   {'pergunta': 'O que significa FM?',
                                    'alternativas': ['Frequência modulada',
                                                     'Força mecânica',
                                                     'Fluxo magnético'],
                                    'correta': 0},
                                   {'pergunta': 'Qual componente transforma o sinal elétrico em som audível?',
                                    'alternativas': ['Alto-falante', 'Antena apenas', 'Botão de sintonia'],
                                    'correta': 0}],
 'Como funciona o controle remoto?': [{'pergunta': 'Muitos controles de televisão enviam comandos usando '
                                                   'qual luz?',
                                       'alternativas': ['Infravermelha', 'Luz azul', 'Ultravioleta'],
                                       'correta': 0},
                                      {'pergunta': 'Por que um controle infravermelho pode falhar atrás de '
                                                   'uma parede?',
                                       'alternativas': ['A parede descarrega a pilha',
                                                        'A parede bloqueia o sinal de luz',
                                                        'A parede muda o canal'],
                                       'correta': 1},
                                      {'pergunta': 'Além de infravermelho, qual tecnologia é usada em alguns '
                                                   'controles?',
                                       'alternativas': ['Corrente elétrica pelo ar',
                                                        'Ultrassom apenas',
                                                        'Bluetooth'],
                                       'correta': 2}],
 'Por que os ímãs atraem alguns metais?': [{'pergunta': 'Qual destes metais costuma ser atraído por um ímã '
                                                        'comum?',
                                            'alternativas': ['Ferro', 'Cobre', 'Ouro'],
                                            'correta': 0},
                                           {'pergunta': 'O que acontece quando polos iguais de dois ímãs se '
                                                        'aproximam?',
                                            'alternativas': ['Perdem todo o magnetismo',
                                                             'Atraem-se',
                                                             'Repelem-se'],
                                            'correta': 2},
                                           {'pergunta': 'O que existe ao redor de um ímã?',
                                            'alternativas': ['Uma onda sonora contínua',
                                                             'Uma carga elétrica obrigatória',
                                                             'Um campo magnético'],
                                            'correta': 2}],
 'Como funciona uma bateria?': [{'pergunta': 'Uma bateria transforma energia química em qual tipo de '
                                             'energia?',
                                 'alternativas': ['Nuclear', 'Elétrica', 'Térmica apenas'],
                                 'correta': 1},
                                {'pergunta': 'Como se chamam os dois terminais de uma pilha comum?',
                                 'alternativas': ['Positivo e negativo', 'Claro e escuro', 'Quente e frio'],
                                 'correta': 0},
                                {'pergunta': 'Qual característica diferencia uma bateria recarregável?',
                                 'alternativas': ['Poder receber carga novamente',
                                                  'Nunca perder energia',
                                                  'Funcionar sem reações químicas'],
                                 'correta': 0}]}

LEGENDAS = {'Aves e suas curiosidades': 'CAPA_SEGUNDOS=2\n'
                             '\n'
                             'Aves e suas curiosidades! Teste seus conhecimentos em três perguntas. Quantas '
                             'você acertou? Conte nos comentários!\n'
                             '\n'
                             '#Aves #Papagaios #Corujas #CuriosidadesDasAves',
 'Répteis e suas características': 'CAPA_SEGUNDOS=2\n'
                                   '\n'
                                   'Répteis e suas características! Teste seus conhecimentos em três '
                                   'perguntas. Quantas você acertou? Conte nos comentários!\n'
                                   '\n'
                                   '#Repteis #Jiboia #Camaleao #Jabuti',
 'Insetos e pequenos bichos': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Insetos e pequenos bichos! Teste seus conhecimentos em três perguntas. '
                              'Quantas você acertou? Conte nos comentários!\n'
                              '\n'
                              '#Insetos #Abelhas #Borboletas #Aracnideos',
 'Legumes e verduras': 'CAPA_SEGUNDOS=2\n'
                       '\n'
                       'Legumes e verduras! Teste seus conhecimentos em três perguntas. Quantas você '
                       'acertou? Conte nos comentários!\n'
                       '\n'
                       '#Hortalicas #Cenoura #Alface #Batata',
 'Comidas típicas brasileiras': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Comidas típicas brasileiras! Teste seus conhecimentos em três perguntas. '
                                'Quantas você acertou? Conte nos comentários!\n'
                                '\n'
                                '#ComidaBrasileira #Feijoada #Tapioca #PaoDeQueijo',
 'Objetos antigos do cotidiano': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Objetos antigos do cotidiano! Teste seus conhecimentos em três perguntas. '
                                 'Quantas você acertou? Conte nos comentários!\n'
                                 '\n'
                                 '#ObjetosAntigos #Gramofone #MaquinaDeEscrever #MemoriaDoCotidiano',
 'Aparelhos domésticos': 'CAPA_SEGUNDOS=2\n'
                         '\n'
                         'Aparelhos domésticos! Teste seus conhecimentos em três perguntas. Quantas você '
                         'acertou? Conte nos comentários!\n'
                         '\n'
                         '#Eletrodomesticos #Geladeira #AspiradorDePo #FerroDePassar',
 'Brinquedos tradicionais': 'CAPA_SEGUNDOS=2\n'
                            '\n'
                            'Brinquedos tradicionais! Teste seus conhecimentos em três perguntas. Quantas '
                            'você acertou? Conte nos comentários!\n'
                            '\n'
                            '#BrinquedosTradicionais #Pipa #Piao #BolaDeGude',
 'Chapéus e acessórios': 'CAPA_SEGUNDOS=2\n'
                         '\n'
                         'Chapéus e acessórios! Teste seus conhecimentos em três perguntas. Quantas você '
                         'acertou? Conte nos comentários!\n'
                         '\n'
                         '#Chapeus #Acessorios #Gorro #Cachecol',
 'Objetos de costura': 'CAPA_SEGUNDOS=2\n'
                       '\n'
                       'Objetos de costura! Teste seus conhecimentos em três perguntas. Quantas você '
                       'acertou? Conte nos comentários!\n'
                       '\n'
                       '#Costura #Dedal #FitaMetrica #Tesoura',
 'Curiosidades sobre o sono': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Curiosidades sobre o sono! Teste seus conhecimentos em três perguntas. '
                              'Quantas você acertou? Conte nos comentários!\n'
                              '\n'
                              '#Sono #SonoREM #Melatonina #CienciaDoSono',
 'Como funciona a memória?': 'CAPA_SEGUNDOS=2\n'
                             '\n'
                             'Como funciona a memória?! Teste seus conhecimentos em três perguntas. Quantas '
                             'você acertou? Conte nos comentários!\n'
                             '\n'
                             '#Memoria #Hipocampo #Aprendizagem #Cerebro',
 'Por que sentimos cócegas?': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Por que sentimos cócegas?! Teste seus conhecimentos em três perguntas. '
                              'Quantas você acertou? Conte nos comentários!\n'
                              '\n'
                              '#Cocegas #Toque #SistemaNervoso #Percepcao',
 'Por que bocejamos?': 'CAPA_SEGUNDOS=2\n'
                       '\n'
                       'Por que bocejamos?! Teste seus conhecimentos em três perguntas. Quantas você '
                       'acertou? Conte nos comentários!\n'
                       '\n'
                       '#Bocejo #BocejoContagioso #Sonolencia #CorpoHumano',
 'Como percebemos os sabores?': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Como percebemos os sabores?! Teste seus conhecimentos em três perguntas. '
                                'Quantas você acertou? Conte nos comentários!\n'
                                '\n'
                                '#Paladar #Sabores #Umami #BotõesGustativos',
 'Como sentimos os cheiros?': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Como sentimos os cheiros?! Teste seus conhecimentos em três perguntas. '
                              'Quantas você acertou? Conte nos comentários!\n'
                              '\n'
                              '#Olfato #Cheiros #Nariz #PercepcaoOlfativa',
 'Por que nossa voz muda em gravações?': 'CAPA_SEGUNDOS=2\n'
                                         '\n'
                                         'Por que nossa voz muda em gravações?! Teste seus conhecimentos em '
                                         'três perguntas. Quantas você acertou? Conte nos comentários!\n'
                                         '\n'
                                         '#Voz #Gravacao #Acustica #ConducaoOssea',
 'Como os animais se comunicam?': 'CAPA_SEGUNDOS=2\n'
                                  '\n'
                                  'Como os animais se comunicam?! Teste seus conhecimentos em três '
                                  'perguntas. Quantas você acertou? Conte nos comentários!\n'
                                  '\n'
                                  '#ComunicacaoAnimal #Abelhas #Lobos #Feromonios',
 'Animais que vivem em sociedade': 'CAPA_SEGUNDOS=2\n'
                                   '\n'
                                   'Animais que vivem em sociedade! Teste seus conhecimentos em três '
                                   'perguntas. Quantas você acertou? Conte nos comentários!\n'
                                   '\n'
                                   '#AnimaisSociais #Formigas #Abelhas #Colonias',
 'Como as plantas espalham suas sementes?': 'CAPA_SEGUNDOS=2\n'
                                            '\n'
                                            'Como as plantas espalham suas sementes?! Teste seus '
                                            'conhecimentos em três perguntas. Quantas você acertou? Conte '
                                            'nos comentários!\n'
                                            '\n'
                                            '#Sementes #DispersaoDeSementes #Plantas #Botanica',
 'Plantas que vivem no deserto': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Plantas que vivem no deserto! Teste seus conhecimentos em três perguntas. '
                                 'Quantas você acertou? Conte nos comentários!\n'
                                 '\n'
                                 '#PlantasDoDeserto #Cactos #Suculentas #AdaptacaoVegetal',
 'Curiosidades sobre os bambus': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Curiosidades sobre os bambus! Teste seus conhecimentos em três perguntas. '
                                 'Quantas você acertou? Conte nos comentários!\n'
                                 '\n'
                                 '#Bambu #Gramineas #Rizomas #Botanica',
 'A história dos números': 'CAPA_SEGUNDOS=2\n'
                           '\n'
                           'A história dos números! Teste seus conhecimentos em três perguntas. Quantas você '
                           'acertou? Conte nos comentários!\n'
                           '\n'
                           '#HistoriaDosNumeros #NumeracaoRomana #SistemaDecimal #Babilonia',
 'A origem do alfabeto': 'CAPA_SEGUNDOS=2\n'
                         '\n'
                         'A origem do alfabeto! Teste seus conhecimentos em três perguntas. Quantas você '
                         'acertou? Conte nos comentários!\n'
                         '\n'
                         '#Alfabeto #Fenicios #Letras #AlfabetoLatino',
 'Como surgiram os jogos de tabuleiro?': 'CAPA_SEGUNDOS=2\n'
                                         '\n'
                                         'Como surgiram os jogos de tabuleiro?! Teste seus conhecimentos em '
                                         'três perguntas. Quantas você acertou? Conte nos comentários!\n'
                                         '\n'
                                         '#JogosDeTabuleiro #Senet #Xadrez #HistoriaDosJogos',
 'A história do cinema': 'CAPA_SEGUNDOS=2\n'
                         '\n'
                         'A história do cinema! Teste seus conhecimentos em três perguntas. Quantas você '
                         'acertou? Conte nos comentários!\n'
                         '\n'
                         '#HistoriaDoCinema #IrmaosLumiere #CinemaMudo #SetimaArte',
 'Como o rádio transmite o som?': 'CAPA_SEGUNDOS=2\n'
                                  '\n'
                                  'Como o rádio transmite o som?! Teste seus conhecimentos em três '
                                  'perguntas. Quantas você acertou? Conte nos comentários!\n'
                                  '\n'
                                  '#Radio #OndasEletromagneticas #FrequenciaModulada #Comunicacao',
 'Como funciona o controle remoto?': 'CAPA_SEGUNDOS=2\n'
                                     '\n'
                                     'Como funciona o controle remoto?! Teste seus conhecimentos em três '
                                     'perguntas. Quantas você acertou? Conte nos comentários!\n'
                                     '\n'
                                     '#ControleRemoto #Infravermelho #Bluetooth #TecnologiaDomestica',
 'Por que os ímãs atraem alguns metais?': 'CAPA_SEGUNDOS=2\n'
                                          '\n'
                                          'Por que os ímãs atraem alguns metais?! Teste seus conhecimentos '
                                          'em três perguntas. Quantas você acertou? Conte nos comentários!\n'
                                          '\n'
                                          '#Imas #Magnetismo #Ferro #CampoMagnetico',
 'Como funciona uma bateria?': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'Como funciona uma bateria?! Teste seus conhecimentos em três perguntas. '
                               'Quantas você acertou? Conte nos comentários!\n'
                               '\n'
                               '#Baterias #Pilhas #EnergiaEletrica #Eletroquimica'}
