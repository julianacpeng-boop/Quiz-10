# -*- coding: utf-8 -*-
"""Quiz-10 — lote 5: 30 temas, 90 perguntas e 30 montagens em caricatura.
Vídeos 1–10: A à esquerda, B ao centro e C à direita, em 1536 × 1024.
"""

QUIZZES = {'Mamíferos da África': [{'pergunta': 'Qual destes animais é considerado o mamífero terrestre mais rápido?',
                          'alternativas': ['Elefante-africano', 'Leão', 'Guepardo'],
                          'correta': 2,
                          'imagem': 'imagens_perguntas/lote5_caricatura_v01_p01.png'},
                         {'pergunta': 'Qual destes mamíferos pode passar grande parte do dia dentro de rios '
                                      'e lagos?',
                          'alternativas': ['Zebra', 'Hipopótamo', 'Guepardo'],
                          'correta': 1,
                          'imagem': 'imagens_perguntas/lote5_caricatura_v01_p02.png'},
                         {'pergunta': 'Qual destes animais é um felino que costuma viver em grupos chamados '
                                      'de bandos?',
                          'alternativas': ['Leão', 'Girafa', 'Rinoceronte'],
                          'correta': 0,
                          'imagem': 'imagens_perguntas/lote5_caricatura_v01_p03.png'}],
 'Animais da fauna brasileira': [{'pergunta': 'Qual destes animais é o maior roedor do mundo?',
                                  'alternativas': ['Capivara', 'Tamanduá-bandeira', 'Tatu'],
                                  'correta': 0,
                                  'imagem': 'imagens_perguntas/lote5_caricatura_v02_p01.png'},
                                 {'pergunta': 'Qual destes animais pertence à família dos felinos?',
                                  'alternativas': ['Capivara', 'Lobo-guará', 'Onça-pintada'],
                                  'correta': 2,
                                  'imagem': 'imagens_perguntas/lote5_caricatura_v02_p02.png'},
                                 {'pergunta': 'Qual destes animais tem uma dieta baseada principalmente em '
                                              'formigas e cupins?',
                                  'alternativas': ['Lobo-guará', 'Tamanduá-bandeira', 'Onça-pintada'],
                                  'correta': 1,
                                  'imagem': 'imagens_perguntas/lote5_caricatura_v02_p03.png'}],
 'Peixes de água doce': [{'pergunta': 'Qual destes peixes tem importância histórica na aquicultura e é '
                                      'originário da África?',
                          'alternativas': ['Pirarucu', 'Tilápia', 'Dourado'],
                          'correta': 1,
                          'imagem': 'imagens_perguntas/lote5_caricatura_v03_p01.png'},
                         {'pergunta': 'Qual destes peixes amazônicos precisa subir à superfície para '
                                      'respirar ar?',
                          'alternativas': ['Pirarucu', 'Tucunaré', 'Tambaqui'],
                          'correta': 0,
                          'imagem': 'imagens_perguntas/lote5_caricatura_v03_p02.png'},
                         {'pergunta': 'Qual destes peixes pertence ao gênero Salminus?',
                          'alternativas': ['Tambaqui', 'Tilápia', 'Dourado'],
                          'correta': 2,
                          'imagem': 'imagens_perguntas/lote5_caricatura_v03_p03.png'}],
 'Frutas menos conhecidas': [{'pergunta': 'Qual destas frutas é conhecida no Brasil também como '
                                          'fruta-do-dragão?',
                              'alternativas': ['Pitaya', 'Carambola', 'Rambutã'],
                              'correta': 0,
                              'imagem': 'imagens_perguntas/lote5_caricatura_v04_p01.png'},
                             {'pergunta': 'Qual destas frutas é originária do Sudeste Asiático e pertence à '
                                          'mesma família do lichia?',
                              'alternativas': ['Pitaya', 'Mangostão', 'Rambutã'],
                              'correta': 2,
                              'imagem': 'imagens_perguntas/lote5_caricatura_v04_p02.png'},
                             {'pergunta': 'Qual destas frutas é conhecida também como uchuva?',
                              'alternativas': ['Mangostão', 'Carambola', 'Physalis'],
                              'correta': 2,
                              'imagem': 'imagens_perguntas/lote5_caricatura_v04_p03.png'}],
 'Temperos e especiarias': [{'pergunta': 'Qual destas especiarias é um botão floral seco?',
                             'alternativas': ['Canela', 'Noz-moscada', 'Cravo-da-índia'],
                             'correta': 2,
                             'imagem': 'imagens_perguntas/lote5_caricatura_v05_p01.png'},
                            {'pergunta': 'Qual destes temperos costuma dar uma cor amarela intensa aos '
                                         'alimentos?',
                             'alternativas': ['Pimenta-do-reino', 'Cúrcuma', 'Orégano'],
                             'correta': 1,
                             'imagem': 'imagens_perguntas/lote5_caricatura_v05_p02.png'},
                            {'pergunta': 'Qual destas especiarias é obtida da casca de uma árvore?',
                             'alternativas': ['Canela', 'Cravo-da-índia', 'Pimenta-do-reino'],
                             'correta': 0,
                             'imagem': 'imagens_perguntas/lote5_caricatura_v05_p03.png'}],
 'Queijos e suas origens': [{'pergunta': 'Qual destes queijos é tradicionalmente associado à Grécia?',
                             'alternativas': ['Feta', 'Parmesão', 'Gouda'],
                             'correta': 0,
                             'imagem': 'imagens_perguntas/lote5_caricatura_v06_p01.png'},
                            {'pergunta': 'Qual destes queijos tem origem tradicional nos Países Baixos?',
                             'alternativas': ['Brie', 'Gouda', 'Feta'],
                             'correta': 1,
                             'imagem': 'imagens_perguntas/lote5_caricatura_v06_p02.png'},
                            {'pergunta': 'Qual destes queijos é tradicionalmente italiano?',
                             'alternativas': ['Gouda', 'Brie', 'Parmesão'],
                             'correta': 2,
                             'imagem': 'imagens_perguntas/lote5_caricatura_v06_p03.png'}],
 'Objetos de jardinagem': [{'pergunta': 'Qual destes objetos pode ajudar a revolver e transportar terra?',
                            'alternativas': ['Luvas de jardinagem', 'Regador', 'Pá'],
                            'correta': 2,
                            'imagem': 'imagens_perguntas/lote5_caricatura_v07_p01.png'},
                           {'pergunta': 'Qual destes objetos ajuda a aplicar água de forma controlada nas '
                                        'plantas?',
                            'alternativas': ['Regador', 'Rastelo', 'Pá'],
                            'correta': 0,
                            'imagem': 'imagens_perguntas/lote5_caricatura_v07_p02.png'},
                           {'pergunta': 'Qual destes objetos é mais indicado para cortar pequenos galhos?',
                            'alternativas': ['Regador', 'Tesoura de poda', 'Rastelo'],
                            'correta': 1,
                            'imagem': 'imagens_perguntas/lote5_caricatura_v07_p03.png'}],
 'Instrumentos de observação': [{'pergunta': 'Qual destes instrumentos é usado para observar células?',
                                 'alternativas': ['Microscópio', 'Telescópio', 'Binóculo'],
                                 'correta': 0,
                                 'imagem': 'imagens_perguntas/lote5_caricatura_v08_p01.png'},
                                {'pergunta': 'Qual destes instrumentos é mais associado à observação de '
                                             'planetas?',
                                 'alternativas': ['Lupa', 'Telescópio', 'Microscópio'],
                                 'correta': 1,
                                 'imagem': 'imagens_perguntas/lote5_caricatura_v08_p02.png'},
                                {'pergunta': 'Qual destes instrumentos é muito usado para observar aves à '
                                             'distância?',
                                 'alternativas': ['Microscópio', 'Lupa', 'Binóculo'],
                                 'correta': 2,
                                 'imagem': 'imagens_perguntas/lote5_caricatura_v08_p03.png'}],
 'Materiais usados em construções': [{'pergunta': 'Qual destes materiais é produzido a partir do tronco de '
                                                  'árvores?',
                                      'alternativas': ['Tijolo cerâmico', 'Tábua de madeira', 'Barra de aço'],
                                      'correta': 1,
                                      'imagem': 'imagens_perguntas/lote5_caricatura_v09_p01.png'},
                                     {'pergunta': 'Qual destes materiais é utilizado como ligante na '
                                                  'preparação de concreto?',
                                      'alternativas': ['Areia', 'Brita', 'Cimento'],
                                      'correta': 2,
                                      'imagem': 'imagens_perguntas/lote5_caricatura_v09_p02.png'},
                                     {'pergunta': 'Qual destes materiais é produzido tradicionalmente a '
                                                  'partir de argila queimada?',
                                      'alternativas': ['Tijolo cerâmico', 'Tábua de madeira', 'Barra de aço'],
                                      'correta': 0,
                                      'imagem': 'imagens_perguntas/lote5_caricatura_v09_p03.png'}],
 'Objetos de higiene pessoal': [{'pergunta': 'Qual destes objetos é usado para pentear e desembaraçar os '
                                             'cabelos?',
                                 'alternativas': ['Sabonete', 'Fio dental', 'Pente'],
                                 'correta': 2,
                                 'imagem': 'imagens_perguntas/lote5_caricatura_v10_p01.png'},
                                {'pergunta': 'Qual destes objetos é usado junto à pasta de dentes?',
                                 'alternativas': ['Pente', 'Escova de dentes', 'Toalha'],
                                 'correta': 1,
                                 'imagem': 'imagens_perguntas/lote5_caricatura_v10_p02.png'},
                                {'pergunta': 'Qual destes objetos ajuda a remover resíduos entre os dentes?',
                                 'alternativas': ['Fio dental', 'Escova de cabelo', 'Sabonete'],
                                 'correta': 0,
                                 'imagem': 'imagens_perguntas/lote5_caricatura_v10_p03.png'}],
 'Por que soluçamos?': [{'pergunta': 'Qual situação pode favorecer o aparecimento de soluços?',
                         'alternativas': ['Ler em silêncio', 'Comer muito rápido', 'Pentear o cabelo'],
                         'correta': 1},
                        {'pergunta': 'O soluço envolve contrações involuntárias de qual músculo?',
                         'alternativas': ['Diafragma', 'Bíceps', 'Trapézio'],
                         'correta': 0},
                        {'pergunta': 'O som do soluço ocorre com o fechamento rápido de qual estrutura?',
                         'alternativas': ['Glote', 'Narina', 'Esôfago'],
                         'correta': 0}],
 'Por que nossos dedos enrugam na água?': [{'pergunta': 'Esse efeito é mais observado em quais regiões?',
                                            'alternativas': ['Costas e barriga',
                                                             'Braços e pernas inteiros',
                                                             'Pontas dos dedos e plantas dos pés'],
                                            'correta': 2},
                                           {'pergunta': 'O que acontece com vasos sanguíneos dos dedos nesse '
                                                        'processo?',
                                            'alternativas': ['Eles se dilatam sempre',
                                                             'Eles param de conduzir sangue para sempre',
                                                             'Eles se contraem'],
                                            'correta': 2},
                                           {'pergunta': 'O enrugamento dos dedos na água envolve qual '
                                                        'sistema?',
                                            'alternativas': ['Sistema nervoso autônomo',
                                                             'Sistema digestório',
                                                             'Sistema reprodutor'],
                                            'correta': 0}],
 'Como o corpo mantém sua temperatura?': [{'pergunta': 'Como o suor ajuda a resfriar o corpo?',
                                           'alternativas': ['Pelo aumento da pressão arterial',
                                                            'Pelo aumento da viscosidade',
                                                            'Pela evaporação'],
                                           'correta': 2},
                                          {'pergunta': 'Como os tremores ajudam no frio?',
                                           'alternativas': ['Produzindo calor pela atividade muscular',
                                                            'Reduzindo a atividade muscular',
                                                            'Diminuindo o metabolismo'],
                                           'correta': 0},
                                          {'pergunta': 'Qual região do cérebro participa do controle da '
                                                       'temperatura corporal?',
                                           'alternativas': ['Hipocampo', 'Cerebelo', 'Hipotálamo'],
                                           'correta': 2}],
 'Por que sentimos sede?': [{'pergunta': 'Qual alteração pode estimular a sede?',
                             'alternativas': ['Aumento da concentração de sais no sangue',
                                              'Mais ar nos pulmões',
                                              'Diminuição da temperatura dos ossos'],
                             'correta': 0},
                            {'pergunta': 'Quais órgãos ajustam a quantidade de água eliminada na urina?',
                             'alternativas': ['Rins', 'Estômago', 'Pulmão'],
                             'correta': 0},
                            {'pergunta': 'A sede ajuda a regular principalmente o quê?',
                             'alternativas': ['Crescimento do cabelo',
                                              'Cor da pele',
                                              'Equilíbrio de água no corpo'],
                             'correta': 2}],
 'Como uma ferida cicatriza?': [{'pergunta': 'Qual processo ajuda a interromper o sangramento após um corte?',
                                 'alternativas': ['Coagulação', 'Respiração', 'Digestão'],
                                 'correta': 0},
                                {'pergunta': 'Qual proteína tem papel importante na formação do tecido de '
                                             'reparo?',
                                 'alternativas': ['Colágeno', 'Insulina', 'Melatonina'],
                                 'correta': 0},
                                {'pergunta': 'Na cicatrização, o que acontece com o tecido lesionado?',
                                 'alternativas': ['Passa por um processo de reparo',
                                                  'Deixa de receber sangue para sempre',
                                                  'É sempre substituído por osso'],
                                 'correta': 0}],
 'Por que algumas pessoas são canhotas?': [{'pergunta': 'Ser canhoto significa ter preferência por qual mão?',
                                            'alternativas': ['Direita', 'Esquerda', 'Nenhuma'],
                                            'correta': 1},
                                           {'pergunta': 'A preferência por uma mão é influenciada por quais '
                                                        'fatores?',
                                            'alternativas': ['Apenas pela posição ao dormir',
                                                             'Fatores genéticos e do desenvolvimento',
                                                             'Somente pelo tipo de alimento'],
                                            'correta': 1},
                                           {'pergunta': 'Quem consegue usar as duas mãos com habilidade '
                                                        'semelhante é chamado de quê?',
                                            'alternativas': ['Canhoto apenas', 'Destro', 'Ambidestro'],
                                            'correta': 2}],
 'Como os morcegos se orientam?': [{'pergunta': 'Na ecolocalização, o animal analisa principalmente o quê?',
                                    'alternativas': ['Ecos de sons emitidos',
                                                     'Somente o cheiro do ar',
                                                     'A cor dos objetos'],
                                    'correta': 0},
                                   {'pergunta': 'Qual recurso muitos morcegos usam para se orientar no '
                                                'escuro?',
                                    'alternativas': ['Ecolocalização', 'Olfato apenas', 'Visão de raios X'],
                                    'correta': 0},
                                   {'pergunta': 'Os sons usados por muitos morcegos na ecolocalização são de '
                                                'qual tipo?',
                                    'alternativas': ['Ultrassons',
                                                     'Infrassons apenas',
                                                     'Sempre audíveis aos humanos'],
                                    'correta': 0}],
 'Como os peixes respiram?': [{'pergunta': 'Qual estrutura permite a muitos peixes retirar oxigênio da água?',
                               'alternativas': ['Barbatanas', 'Escamas', 'Brânquias'],
                               'correta': 2},
                              {'pergunta': 'Por que a passagem de água pelas brânquias é importante?',
                               'alternativas': ['Para endurecer as nadadeiras',
                                                'Para permitir trocas gasosas',
                                                'Para criar novas escamas'],
                               'correta': 1},
                              {'pergunta': 'Qual substância dissolvida na água é usada na respiração?',
                               'alternativas': ['Nitrogênio sólido', 'Oxigênio', 'Hidrogênio puro'],
                               'correta': 1}],
 'Por que algumas aves migram?': [{'pergunta': 'Qual destas pistas pode ajudar aves a se orientar?',
                                   'alternativas': ['Somente os sons dos carros',
                                                    'Campo magnético da Terra',
                                                    'Cheiro de combustíveis'],
                                   'correta': 1},
                                  {'pergunta': 'Qual fator pode favorecer a migração de aves?',
                                   'alternativas': ['Mudanças sazonais na oferta de alimento',
                                                    'Mudança na cor das pedras',
                                                    'Aumento do tamanho do bico'],
                                   'correta': 0},
                                  {'pergunta': 'A migração de aves geralmente envolve o quê?',
                                   'alternativas': ['Ficar sempre no mesmo ninho',
                                                    'Deslocamentos sazonais entre regiões',
                                                    'Trocar de espécie'],
                                   'correta': 1}],
 'Como as aranhas produzem suas teias?': [{'pergunta': 'Além de capturar presas, para que a seda pode ser '
                                                       'usada?',
                                           'alternativas': ['Para proteger ovos',
                                                            'Para produzir mel',
                                                            'Para produzir néctar'],
                                           'correta': 0},
                                          {'pergunta': 'Como se chamam as estruturas por onde os fios de '
                                                       'seda saem?',
                                           'alternativas': ['Antenas', 'Fiandeiras', 'Brânquias'],
                                           'correta': 1},
                                          {'pergunta': 'Onde a seda das aranhas é produzida?',
                                           'alternativas': ['Olhos', 'Patas apenas', 'Glândulas de seda'],
                                           'correta': 2}],
 'Por que as folhas mudam de cor?': [{'pergunta': 'Qual pigmento dá a cor verde a muitas folhas?',
                                      'alternativas': ['Hemoglobina', 'Melanina', 'Clorofila'],
                                      'correta': 2},
                                     {'pergunta': 'O que pode ocorrer no outono com a clorofila de certas '
                                                  'árvores?',
                                      'alternativas': ['Transforma-se em raízes',
                                                       'Ela se degrada',
                                                       'Passa a produzir oxigênio sem luz'],
                                      'correta': 1},
                                     {'pergunta': 'Quais pigmentos podem contribuir para tons amarelos e '
                                                  'alaranjados?',
                                      'alternativas': ['Clorofilas apenas', 'Melaninas', 'Carotenoides'],
                                      'correta': 2}],
 'Como as flores atraem polinizadores?': [{'pergunta': 'Qual destes animais pode atuar como polinizador?',
                                           'alternativas': ['Minhoca apenas', 'Abelha', 'Tubarão'],
                                           'correta': 1},
                                          {'pergunta': 'Qual recurso pode atrair animais polinizadores?',
                                           'alternativas': ['Sal de cozinha',
                                                            'Resina de construção',
                                                            'Néctar'],
                                           'correta': 2},
                                          {'pergunta': 'O que a polinização envolve?',
                                           'alternativas': ['Transporte de raízes',
                                                            'Transferência de pólen',
                                                            'Troca de folhas entre plantas'],
                                           'correta': 1}],
 'Como funciona uma panela de pressão?': [{'pergunta': 'Com pressão maior, a água pode ferver em qual '
                                                       'condição?',
                                           'alternativas': ['Somente a 50 graus',
                                                            'Em temperatura mais alta',
                                                            'Sempre abaixo de zero'],
                                           'correta': 1},
                                          {'pergunta': 'O que aumenta dentro de uma panela de pressão '
                                                       'durante o uso?',
                                           'alternativas': ['Volume do metal da tampa',
                                                            'Quantidade de oxigênio externo',
                                                            'Pressão do vapor'],
                                           'correta': 2},
                                          {'pergunta': 'Qual componente ajuda a controlar a pressão durante '
                                                       'o funcionamento?',
                                           'alternativas': ['Cabo lateral', 'Válvula', 'Base externa'],
                                           'correta': 1}],
 'Por que o óleo não se mistura com a água?': [{'pergunta': 'Como é classificada a molécula de água quanto à '
                                                            'polaridade?',
                                                'alternativas': ['Apolar', 'Polar', 'Metálica'],
                                                'correta': 1},
                                               {'pergunta': 'Em geral, óleos de cozinha são '
                                                            'predominantemente de qual tipo?',
                                                'alternativas': ['Apolares', 'Metálicos', 'Iônicos'],
                                                'correta': 0},
                                               {'pergunta': 'Como se chama uma mistura de gotículas de óleo '
                                                            'dispersas na água?',
                                                'alternativas': ['Cristal', 'Emulsão', 'Liga metálica'],
                                                'correta': 1}],
 'Como funciona um forno de micro-ondas?': [{'pergunta': 'Qual tipo de radiação é usado no forno de '
                                                         'micro-ondas?',
                                             'alternativas': ['Eletromagnética',
                                                              'Radioativa nuclear',
                                                              'Ultravioleta apenas'],
                                             'correta': 0},
                                            {'pergunta': 'Qual componente dos alimentos tem grande '
                                                         'participação no aquecimento por micro-ondas?',
                                             'alternativas': ['Água',
                                                              'Ar da embalagem',
                                                              'Ferro sólido apenas'],
                                             'correta': 0},
                                            {'pergunta': 'Qual componente gera as micro-ondas em muitos '
                                                         'desses fornos?',
                                             'alternativas': ['Compressor', 'Magnetron', 'Termostato apenas'],
                                             'correta': 1}],
 'Como o som produz eco?': [{'pergunta': 'Qual superfície tende a refletir bem o som?',
                             'alternativas': ['Espuma macia', 'Parede de concreto', 'Cobertor grosso'],
                             'correta': 1},
                            {'pergunta': 'Para ouvir um eco separado da fala, o som refletido precisa chegar '
                                         'como?',
                             'alternativas': ['Com atraso suficiente',
                                              'Exatamente ao mesmo tempo',
                                              'Antes do som original'],
                             'correta': 0},
                            {'pergunta': 'O eco resulta de qual fenômeno?',
                             'alternativas': ['Refração da luz', 'Evaporação da água', 'Reflexão do som'],
                             'correta': 2}],
 'Por que vemos relâmpagos antes de ouvir trovões?': [{'pergunta': 'Um intervalo maior entre relâmpago e '
                                                                   'trovão geralmente indica o quê?',
                                                       'alternativas': ['Uma descarga mais distante',
                                                                        'Uma nuvem menor',
                                                                        'Uma chuva mais quente'],
                                                       'correta': 0},
                                                      {'pergunta': 'O trovão é causado principalmente por '
                                                                   'qual fenômeno?',
                                                       'alternativas': ['Expansão rápida do ar aquecido pelo '
                                                                        'relâmpago',
                                                                        'Vento passando sobre o solo',
                                                                        'Choque entre gotas de chuva'],
                                                       'correta': 0},
                                                      {'pergunta': 'Qual se propaga mais rápido no ar?',
                                                       'alternativas': ['Ambos na mesma velocidade',
                                                                        'Som',
                                                                        'Luz'],
                                                       'correta': 2}],
 'Como funciona uma tela sensível ao toque?': [{'pergunta': 'Como é chamado o tipo de tela que detecta '
                                                            'pressão entre camadas?',
                                                'alternativas': ['Tela de projeção apenas',
                                                                 'Tela de papel',
                                                                 'Tela resistiva'],
                                                'correta': 2},
                                               {'pergunta': 'Em uma tela, o que significa multitoque?',
                                                'alternativas': ['Mostrar várias fotos',
                                                                 'Reconhecer mais de um toque ao mesmo tempo',
                                                                 'Usar várias baterias'],
                                                'correta': 1},
                                               {'pergunta': 'Muitas telas de celulares detectam mudanças em '
                                                            'qual propriedade?',
                                                'alternativas': ['Peso do aparelho',
                                                                 'Pressão do ar',
                                                                 'Capacitância elétrica'],
                                                'correta': 2}],
 'Como os satélites ajudam na localização?': [{'pergunta': 'Em condições normais, quantos satélites são '
                                                           'necessários para calcular posição 3D e corrigir '
                                                           'o relógio do receptor?',
                                               'alternativas': ['Um', 'Pelo menos quatro', 'Dois'],
                                               'correta': 1},
                                              {'pergunta': 'Para calcular distâncias, o receptor usa '
                                                           'informações ligadas a quê?',
                                               'alternativas': ['Peso do satélite',
                                                                'Cor da antena',
                                                                'Tempo de viagem dos sinais'],
                                               'correta': 2},
                                              {'pergunta': 'O GPS recebe sinais enviados por quê?',
                                               'alternativas': ['Cabos subterrâneos apenas',
                                                                'Boias oceânicas apenas',
                                                                'Satélites'],
                                               'correta': 2}],
 'Como uma impressora imprime?': [{'pergunta': 'Uma impressora a laser costuma usar qual material?',
                                   'alternativas': ['Tinta a óleo', 'Água colorida', 'Toner'],
                                   'correta': 2},
                                  {'pergunta': 'Para que serve o fusor em muitas impressoras a laser?',
                                   'alternativas': ['Digitalizar documentos',
                                                    'Fixar o toner no papel com calor e pressão',
                                                    'Apagar o papel'],
                                   'correta': 1},
                                  {'pergunta': 'Uma impressora a jato de tinta usa qual material para formar '
                                               'a imagem?',
                                   'alternativas': ['Gotículas de tinta',
                                                    'Toner em pó apenas',
                                                    'Fita de carbono apenas'],
                                   'correta': 0}]}

