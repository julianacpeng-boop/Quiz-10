# Quiz-10 — lote 3: 30 temas, 90 perguntas e 30 montagens em caricatura.
# Três painéis A/B/C da esquerda para a direita, 1536 x 1024 pixels.
# Temas 1 a 10 com imagens; temas 11 a 30 sem imagens.
# correta: 0 = A, 1 = B, 2 = C.

QUIZZES = {'Calçados e suas diferenças': [{'pergunta': 'Qual destes calçados costuma ser usado em atividades '
                                             'esportivas?',
                                 'alternativas': ['Tênis', 'Bota', 'Sandália'],
                                 'correta': 0,
                                 'imagem': 'imagens_perguntas/lote3_caricatura_v01_p01.png'},
                                {'pergunta': 'Qual destes calçados tem o salto fino e elevado?',
                                 'alternativas': ['Chinelo', 'Scarpin', 'Sapatilha'],
                                 'correta': 1,
                                 'imagem': 'imagens_perguntas/lote3_caricatura_v01_p02.png'},
                                {'pergunta': 'Qual destes calçados pode ter cano alto e cobrir parte da '
                                             'perna?',
                                 'alternativas': ['Mocassim', 'Chinelo', 'Bota de cano alto'],
                                 'correta': 2,
                                 'imagem': 'imagens_perguntas/lote3_caricatura_v01_p03.png'}],
 'Bolsas e malas': [{'pergunta': 'Qual destes objetos costuma ser carregado nas costas com duas alças?',
                     'alternativas': ['Mala de viagem', 'Mochila', 'Bolsa de mão'],
                     'correta': 1,
                     'imagem': 'imagens_perguntas/lote3_caricatura_v02_p01.png'},
                    {'pergunta': 'Qual destes objetos costuma ter rodas e alça retrátil para viagens?',
                     'alternativas': ['Mala de viagem', 'Pochete', 'Bolsa de mão'],
                     'correta': 0,
                     'imagem': 'imagens_perguntas/lote3_caricatura_v02_p02.png'},
                    {'pergunta': 'Qual destes acessórios costuma ser preso à cintura?',
                     'alternativas': ['Mochila', 'Mala de viagem', 'Pochete'],
                     'correta': 2,
                     'imagem': 'imagens_perguntas/lote3_caricatura_v02_p03.png'}],
 'Relógios e formas de marcar o tempo': [{'pergunta': 'Qual destes objetos marca o tempo pela passagem de '
                                                      'areia?',
                                          'alternativas': ['Relógio de pulso',
                                                           'Ampulheta',
                                                           'Relógio de parede'],
                                          'correta': 1,
                                          'imagem': 'imagens_perguntas/lote3_caricatura_v03_p01.png'},
                                         {'pergunta': 'Qual destes objetos é usado para medir intervalos de '
                                                      'tempo?',
                                          'alternativas': ['Cronômetro', 'Calendário', 'Relógio de sol'],
                                          'correta': 0,
                                          'imagem': 'imagens_perguntas/lote3_caricatura_v03_p02.png'},
                                         {'pergunta': 'Qual destes objetos indica as horas usando a sombra '
                                                      'do Sol?',
                                          'alternativas': ['Relógio digital',
                                                           'Relógio de cuco',
                                                           'Relógio de sol'],
                                          'correta': 2,
                                          'imagem': 'imagens_perguntas/lote3_caricatura_v03_p03.png'}],
 'Tipos de embarcações': [{'pergunta': 'Qual destas embarcações pode usar o vento nas velas para se mover?',
                           'alternativas': ['Veleiro', 'Canoa', 'Navio cargueiro'],
                           'correta': 0,
                           'imagem': 'imagens_perguntas/lote3_caricatura_v04_p01.png'},
                          {'pergunta': 'Qual destas embarcações é própria para transportar contêineres?',
                           'alternativas': ['Caiaque', 'Navio cargueiro', 'Veleiro'],
                           'correta': 1,
                           'imagem': 'imagens_perguntas/lote3_caricatura_v04_p02.png'},
                          {'pergunta': 'Qual destas embarcações pode navegar submersa?',
                           'alternativas': ['Lancha', 'Jangada', 'Submarino'],
                           'correta': 2,
                           'imagem': 'imagens_perguntas/lote3_caricatura_v04_p03.png'}],
 'Construções e moradias': [{'pergunta': 'Qual destas moradias é tradicionalmente feita com blocos de neve?',
                             'alternativas': ['Chalé', 'Iglu', 'Casa de alvenaria'],
                             'correta': 1,
                             'imagem': 'imagens_perguntas/lote3_caricatura_v05_p01.png'},
                            {'pergunta': 'Qual destas moradias costuma ser montada com tecido e varetas?',
                             'alternativas': ['Barraca', 'Sobrado', 'Chalé'],
                             'correta': 0,
                             'imagem': 'imagens_perguntas/lote3_caricatura_v05_p02.png'},
                            {'pergunta': 'Qual destas moradias é construída sobre estacas em áreas sujeitas '
                                         'a água?',
                             'alternativas': ['Iglu', 'Casa de alvenaria', 'Palafita'],
                             'correta': 2,
                             'imagem': 'imagens_perguntas/lote3_caricatura_v05_p03.png'}],
 'Sobremesas pelo mundo': [{'pergunta': 'Qual destas sobremesas costuma levar biscoitos embebidos em café e '
                                        'mascarpone?',
                            'alternativas': ['Pudim', 'Cheesecake', 'Tiramisù'],
                            'correta': 2,
                            'imagem': 'imagens_perguntas/lote3_caricatura_v06_p01.png'},
                           {'pergunta': 'Qual destas sobremesas é uma torta cuja base do recheio costuma ser '
                                        'queijo cremoso?',
                            'alternativas': ['Cheesecake', 'Mousse de chocolate', 'Pudim'],
                            'correta': 0,
                            'imagem': 'imagens_perguntas/lote3_caricatura_v06_p02.png'},
                           {'pergunta': 'Qual destas sobremesas francesas tem uma camada de açúcar '
                                        'caramelizado sobre um creme?',
                            'alternativas': ['Brownie', 'Crème brûlée', 'Sorvete'],
                            'correta': 1,
                            'imagem': 'imagens_perguntas/lote3_caricatura_v06_p03.png'}],
 'Cereais e grãos': [{'pergunta': 'Qual destes cereais produz grãos em uma espiga com sabugo?',
                      'alternativas': ['Arroz', 'Milho', 'Trigo'],
                      'correta': 1,
                      'imagem': 'imagens_perguntas/lote3_caricatura_v07_p01.png'},
                     {'pergunta': 'Qual destes cereais é muito usado para produzir farinha de pão?',
                      'alternativas': ['Trigo', 'Arroz', 'Aveia'],
                      'correta': 0,
                      'imagem': 'imagens_perguntas/lote3_caricatura_v07_p02.png'},
                     {'pergunta': 'Qual destes cereais é cultivado em muitas áreas alagadas?',
                      'alternativas': ['Milho', 'Trigo', 'Arroz'],
                      'correta': 2,
                      'imagem': 'imagens_perguntas/lote3_caricatura_v07_p03.png'}],
 'Cogumelos e suas formas': [{'pergunta': 'Qual destes cogumelos costuma ser vendido com pequenos chapéus '
                                          'reunidos em cachos?',
                              'alternativas': ['Champignon', 'Shiitake', 'Shimeji'],
                              'correta': 2,
                              'imagem': 'imagens_perguntas/lote3_caricatura_v08_p01.png'},
                             {'pergunta': 'Qual destes nomes costuma designar o cogumelo branco de chapéu '
                                          'arredondado?',
                              'alternativas': ['Champignon', 'Shiitake', 'Shimeji'],
                              'correta': 0,
                              'imagem': 'imagens_perguntas/lote3_caricatura_v08_p02.png'},
                             {'pergunta': 'Qual destes cogumelos costuma ter chapéu largo e marrom?',
                              'alternativas': ['Shimeji branco', 'Shiitake', 'Champignon branco'],
                              'correta': 1,
                              'imagem': 'imagens_perguntas/lote3_caricatura_v08_p03.png'}],
 'Lendas': [{'pergunta': 'Segundo o folclore brasileiro, qual personagem tem uma perna só e usa gorro '
                         'vermelho?',
             'alternativas': ['Saci', 'Curupira', 'Iara'],
             'correta': 0,
             'imagem': 'imagens_perguntas/lote3_caricatura_v09_p01.png'},
            {'pergunta': 'Qual personagem do folclore brasileiro é descrito como uma serpente de fogo?',
             'alternativas': ['Boto', 'Boitatá', 'Lobisomem'],
             'correta': 1,
             'imagem': 'imagens_perguntas/lote3_caricatura_v09_p02.png'},
            {'pergunta': 'Qual figura das lendas brasileiras é conhecida como uma sereia dos rios?',
             'alternativas': ['Cuca', 'Iara', 'Vitória-régia'],
             'correta': 1,
             'imagem': 'imagens_perguntas/lote3_caricatura_v09_p03.png'}],
 'História bíblica': [{'pergunta': 'Segundo a narrativa bíblica, quem construiu uma arca para o dilúvio?',
                       'alternativas': ['Noé', 'Moisés', 'Davi'],
                       'correta': 0,
                       'imagem': 'imagens_perguntas/lote3_caricatura_v10_p01.png'},
                      {'pergunta': 'Segundo o livro bíblico de Jonas, quem foi engolido por um grande peixe?',
                       'alternativas': ['Davi', 'Jonas', 'José'],
                       'correta': 1,
                       'imagem': 'imagens_perguntas/lote3_caricatura_v10_p02.png'},
                      {'pergunta': 'Segundo a narrativa bíblica, quem foi colocado na cova dos leões?',
                       'alternativas': ['Daniel', 'Salomão', 'Moisés'],
                       'correta': 0,
                       'imagem': 'imagens_perguntas/lote3_caricatura_v10_p03.png'}],
 'Por que o céu é azul?': [{'pergunta': 'A cor azul do céu está relacionada principalmente à dispersão da...',
                            'alternativas': ['Luz solar', 'Água do mar', 'Luz da Lua'],
                            'correta': 0},
                           {'pergunta': 'Qual componente ajuda a espalhar a luz solar na atmosfera?',
                            'alternativas': ['A crosta terrestre', 'As moléculas do ar', 'Os continentes'],
                            'correta': 1},
                           {'pergunta': 'Qual cor costuma se destacar no céu ao amanhecer ou ao entardecer?',
                            'alternativas': ['Verde fluorescente', 'Preto sólido', 'Avermelhada'],
                            'correta': 2}],
 'Como se formam as nuvens?': [{'pergunta': 'As nuvens se formam quando o vapor de água...',
                                'alternativas': ['Vira areia', 'Se condensa', 'Desaparece'],
                                'correta': 1},
                               {'pergunta': 'Qual processo transforma água líquida em vapor?',
                                'alternativas': ['Evaporação', 'Congelamento', 'Trituração'],
                                'correta': 0},
                               {'pergunta': 'As nuvens são compostas principalmente por gotículas de água '
                                            'e...',
                                'alternativas': ['Grãos de sal', 'Pedras', 'Cristais de gelo'],
                                'correta': 2}],
 'Por que os trovões fazem barulho?': [{'pergunta': 'Qual fenômeno aquece rapidamente o ar e provoca o '
                                                    'trovão?',
                                        'alternativas': ['Raio', 'Arco-íris', 'Geada'],
                                        'correta': 0},
                                       {'pergunta': 'Por que normalmente vemos o relâmpago antes de ouvir o '
                                                    'trovão?',
                                        'alternativas': ['O som é mais rápido',
                                                         'A luz é mais rápida',
                                                         'A luz está mais perto'],
                                        'correta': 1},
                                       {'pergunta': 'O trovão é percebido principalmente por qual sentido?',
                                        'alternativas': ['Paladar', 'Olfato', 'Audição'],
                                        'correta': 2}],
 'Como nasce um arco-íris?': [{'pergunta': 'O arco-íris pode se formar quando a luz solar atravessa...',
                               'alternativas': ['Pedras', 'Gotículas de água', 'Folhas secas'],
                               'correta': 1},
                              {'pergunta': 'Qual cor aparece na borda externa de um arco-íris primário?',
                               'alternativas': ['Vermelho', 'Violeta', 'Azul'],
                               'correta': 0},
                              {'pergunta': 'Qual fenômeno separa a luz branca em diferentes cores?',
                               'alternativas': ['Magnetização', 'Evaporação', 'Dispersão da luz'],
                               'correta': 2}],
 'Por que o mar tem ondas?': [{'pergunta': 'Qual é a principal causa de muitas ondas na superfície do mar?',
                               'alternativas': ['Vento', 'Peixes', 'Areia'],
                               'correta': 0},
                              {'pergunta': 'O que as ondas transportam principalmente através da água?',
                               'alternativas': ['Continentes', 'Energia', 'Sal em sacos'],
                               'correta': 1},
                              {'pergunta': 'Quando uma onda se quebra perto da praia, ela costuma formar...',
                               'alternativas': ['Neve', 'Lava', 'Espuma'],
                               'correta': 2}],
 'Como funcionam as marés?': [{'pergunta': 'Qual astro tem papel fundamental na formação das marés '
                                           'terrestres?',
                               'alternativas': ['Marte', 'Lua', 'Saturno'],
                               'correta': 1},
                              {'pergunta': 'Como se chama o período em que o nível do mar está mais elevado '
                                           'no ciclo da maré?',
                               'alternativas': ['Maré alta', 'Maré seca permanente', 'Maré congelada'],
                               'correta': 0},
                              {'pergunta': 'Além da Lua, qual astro também influencia as marés?',
                               'alternativas': ['Júpiter', 'Netuno', 'Sol'],
                               'correta': 2}],
 'Como os rios chegam ao mar?': [{'pergunta': 'Como se chama o local onde um rio deságua?',
                                  'alternativas': ['Foz', 'Nascente', 'Margem'],
                                  'correta': 0},
                                 {'pergunta': 'Como se chama o lugar onde um rio começa?',
                                  'alternativas': ['Foz', 'Nascente', 'Delta'],
                                  'correta': 1},
                                 {'pergunta': 'Um rio que deságua em outro rio é chamado de...',
                                  'alternativas': ['Vulcão', 'Iceberg', 'Afluente'],
                                  'correta': 2}],
 'Por que alguns lagos são salgados?': [{'pergunta': 'Qual processo pode concentrar os sais de um lago?',
                                         'alternativas': ['Congelamento do Sol',
                                                          'Evaporação da água',
                                                          'Crescimento de árvores'],
                                         'correta': 1},
                                        {'pergunta': 'Os sais podem chegar aos lagos principalmente pela '
                                                     'água que dissolve...',
                                         'alternativas': ['Minerais das rochas',
                                                          'Luz das estrelas',
                                                          'Som dos animais'],
                                         'correta': 0},
                                        {'pergunta': 'Qual destes locais é conhecido por sua elevada '
                                                     'salinidade?',
                                         'alternativas': ['Lagoa de água da chuva',
                                                          'Piscina de água doce',
                                                          'Mar Morto'],
                                         'correta': 2}],
 'Como se formam as dunas?': [{'pergunta': 'Qual agente movimenta a areia e ajuda a formar muitas dunas?',
                               'alternativas': ['Vento', 'Luz', 'Magnetismo'],
                               'correta': 0},
                              {'pergunta': 'As dunas são formadas principalmente pelo acúmulo de...',
                               'alternativas': ['Folhas', 'Areia', 'Gelo'],
                               'correta': 1},
                              {'pergunta': 'Qual destes ambientes pode apresentar dunas?',
                               'alternativas': ['Fundo de uma geladeira',
                                                'Interior de uma caverna inundada',
                                                'Deserto'],
                               'correta': 2}],
 'Como os fósseis são preservados?': [{'pergunta': 'Fósseis são restos ou vestígios de seres vivos '
                                                   'preservados do...',
                                       'alternativas': ['Futuro', 'Passado', 'Espaço exterior apenas'],
                                       'correta': 1},
                                      {'pergunta': 'Qual material pode preservar insetos antigos em seu '
                                                   'interior?',
                                       'alternativas': ['Âmbar', 'Aço', 'Plástico moderno'],
                                       'correta': 0},
                                      {'pergunta': 'Qual destas marcas pode ser um fóssil de atividade de um '
                                                   'animal?',
                                       'alternativas': ['Uma pintura recente',
                                                        'Uma fotografia digital',
                                                        'Uma pegada preservada'],
                                       'correta': 2}],
 'A história do papel': [{'pergunta': 'Qual material vegetal é muito usado na fabricação de papel?',
                          'alternativas': ['Celulose', 'Borracha', 'Resina de pinho apenas'],
                          'correta': 0},
                         {'pergunta': 'Em qual país surgiu a tradição de fabricação de papel associada a Cai '
                                      'Lun?',
                          'alternativas': ['Brasil', 'China', 'Austrália'],
                          'correta': 1},
                         {'pergunta': 'Qual destes materiais era usado no Egito antigo para escrever?',
                          'alternativas': ['Náilon', 'Polietileno', 'Papiro'],
                          'correta': 2}],
 'Como o vidro é produzido?': [{'pergunta': 'Qual matéria-prima é muito usada para fabricar vidro comum?',
                                'alternativas': ['Farinha', 'Areia rica em sílica', 'Algodão'],
                                'correta': 1},
                               {'pergunta': 'Para produzir vidro, a mistura de matérias-primas precisa '
                                            'ser...',
                                'alternativas': ['Aquecida a altas temperaturas',
                                                 'Congelada',
                                                 'Molhada com suco'],
                                'correta': 0},
                               {'pergunta': 'Qual propriedade do vidro permite enxergar através de muitos '
                                            'objetos feitos dele?',
                                'alternativas': ['Magnetismo', 'Elasticidade elevada', 'Transparência'],
                                'correta': 2}],
 'De onde vem a borracha?': [{'pergunta': 'A borracha natural é obtida a partir do...',
                              'alternativas': ['Látex', 'Sal', 'Carvão'],
                              'correta': 0},
                             {'pergunta': 'Qual árvore é conhecida pela produção de látex para borracha?',
                              'alternativas': ['Coqueiro', 'Seringueira', 'Mangueira'],
                              'correta': 1},
                             {'pergunta': 'Além da natural, existe borracha produzida industrialmente '
                                          'chamada de...',
                              'alternativas': ['Mineral pura', 'Cristalina', 'Sintética'],
                              'correta': 2}],
 'Como o plástico é fabricado?': [{'pergunta': 'Os plásticos são formados principalmente por cadeias de '
                                               'moléculas chamadas de...',
                                   'alternativas': ['Rochas', 'Polímeros', 'Cristais de gelo'],
                                   'correta': 1},
                                  {'pergunta': 'Qual destas fontes fornece matéria-prima para muitos '
                                               'plásticos convencionais?',
                                   'alternativas': ['Petróleo', 'Água do mar apenas', 'Areia apenas'],
                                   'correta': 0},
                                  {'pergunta': 'Qual processo pode dar nova utilização a certos resíduos '
                                               'plásticos?',
                                   'alternativas': ['Fotossíntese', 'Vulcanismo', 'Reciclagem'],
                                   'correta': 2}],
 'A história das moedas': [{'pergunta': 'Qual material é tradicionalmente usado para fabricar muitas moedas?',
                            'alternativas': ['Metal', 'Papelão', 'Vidro'],
                            'correta': 0},
                           {'pergunta': 'Qual nome designa uma troca de bens sem uso de dinheiro?',
                            'alternativas': ['Inflação', 'Escambo', 'Depósito'],
                            'correta': 1},
                           {'pergunta': 'Como se chama o estudo e a coleção de moedas e medalhas?',
                            'alternativas': ['Botânica', 'Astronomia', 'Numismática'],
                            'correta': 2}],
 'Como surgiram os calendários?': [{'pergunta': 'Um calendário lunar se baseia principalmente nos ciclos '
                                                'da...',
                                    'alternativas': ['Terra sólida', 'Lua', 'Maré do rio'],
                                    'correta': 1},
                                   {'pergunta': 'Qual calendário é amplamente usado hoje em muitos países?',
                                    'alternativas': ['Gregoriano',
                                                     'Calendário do oceano',
                                                     'Calendário do vento'],
                                    'correta': 0},
                                   {'pergunta': 'No calendário gregoriano, um ano bissexto tem quantos dias?',
                                    'alternativas': ['364', '365', '366'],
                                    'correta': 2}],
 'Por que existem fusos horários?': [{'pergunta': 'Os fusos horários estão relacionados à...',
                                      'alternativas': ['Rotação da Terra',
                                                       'Forma das nuvens',
                                                       'Temperatura do mar'],
                                      'correta': 0},
                                     {'pergunta': 'Qual meridiano é referência para a longitude zero?',
                                      'alternativas': ['Trópico de Câncer', 'Greenwich', 'Equador'],
                                      'correta': 1},
                                     {'pergunta': 'Em geral, ao viajar para leste, o horário local tende '
                                                  'a...',
                                      'alternativas': ['Parar', 'Atrasar sempre', 'Avançar'],
                                      'correta': 2}],
 'Como os mapas representam a Terra?': [{'pergunta': 'Qual elemento mostra a relação entre a distância no '
                                                     'mapa e no terreno?',
                                         'alternativas': ['Título', 'Escala', 'Moldura'],
                                         'correta': 1},
                                        {'pergunta': 'Qual elemento explica os símbolos usados em um mapa?',
                                         'alternativas': ['Legenda', 'Capa', 'Rodapé'],
                                         'correta': 0},
                                        {'pergunta': 'Como se chama a representação da superfície terrestre '
                                                     'em um plano?',
                                         'alternativas': ['Fermentação',
                                                          'Condensação',
                                                          'Projeção cartográfica'],
                                         'correta': 2}],
 'Como os códigos de barras funcionam?': [{'pergunta': 'Um código de barras representa informações por meio '
                                                       'de...',
                                           'alternativas': ['Barras e espaços', 'Perfumes', 'Sons musicais'],
                                           'correta': 0},
                                          {'pergunta': 'Qual equipamento costuma interpretar um código de '
                                                       'barras?',
                                           'alternativas': ['Termômetro', 'Leitor óptico', 'Bússola'],
                                           'correta': 1},
                                          {'pergunta': 'No comércio, um código de barras pode ajudar a...',
                                           'alternativas': ['Medir a pressão atmosférica',
                                                            'Prever chuvas',
                                                            'Identificar um produto'],
                                           'correta': 2}],
 'Por que algumas pontes têm cabos?': [{'pergunta': 'Os cabos de certas pontes ajudam a sustentar o...',
                                        'alternativas': ['Céu', 'Tabuleiro da ponte', 'Leito do rio'],
                                        'correta': 1},
                                       {'pergunta': 'Como é chamado o esforço que estica um cabo?',
                                        'alternativas': ['Tração', 'Congelamento', 'Evaporação'],
                                        'correta': 0},
                                       {'pergunta': 'Em uma ponte estaiada, os cabos se ligam ao tabuleiro e '
                                                    'a...',
                                        'alternativas': ['Nuvens', 'Barcos', 'Torres ou mastros'],
                                        'correta': 2}]}