LEGENDAS = {'Mamíferos da África': 'CAPA_SEGUNDOS=2\n'
                        '\n'
                        'Mamíferos da África! Três perguntas para testar seus conhecimentos. Comente quantas '
                        'você acertou!\n'
                        '\n'
                        '#MamiferosDaAfrica #Leoes #Hipopotamos #Guepardos',
 'Animais da fauna brasileira': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Animais da fauna brasileira! Três perguntas para testar seus conhecimentos. '
                                'Comente quantas você acertou!\n'
                                '\n'
                                '#FaunaBrasileira #Capivara #Tamandua #OncaPintada',
 'Peixes de água doce': 'CAPA_SEGUNDOS=2\n'
                        '\n'
                        'Peixes de água doce! Três perguntas para testar seus conhecimentos. Comente quantas '
                        'você acertou!\n'
                        '\n'
                        '#PeixesDeAguaDoce #Pirarucu #Tilapia #Dourado',
 'Frutas menos conhecidas': 'CAPA_SEGUNDOS=2\n'
                            '\n'
                            'Frutas menos conhecidas! Três perguntas para testar seus conhecimentos. Comente '
                            'quantas você acertou!\n'
                            '\n'
                            '#Frutas #Pitaya #Physalis #Rambuta',
 'Temperos e especiarias': 'CAPA_SEGUNDOS=2\n'
                           '\n'
                           'Temperos e especiarias! Três perguntas para testar seus conhecimentos. Comente '
                           'quantas você acertou!\n'
                           '\n'
                           '#Especiarias #Canela #Curcuma #CravoDaIndia',
 'Queijos e suas origens': 'CAPA_SEGUNDOS=2\n'
                           '\n'
                           'Queijos e suas origens! Três perguntas para testar seus conhecimentos. Comente '
                           'quantas você acertou!\n'
                           '\n'
                           '#Queijos #Feta #Gouda #Parmesao',
 'Objetos de jardinagem': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Objetos de jardinagem! Três perguntas para testar seus conhecimentos. Comente '
                          'quantas você acertou!\n'
                          '\n'
                          '#Jardinagem #Regador #Poda #CultivoDePlantas',
 'Instrumentos de observação': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'Instrumentos de observação! Três perguntas para testar seus conhecimentos. '
                               'Comente quantas você acertou!\n'
                               '\n'
                               '#InstrumentosDeObservacao #Microscopio #Telescopio #Binoculo',
 'Materiais usados em construções': 'CAPA_SEGUNDOS=2\n'
                                    '\n'
                                    'Materiais usados em construções! Três perguntas para testar seus '
                                    'conhecimentos. Comente quantas você acertou!\n'
                                    '\n'
                                    '#Construcao #Tijolo #Madeira #Cimento',
 'Objetos de higiene pessoal': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'Objetos de higiene pessoal! Três perguntas para testar seus conhecimentos. '
                               'Comente quantas você acertou!\n'
                               '\n'
                               '#HigienePessoal #HigieneBucal #FioDental #CuidadosPessoais',
 'Por que soluçamos?': 'CAPA_SEGUNDOS=2\n'
                       '\n'
                       'Por que soluçamos?! Três perguntas para testar seus conhecimentos. Comente quantas '
                       'você acertou!\n'
                       '\n'
                       '#Soluco #Diafragma #Glote #CorpoHumano',
 'Por que nossos dedos enrugam na água?': 'CAPA_SEGUNDOS=2\n'
                                          '\n'
                                          'Por que nossos dedos enrugam na água?! Três perguntas para testar '
                                          'seus conhecimentos. Comente quantas você acertou!\n'
                                          '\n'
                                          '#DedosEnrugados #Pele #SistemaNervoso #Vasoconstricao',
 'Como o corpo mantém sua temperatura?': 'CAPA_SEGUNDOS=2\n'
                                         '\n'
                                         'Como o corpo mantém sua temperatura?! Três perguntas para testar '
                                         'seus conhecimentos. Comente quantas você acertou!\n'
                                         '\n'
                                         '#TemperaturaCorporal #Hipotalamo #Suor #Termorregulacao',
 'Por que sentimos sede?': 'CAPA_SEGUNDOS=2\n'
                           '\n'
                           'Por que sentimos sede?! Três perguntas para testar seus conhecimentos. Comente '
                           'quantas você acertou!\n'
                           '\n'
                           '#Sede #Hidratacao #Rins #EquilibrioHidrico',
 'Como uma ferida cicatriza?': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'Como uma ferida cicatriza?! Três perguntas para testar seus conhecimentos. '
                               'Comente quantas você acertou!\n'
                               '\n'
                               '#Cicatrizacao #Colageno #Coagulacao #ReparoTecidual',
 'Por que algumas pessoas são canhotas?': 'CAPA_SEGUNDOS=2\n'
                                          '\n'
                                          'Por que algumas pessoas são canhotas?! Três perguntas para testar '
                                          'seus conhecimentos. Comente quantas você acertou!\n'
                                          '\n'
                                          '#Canhotos #Lateralidade #Ambidestros #DesenvolvimentoHumano',
 'Como os morcegos se orientam?': 'CAPA_SEGUNDOS=2\n'
                                  '\n'
                                  'Como os morcegos se orientam?! Três perguntas para testar seus '
                                  'conhecimentos. Comente quantas você acertou!\n'
                                  '\n'
                                  '#Morcegos #Ecolocalizacao #Ultrassom #OrientacaoAnimal',
 'Como os peixes respiram?': 'CAPA_SEGUNDOS=2\n'
                             '\n'
                             'Como os peixes respiram?! Três perguntas para testar seus conhecimentos. '
                             'Comente quantas você acertou!\n'
                             '\n'
                             '#Peixes #Branquias #RespiracaoAquatica #Oxigenio',
 'Por que algumas aves migram?': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Por que algumas aves migram?! Três perguntas para testar seus '
                                 'conhecimentos. Comente quantas você acertou!\n'
                                 '\n'
                                 '#MigracaoDeAves #Aves #CampoMagnetico #Natureza',
 'Como as aranhas produzem suas teias?': 'CAPA_SEGUNDOS=2\n'
                                         '\n'
                                         'Como as aranhas produzem suas teias?! Três perguntas para testar '
                                         'seus conhecimentos. Comente quantas você acertou!\n'
                                         '\n'
                                         '#Aranhas #Teias #Seda #Fiandeiras',
 'Por que as folhas mudam de cor?': 'CAPA_SEGUNDOS=2\n'
                                    '\n'
                                    'Por que as folhas mudam de cor?! Três perguntas para testar seus '
                                    'conhecimentos. Comente quantas você acertou!\n'
                                    '\n'
                                    '#Folhas #Clorofila #Carotenoides #Botanica',
 'Como as flores atraem polinizadores?': 'CAPA_SEGUNDOS=2\n'
                                         '\n'
                                         'Como as flores atraem polinizadores?! Três perguntas para testar '
                                         'seus conhecimentos. Comente quantas você acertou!\n'
                                         '\n'
                                         '#Flores #Polinizacao #Nectar #Abelhas',
 'Como funciona uma panela de pressão?': 'CAPA_SEGUNDOS=2\n'
                                         '\n'
                                         'Como funciona uma panela de pressão?! Três perguntas para testar '
                                         'seus conhecimentos. Comente quantas você acertou!\n'
                                         '\n'
                                         '#PanelaDePressao #Vapor #Pressao #PontoDeEbulicao',
 'Por que o óleo não se mistura com a água?': 'CAPA_SEGUNDOS=2\n'
                                              '\n'
                                              'Por que o óleo não se mistura com a água?! Três perguntas '
                                              'para testar seus conhecimentos. Comente quantas você '
                                              'acertou!\n'
                                              '\n'
                                              '#OleoEAgua #Polaridade #Emulsao #Quimica',
 'Como funciona um forno de micro-ondas?': 'CAPA_SEGUNDOS=2\n'
                                           '\n'
                                           'Como funciona um forno de micro-ondas?! Três perguntas para '
                                           'testar seus conhecimentos. Comente quantas você acertou!\n'
                                           '\n'
                                           '#MicroOndas #Magnetron #Aquecimento #OndasEletromagneticas',
 'Como o som produz eco?': 'CAPA_SEGUNDOS=2\n'
                           '\n'
                           'Como o som produz eco?! Três perguntas para testar seus conhecimentos. Comente '
                           'quantas você acertou!\n'
                           '\n'
                           '#Eco #Som #ReflexaoSonora #Acustica',
 'Por que vemos relâmpagos antes de ouvir trovões?': 'CAPA_SEGUNDOS=2\n'
                                                     '\n'
                                                     'Por que vemos relâmpagos antes de ouvir trovões?! Três '
                                                     'perguntas para testar seus conhecimentos. Comente '
                                                     'quantas você acertou!\n'
                                                     '\n'
                                                     '#Relampagos #Trovoes #LuzESom #Tempestades',
 'Como funciona uma tela sensível ao toque?': 'CAPA_SEGUNDOS=2\n'
                                              '\n'
                                              'Como funciona uma tela sensível ao toque?! Três perguntas '
                                              'para testar seus conhecimentos. Comente quantas você '
                                              'acertou!\n'
                                              '\n'
                                              '#TelaTouch #Capacitancia #TelaResistiva #Multitoque',
 'Como os satélites ajudam na localização?': 'CAPA_SEGUNDOS=2\n'
                                             '\n'
                                             'Como os satélites ajudam na localização?! Três perguntas para '
                                             'testar seus conhecimentos. Comente quantas você acertou!\n'
                                             '\n'
                                             '#GPS #Satelites #Geolocalizacao #Navegacao',
 'Como uma impressora imprime?': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Como uma impressora imprime?! Três perguntas para testar seus '
                                 'conhecimentos. Comente quantas você acertou!\n'
                                 '\n'
                                 '#Impressoras #JatoDeTinta #Toner #ImpressaoALaser'}