LEGENDAS = {'Calçados e suas diferenças': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'Calçados e suas diferenças: você acerta as três perguntas? Conte sua '
                               'pontuação nos comentários!\n'
                               '#Calcados #Tenis #Scarpin #Botas',
 'Bolsas e malas': 'CAPA_SEGUNDOS=2\n'
                   '\n'
                   'Bolsas e malas: você acerta as três perguntas? Conte sua pontuação nos comentários!\n'
                   '#Bolsas #Mochila #MalaDeViagem #Pochete',
 'Relógios e formas de marcar o tempo': 'CAPA_SEGUNDOS=2\n'
                                        '\n'
                                        'Relógios e formas de marcar o tempo: você acerta as três perguntas? '
                                        'Conte sua pontuação nos comentários!\n'
                                        '#Relogios #Ampulheta #Cronometro #RelogioDeSol',
 'Tipos de embarcações': 'CAPA_SEGUNDOS=2\n'
                         '\n'
                         'Tipos de embarcações: você acerta as três perguntas? Conte sua pontuação nos '
                         'comentários!\n'
                         '#Embarcacoes #Veleiro #NavioCargueiro #Submarino',
 'Construções e moradias': 'CAPA_SEGUNDOS=2\n'
                           '\n'
                           'Construções e moradias: você acerta as três perguntas? Conte sua pontuação nos '
                           'comentários!\n'
                           '#Moradias #Iglu #Barraca #Palafita',
 'Sobremesas pelo mundo': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Sobremesas pelo mundo: você acerta as três perguntas? Conte sua pontuação nos '
                          'comentários!\n'
                          '#Sobremesas #Tiramisu #Cheesecake #CremeBrulee',
 'Cereais e grãos': 'CAPA_SEGUNDOS=2\n'
                    '\n'
                    'Cereais e grãos: você acerta as três perguntas? Conte sua pontuação nos comentários!\n'
                    '#Cereais #Milho #Trigo #Arroz',
 'Cogumelos e suas formas': 'CAPA_SEGUNDOS=2\n'
                            '\n'
                            'Cogumelos e suas formas: você acerta as três perguntas? Conte sua pontuação nos '
                            'comentários!\n'
                            '#Cogumelos #Champignon #Shiitake #Shimeji',
 'Lendas': 'CAPA_SEGUNDOS=2\n'
           '\n'
           'Lendas: você acerta as três perguntas? Conte sua pontuação nos comentários!\n'
           '#LendasBrasileiras #Saci #Boitata #Iara',
 'História bíblica': 'CAPA_SEGUNDOS=2\n'
                     '\n'
                     'História bíblica: você acerta as três perguntas? Conte sua pontuação nos comentários!\n'
                     '#HistoriaBiblica #Noe #Jonas #Daniel',
 'Por que o céu é azul?': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Por que o céu é azul?: você acerta as três perguntas? Conte sua pontuação nos '
                          'comentários!\n'
                          '#CeuAzul #LuzSolar #Atmosfera #DispersaoDaLuz',
 'Como se formam as nuvens?': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Como se formam as nuvens?: você acerta as três perguntas? Conte sua pontuação '
                              'nos comentários!\n'
                              '#Nuvens #Condensacao #Evaporacao #CicloDaAgua',
 'Por que os trovões fazem barulho?': 'CAPA_SEGUNDOS=2\n'
                                      '\n'
                                      'Por que os trovões fazem barulho?: você acerta as três perguntas? '
                                      'Conte sua pontuação nos comentários!\n'
                                      '#Trovao #Raios #Relampago #Som',
 'Como nasce um arco-íris?': 'CAPA_SEGUNDOS=2\n'
                             '\n'
                             'Como nasce um arco-íris?: você acerta as três perguntas? Conte sua pontuação '
                             'nos comentários!\n'
                             '#ArcoIris #LuzBranca #Cores #GoticulasDeAgua',
 'Por que o mar tem ondas?': 'CAPA_SEGUNDOS=2\n'
                             '\n'
                             'Por que o mar tem ondas?: você acerta as três perguntas? Conte sua pontuação '
                             'nos comentários!\n'
                             '#OndasDoMar #Vento #Energia #Praia',
 'Como funcionam as marés?': 'CAPA_SEGUNDOS=2\n'
                             '\n'
                             'Como funcionam as marés?: você acerta as três perguntas? Conte sua pontuação '
                             'nos comentários!\n'
                             '#Mares #Lua #MareAlta #Sol',
 'Como os rios chegam ao mar?': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Como os rios chegam ao mar?: você acerta as três perguntas? Conte sua '
                                'pontuação nos comentários!\n'
                                '#Rios #Foz #Nascente #Afluentes',
 'Por que alguns lagos são salgados?': 'CAPA_SEGUNDOS=2\n'
                                       '\n'
                                       'Por que alguns lagos são salgados?: você acerta as três perguntas? '
                                       'Conte sua pontuação nos comentários!\n'
                                       '#LagosSalgados #Salinidade #Evaporacao #MarMorto',
 'Como se formam as dunas?': 'CAPA_SEGUNDOS=2\n'
                             '\n'
                             'Como se formam as dunas?: você acerta as três perguntas? Conte sua pontuação '
                             'nos comentários!\n'
                             '#Dunas #Areia #Vento #Desertos',
 'Como os fósseis são preservados?': 'CAPA_SEGUNDOS=2\n'
                                     '\n'
                                     'Como os fósseis são preservados?: você acerta as três perguntas? Conte '
                                     'sua pontuação nos comentários!\n'
                                     '#Fosseis #Ambar #Paleontologia #PegadasFossilizadas',
 'A história do papel': 'CAPA_SEGUNDOS=2\n'
                        '\n'
                        'A história do papel: você acerta as três perguntas? Conte sua pontuação nos '
                        'comentários!\n'
                        '#Papel #Celulose #ChinaAntiga #Papiro',
 'Como o vidro é produzido?': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Como o vidro é produzido?: você acerta as três perguntas? Conte sua pontuação '
                              'nos comentários!\n'
                              '#Vidro #Silica #Areia #FabricacaoDoVidro',
 'De onde vem a borracha?': 'CAPA_SEGUNDOS=2\n'
                            '\n'
                            'De onde vem a borracha?: você acerta as três perguntas? Conte sua pontuação nos '
                            'comentários!\n'
                            '#Borracha #Latex #Seringueira #BorrachaSintetica',
 'Como o plástico é fabricado?': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Como o plástico é fabricado?: você acerta as três perguntas? Conte sua '
                                 'pontuação nos comentários!\n'
                                 '#Plasticos #Polimeros #Petroleo #ReciclagemDoPlastico',
 'A história das moedas': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'A história das moedas: você acerta as três perguntas? Conte sua pontuação nos '
                          'comentários!\n'
                          '#Moedas #Escambo #Numismatica #HistoriaDoDinheiro',
 'Como surgiram os calendários?': 'CAPA_SEGUNDOS=2\n'
                                  '\n'
                                  'Como surgiram os calendários?: você acerta as três perguntas? Conte sua '
                                  'pontuação nos comentários!\n'
                                  '#Calendarios #CalendarioLunar #Gregoriano #AnoBissexto',
 'Por que existem fusos horários?': 'CAPA_SEGUNDOS=2\n'
                                    '\n'
                                    'Por que existem fusos horários?: você acerta as três perguntas? Conte '
                                    'sua pontuação nos comentários!\n'
                                    '#FusosHorarios #RotacaoDaTerra #Greenwich #HorarioLocal',
 'Como os mapas representam a Terra?': 'CAPA_SEGUNDOS=2\n'
                                       '\n'
                                       'Como os mapas representam a Terra?: você acerta as três perguntas? '
                                       'Conte sua pontuação nos comentários!\n'
                                       '#Mapas #Escala #Legenda #Cartografia',
 'Como os códigos de barras funcionam?': 'CAPA_SEGUNDOS=2\n'
                                         '\n'
                                         'Como os códigos de barras funcionam?: você acerta as três '
                                         'perguntas? Conte sua pontuação nos comentários!\n'
                                         '#CodigoDeBarras #LeitorOptico #Produtos #Tecnologia',
 'Por que algumas pontes têm cabos?': 'CAPA_SEGUNDOS=2\n'
                                      '\n'
                                      'Por que algumas pontes têm cabos?: você acerta as três perguntas? '
                                      'Conte sua pontuação nos comentários!\n'
                                      '#Pontes #Cabos #Tracao #PontesEstaiadas'}
