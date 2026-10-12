# Juh Quiz — rodada 9: 30 vídeos, 3 perguntas cada.
# Caricaturas nos 10 primeiros vídeos; 4 hashtags específicas por legenda.

QUIZZES = {'Português: você escreve certo?': [{'pergunta': "Qual é o plural correto de 'cidadão'?",
                                     'alternativas': ['Cidadões', 'Cidadãos', 'Cidadães'],
                                     'correta': 1,
                                     'imagem': 'imagens_perguntas/rodada9_v01_p01.png'},
                                    {'pergunta': "A palavra 'feliz' é um exemplo de...",
                                     'alternativas': ['Verbo', 'Substantivo', 'Adjetivo'],
                                     'correta': 2,
                                     'imagem': 'imagens_perguntas/rodada9_v01_p02.png'},
                                    {'pergunta': "Complete: 'Não fui ___ estava chovendo'.",
                                     'alternativas': ['Porque', 'Por que', 'Porquê'],
                                     'correta': 0,
                                     'imagem': 'imagens_perguntas/rodada9_v01_p03.png'}],
 'História: três viagens ao passado': [{'pergunta': 'Qual civilização antiga construiu o Coliseu?',
                                        'alternativas': ['Romana', 'Grega', 'Egípcia'],
                                        'correta': 0,
                                        'imagem': 'imagens_perguntas/rodada9_v02_p01.png'},
                                       {'pergunta': 'Em que ano aconteceu a Independência do '
                                                    'Brasil?',
                                        'alternativas': ['1889', '1822', '1500'],
                                        'correta': 1,
                                        'imagem': 'imagens_perguntas/rodada9_v02_p02.png'},
                                       {'pergunta': 'A Lei Áurea, de 1888, aboliu o quê no Brasil?',
                                        'alternativas': ['A monarquia',
                                                         'Os impostos',
                                                         'A escravidão'],
                                        'correta': 2,
                                        'imagem': 'imagens_perguntas/rodada9_v02_p03.png'}],
 'Geografia: oceano, deserto e Equador': [{'pergunta': 'Qual é o maior oceano do planeta?',
                                           'alternativas': ['Atlântico 🌊',
                                                            'Pacífico 🌊',
                                                            'Índico 🌊'],
                                           'correta': 1,
                                           'imagem': 'imagens_perguntas/rodada9_v03_p01.png'},
                                          {'pergunta': 'Em qual continente fica o deserto do '
                                                       'Saara?',
                                           'alternativas': ['Ásia', 'Europa', 'África'],
                                           'correta': 2,
                                           'imagem': 'imagens_perguntas/rodada9_v03_p02.png'},
                                          {'pergunta': 'Qual linha divide a Terra em hemisférios '
                                                       'Norte e Sul?',
                                           'alternativas': ['Equador',
                                                            'Greenwich',
                                                            'Trópico de Capricórnio'],
                                           'correta': 0,
                                           'imagem': 'imagens_perguntas/rodada9_v03_p03.png'}],
 'Ciências: vida, plantas e água': [{'pergunta': 'Qual é a unidade básica dos seres vivos?',
                                     'alternativas': ['Tecido', 'Órgão', 'Célula'],
                                     'correta': 2,
                                     'imagem': 'imagens_perguntas/rodada9_v04_p01.png'},
                                    {'pergunta': 'Qual parte da planta absorve água do solo?',
                                     'alternativas': ['Raiz 🌱', 'Folha 🍃', 'Flor 🌸'],
                                     'correta': 0,
                                     'imagem': 'imagens_perguntas/rodada9_v04_p02.png'},
                                    {'pergunta': 'Qual processo transforma água líquida em vapor?',
                                     'alternativas': ['Fusão', 'Evaporação', 'Condensação'],
                                     'correta': 1,
                                     'imagem': 'imagens_perguntas/rodada9_v04_p03.png'}],
 'Física: som, inércia e força': [{'pergunta': 'Em qual lugar o som não se propaga?',
                                   'alternativas': ['Debaixo da água', 'No ar', 'No vácuo'],
                                   'correta': 2,
                                   'imagem': 'imagens_perguntas/rodada9_v05_p01.png'},
                                  {'pergunta': 'Qual conceito explica seu corpo seguir adiante '
                                               'quando o ônibus freia?',
                                   'alternativas': ['Inércia', 'Magnetismo', 'Refração'],
                                   'correta': 0,
                                   'imagem': 'imagens_perguntas/rodada9_v05_p02.png'},
                                  {'pergunta': 'Qual unidade do SI mede força?',
                                   'alternativas': ['Watt', 'Newton', 'Joule'],
                                   'correta': 1,
                                   'imagem': 'imagens_perguntas/rodada9_v05_p03.png'}],
 'Química: água, ouro e gelo': [{'pergunta': 'Qual fórmula representa a água?',
                                 'alternativas': ['CO₂', 'H₂O', 'NaCl'],
                                 'correta': 1,
                                 'imagem': 'imagens_perguntas/rodada9_v06_p01.png'},
                                {'pergunta': 'Qual símbolo químico representa o ouro?',
                                 'alternativas': ['Au', 'Ag', 'Fe'],
                                 'correta': 0,
                                 'imagem': 'imagens_perguntas/rodada9_v06_p02.png'},
                                {'pergunta': 'Gelo e água líquida são a mesma substância?',
                                 'alternativas': ['Não, são elementos diferentes',
                                                  'Só quando têm sal',
                                                  'Sim, em estados diferentes'],
                                 'correta': 2,
                                 'imagem': 'imagens_perguntas/rodada9_v06_p03.png'}],
 'Escândalos famosos: o que aconteceu?': [{'pergunta': 'Em qual país aconteceu o escândalo '
                                                       'Watergate?',
                                           'alternativas': ['Estados Unidos',
                                                            'França',
                                                            'Argentina'],
                                           'correta': 0,
                                           'imagem': 'imagens_perguntas/rodada9_v07_p01.png'},
                                          {'pergunta': 'O Dieselgate envolveu fraude em testes de '
                                                       'quê?',
                                           'alternativas': ['Resistência dos pneus',
                                                            'Emissões de veículos',
                                                            'Velocidade máxima'],
                                           'correta': 1,
                                           'imagem': 'imagens_perguntas/rodada9_v07_p02.png'},
                                          {'pergunta': 'Qual irregularidade marcou o escândalo da '
                                                       'Enron?',
                                           'alternativas': ['Troca de uniformes',
                                                            'Cópia de receitas',
                                                            'Fraude contábil'],
                                           'correta': 2,
                                           'imagem': 'imagens_perguntas/rodada9_v07_p03.png'}],
 'Homem-Aranha: curiosidades dos quadrinhos': [{'pergunta': 'Em qual revista o Homem-Aranha '
                                                            'estreou em 1962?',
                                                'alternativas': ['Amazing Fantasy 15',
                                                                 'Amazing Spider-Man 1',
                                                                 'Marvel Comics 1'],
                                                'correta': 0,
                                                'imagem': 'imagens_perguntas/rodada9_v08_p01.png'},
                                               {'pergunta': 'Qual é o nome do Homem-Aranha '
                                                            'original?',
                                                'alternativas': ['Tony Stark',
                                                                 'Peter Parker',
                                                                 'Bruce Banner'],
                                                'correta': 1,
                                                'imagem': 'imagens_perguntas/rodada9_v08_p02.png'},
                                               {'pergunta': 'Nos quadrinhos clássicos, Peter lança '
                                                            'teias usando...',
                                                'alternativas': ['Magia',
                                                                 'O cabelo',
                                                                 'Lançadores mecânicos'],
                                                'correta': 2,
                                                'imagem': 'imagens_perguntas/rodada9_v08_p03.png'}],
 'Boi da Cara Preta: cantiga e folclore': [{'pergunta': "'Boi da Cara Preta' é conhecido "
                                                        'principalmente como...',
                                            'alternativas': ['Uma receita',
                                                             'Uma cantiga de ninar',
                                                             'Uma regra de futebol'],
                                            'correta': 1,
                                            'imagem': 'imagens_perguntas/rodada9_v09_p01.png'},
                                           {'pergunta': 'Qual parte do boi é descrita como preta '
                                                        'na cantiga?',
                                            'alternativas': ['O rabo', 'A pata', 'A cara'],
                                            'correta': 2,
                                            'imagem': 'imagens_perguntas/rodada9_v09_p02.png'},
                                           {'pergunta': 'Como cantigas populares costumam passar '
                                                        'entre gerações?',
                                            'alternativas': ['Pela tradição oral',
                                                             'Somente por leis',
                                                             'Por um livro único'],
                                            'correta': 0,
                                            'imagem': 'imagens_perguntas/rodada9_v09_p03.png'}],
 'A primeira televisão: os primeiros passos': [{'pergunta': 'Quem demonstrou imagens de televisão '
                                                            'em Londres em 1926?',
                                                'alternativas': ['Thomas Edison',
                                                                 'John Logie Baird',
                                                                 'Alexander Graham Bell'],
                                                'correta': 1,
                                                'imagem': 'imagens_perguntas/rodada9_v10_p01.png'},
                                               {'pergunta': 'O sistema demonstrado por Baird em '
                                                            '1926 era...',
                                                'alternativas': ['Mecânico',
                                                                 'Via satélite',
                                                                 'Por streaming'],
                                                'correta': 0,
                                                'imagem': 'imagens_perguntas/rodada9_v10_p02.png'},
                                               {'pergunta': 'Qual emissora inaugurou a televisão '
                                                            'no Brasil em 1950?',
                                                'alternativas': ['TV Globo', 'Band', 'TV Tupi'],
                                                'correta': 2,
                                                'imagem': 'imagens_perguntas/rodada9_v10_p03.png'}],
 'Origami: um papel, muitas formas': [{'pergunta': 'Qual é a técnica central do origami '
                                                   'tradicional?',
                                       'alternativas': ['Dobrar papel',
                                                        'Fundir vidro',
                                                        'Entalhar pedra'],
                                       'correta': 0},
                                      {'pergunta': 'Qual ave aparece no tradicional tsuru de '
                                                   'origami?',
                                       'alternativas': ['Pinguim', 'Grou', 'Papagaio'],
                                       'correta': 1},
                                      {'pergunta': 'Qual material é usado no origami?',
                                       'alternativas': ['Barro', 'Tecido', 'Papel'],
                                       'correta': 2}],
 'Braille: leitura pelo toque': [{'pergunta': 'Quantos pontos tem a cela braille tradicional?',
                                  'alternativas': ['Quatro', 'Seis', 'Oito'],
                                  'correta': 1},
                                 {'pergunta': 'Na leitura braille, os pontos são percebidos '
                                              'principalmente pelo...',
                                  'alternativas': ['Olfato', 'Paladar', 'Tato'],
                                  'correta': 2},
                                 {'pergunta': 'O braille é principalmente um sistema de...',
                                  'alternativas': ['Leitura e escrita',
                                                   'Navegação por satélite',
                                                   'Pintura com luz'],
                                  'correta': 0}],
 'Libras: uma língua visual': [{'pergunta': 'O que significa Libras?',
                                'alternativas': ['Livro Brasileiro de Arte',
                                                 'Lista Brasileira de Símbolos',
                                                 'Língua Brasileira de Sinais'],
                                'correta': 2},
                               {'pergunta': 'As expressões faciais em Libras podem ter função...',
                                'alternativas': ['Gramatical', 'Só decorativa', 'Apenas musical'],
                                'correta': 0},
                               {'pergunta': 'As línguas de sinais são iguais em todos os países?',
                                'alternativas': ['Sim, sempre',
                                                 'Não, existem diferentes línguas',
                                                 'Só mudam de cor'],
                                'correta': 1}],
 'Fotografia analógica: antes do digital': [{'pergunta': 'O que registra a imagem em uma câmera '
                                                         'analógica tradicional?',
                                             'alternativas': ['Um filme fotográfico',
                                                              'Uma fita de tecido',
                                                              'Um espelho solto'],
                                             'correta': 0},
                                            {'pergunta': 'A abertura da lente controla '
                                                         'principalmente a entrada de...',
                                             'alternativas': ['Som', 'Luz', 'Água'],
                                             'correta': 1},
                                            {'pergunta': 'Qual processo transforma o filme exposto '
                                                         'em imagens visíveis?',
                                             'alternativas': ['Congelamento',
                                                              'Polimento',
                                                              'Revelação'],
                                             'correta': 2}],
 'Cerâmica: do barro ao forno': [{'pergunta': 'Qual material é muito usado para modelar cerâmica?',
                                  'alternativas': ['Gelo', 'Argila', 'Borracha'],
                                  'correta': 1},
                                 {'pergunta': 'A queima das peças de cerâmica costuma acontecer em '
                                              'um...',
                                  'alternativas': ['Forno', 'Congelador', 'Liquidificador'],
                                  'correta': 0},
                                 {'pergunta': 'Qual equipamento gira a peça durante a modelagem?',
                                  'alternativas': ['Telescópio',
                                                   'Microscópio',
                                                   'Torno de cerâmica'],
                                  'correta': 2}],
 'Vitrais: desenhos feitos de luz': [{'pergunta': 'Um vitral é formado principalmente por peças '
                                                  'de...',
                                      'alternativas': ['Madeira', 'Papel', 'Vidro'],
                                      'correta': 2},
                                     {'pergunta': 'O que atravessa o vitral e destaca suas cores?',
                                      'alternativas': ['Luz', 'Som', 'Vento'],
                                      'correta': 0},
                                     {'pergunta': 'Vitrais são muito usados em qual parte dos '
                                                  'edifícios?',
                                      'alternativas': ['Tubulações', 'Janelas', 'Fundações'],
                                      'correta': 1}],
 'Bordado: histórias em cada ponto': [{'pergunta': 'Qual instrumento conduz a linha no bordado '
                                                   'manual?',
                                       'alternativas': ['Agulha', 'Martelo', 'Alicate'],
                                       'correta': 0},
                                      {'pergunta': 'Qual peça ajuda a manter o tecido esticado?',
                                       'alternativas': ['Prendedor de cabelo',
                                                        'Bastidor',
                                                        'Colher'],
                                       'correta': 1},
                                      {'pergunta': 'Qual técnica faz pontos que lembram a letra X?',
                                       'alternativas': ['Crochê', 'Macramê', 'Ponto cruz'],
                                       'correta': 2}],
 'Perfumes: notas e famílias': [{'pergunta': 'Quais notas de um perfume costumam ser percebidas '
                                             'primeiro?',
                                 'alternativas': ['Notas de fundo',
                                                  'Notas de saída',
                                                  'Notas escondidas'],
                                 'correta': 1},
                                {'pergunta': 'A família floral reúne aromas associados a...',
                                 'alternativas': ['Pedras', 'Metais', 'Flores'],
                                 'correta': 2},
                                {'pergunta': 'Na perfumaria, a pirâmide olfativa organiza...',
                                 'alternativas': ['As notas do perfume',
                                                  'O preço da embalagem',
                                                  'A cor do frasco'],
                                 'correta': 0}],
 'Bolhas de sabão: beleza e ciência': [{'pergunta': 'A película de uma bolha de sabão envolve '
                                                    'principalmente...',
                                        'alternativas': ['Areia', 'Madeira', 'Ar'],
                                        'correta': 2},
                                       {'pergunta': 'A forma esférica ajuda a bolha a reduzir '
                                                    'sua...',
                                        'alternativas': ['Área de superfície',
                                                         'Quantidade de cores',
                                                         'Temperatura obrigatoriamente'],
                                        'correta': 0},
                                       {'pergunta': 'As cores da bolha aparecem por um fenômeno '
                                                    'chamado...',
                                        'alternativas': ['Gravidade',
                                                         'Interferência da luz',
                                                         'Magnetismo'],
                                        'correta': 1}],
 'Ilusões de óptica: seus olhos te enganam?': [{'pergunta': 'Numa ilusão de óptica, a percepção '
                                                            'pode diferir da...',
                                                'alternativas': ['Realidade física',
                                                                 'Temperatura do Sol',
                                                                 'Idade do papel'],
                                                'correta': 0},
                                               {'pergunta': 'Qual sentido está mais ligado às '
                                                            'ilusões de óptica?',
                                                'alternativas': ['Paladar', 'Visão', 'Olfato'],
                                                'correta': 1},
                                               {'pergunta': 'Quem interpreta as informações '
                                                            'recebidas pelos olhos?',
                                                'alternativas': ['As unhas',
                                                                 'Os cabelos',
                                                                 'O cérebro'],
                                                'correta': 2}],
 'Capoeira: roda, ritmo e movimento': [{'pergunta': 'Qual instrumento é um dos símbolos da '
                                                    'capoeira?',
                                        'alternativas': ['Violino', 'Berimbau', 'Trompete'],
                                        'correta': 1},
                                       {'pergunta': 'Como se chama a formação de pessoas em torno '
                                                    'do jogo?',
                                        'alternativas': ['Roda', 'Fila', 'Labirinto'],
                                        'correta': 0},
                                       {'pergunta': 'Qual é um movimento básico contínuo da '
                                                    'capoeira?',
                                        'alternativas': ['Saque', 'Drible', 'Ginga'],
                                        'correta': 2}],
 'Peteca: esporte na palma da mão': [{'pergunta': 'A peteca é tradicionalmente rebatida com...',
                                      'alternativas': ['Uma colher', 'O pé apenas', 'A mão'],
                                      'correta': 2},
                                     {'pergunta': 'O objeto chamado peteca costuma ter uma base '
                                                  'e...',
                                      'alternativas': ['Penas', 'Rodas', 'Engrenagens'],
                                      'correta': 0},
                                     {'pergunta': 'No esporte de quadra, os lados são separados '
                                                  'por uma...',
                                      'alternativas': ['Parede de concreto',
                                                       'Rede',
                                                       'Cerca elétrica'],
                                      'correta': 1}],
 'Curling: pedras deslizando no gelo': [{'pergunta': 'Em qual superfície é disputado o curling?',
                                         'alternativas': ['Gelo', 'Areia', 'Grama'],
                                         'correta': 0},
                                        {'pergunta': 'Os jogadores usam qual objeto para varrer à '
                                                     'frente da pedra?',
                                         'alternativas': ['Raquete', 'Escova', 'Corda'],
                                         'correta': 1},
                                        {'pergunta': 'As pedras de competição são feitas '
                                                     'principalmente de...',
                                         'alternativas': ['Papel', 'Borracha', 'Granito'],
                                         'correta': 2}],
 'Esgrima: toque, defesa e precisão': [{'pergunta': 'Qual destes é uma arma da esgrima esportiva?',
                                        'alternativas': ['Arco', 'Florete', 'Estilingue'],
                                        'correta': 1},
                                       {'pergunta': 'Qual equipamento protege o rosto do '
                                                    'esgrimista?',
                                        'alternativas': ['Boné', 'Óculos de sol', 'Máscara'],
                                        'correta': 2},
                                       {'pergunta': 'Como se chama a ação de bloquear o ataque '
                                                    'adversário?',
                                        'alternativas': ['Parada', 'Saque', 'Arremesso'],
                                        'correta': 0}],
 'Dominó: peças e combinações': [{'pergunta': 'Quantas peças tem um dominó tradicional duplo-seis?',
                                  'alternativas': ['21', '36', '28'],
                                  'correta': 2},
                                 {'pergunta': 'Cada peça do dominó é dividida em quantas metades?',
                                  'alternativas': ['Duas', 'Três', 'Quatro'],
                                  'correta': 0},
                                 {'pergunta': 'Num jogo comum, a peça encaixa quando os valores '
                                              'das pontas...',
                                  'alternativas': ['São sempre zero',
                                                   'São iguais',
                                                   'Somam sempre dez'],
                                  'correta': 1}],
 'Boliche: rumo ao strike': [{'pergunta': 'Quantos pinos há no boliche tradicional de dez pinos?',
                              'alternativas': ['Dez', 'Oito', 'Doze'],
                              'correta': 0},
                             {'pergunta': 'Derrubar todos os pinos na primeira bola é um...',
                              'alternativas': ['Spare', 'Strike', 'Tie-break'],
                              'correta': 1},
                             {'pergunta': 'Derrubar os pinos restantes com a segunda bola é um...',
                              'alternativas': ['Gol', 'Ace', 'Spare'],
                              'correta': 2}],
 'Cogumelos: um reino à parte': [{'pergunta': 'Os cogumelos pertencem ao reino dos...',
                                  'alternativas': ['Animais', 'Fungos', 'Minerais'],
                                  'correta': 1},
                                 {'pergunta': 'As estruturas filamentosas dos fungos são chamadas '
                                              'de...',
                                  'alternativas': ['Hifas', 'Nervuras', 'Escamas'],
                                  'correta': 0},
                                 {'pergunta': 'Muitos fungos se reproduzem espalhando...',
                                  'alternativas': ['Sementes', 'Ovos', 'Esporos'],
                                  'correta': 2}],
 'Liquens: uma parceria da natureza': [{'pergunta': 'Liquens associam um fungo a organismos que '
                                                    'fazem...',
                                        'alternativas': ['Fotossíntese', 'Cerâmica', 'Costura'],
                                        'correta': 0},
                                       {'pergunta': 'Liquens podem crescer sobre...',
                                        'alternativas': ['Somente água fervente',
                                                         'Rochas e troncos',
                                                         'Somente plástico novo'],
                                        'correta': 1},
                                       {'pergunta': 'A relação entre os parceiros de um líquen é '
                                                    'uma...',
                                        'alternativas': ['Competição esportiva',
                                                         'Liga metálica',
                                                         'Simbiose'],
                                        'correta': 2}],
 'Bonsai: pequenas árvores, grande arte': [{'pergunta': 'Bonsai é principalmente a arte de '
                                                        'cultivar...',
                                            'alternativas': ['Flores de plástico',
                                                             'Árvores em miniatura',
                                                             'Cogumelos gigantes'],
                                            'correta': 1},
                                           {'pergunta': 'Bonsai é o nome de uma única espécie de '
                                                        'árvore?',
                                            'alternativas': ['Sim, uma espécie só',
                                                             'Só no verão',
                                                             'Não, diferentes espécies podem ser '
                                                             'usadas'],
                                            'correta': 2},
                                           {'pergunta': 'Qual técnica ajuda a controlar o '
                                                        'crescimento do bonsai?',
                                            'alternativas': ['Poda',
                                                             'Congelamento',
                                                             'Pintura das folhas'],
                                            'correta': 0}],
 'Manguezais: entre a terra e o mar': [{'pergunta': 'Manguezais são comuns em regiões costeiras '
                                                    'influenciadas pelas...',
                                        'alternativas': ['Dunas apenas', 'Geleiras', 'Marés'],
                                        'correta': 2},
                                       {'pergunta': 'Quando água doce e salgada se misturam, a '
                                                    'água é chamada de...',
                                        'alternativas': ['Salobra',
                                                         'Destilada',
                                                         'Mineral sem sais'],
                                        'correta': 0},
                                       {'pergunta': 'Manguezais ajudam a abrigar filhotes de '
                                                    'muitas espécies de...',
                                        'alternativas': ['Animais terrestres apenas',
                                                         'Peixes e crustáceos',
                                                         'Dinossauros'],
                                        'correta': 1}]}

LEGENDAS = {'Português: você escreve certo?': 'CAPA_SEGUNDOS=2\n'
                                   '\n'
                                   'Cidadão, feliz e os porquês: três desafios de português para '
                                   'pegar quem responde no impulso! Quantos você acertou?\n'
                                   '\n'
                                   '#JuhQuiz #LinguaPortuguesa #Gramatica #Ortografia',
 'História: três viagens ao passado': 'CAPA_SEGUNDOS=2\n'
                                      '\n'
                                      'Do Coliseu à Independência e à Lei Áurea: será que você '
                                      'lembra desses marcos da história? Teste sua memória em três '
                                      'perguntas.\n'
                                      '\n'
                                      '#JuhQuiz #Historia #HistoriaDoBrasil #RomaAntiga',
 'Geografia: oceano, deserto e Equador': 'CAPA_SEGUNDOS=2\n'
                                         '\n'
                                         'Qual oceano é o maior? Onde fica o Saara? E que linha '
                                         'divide o planeta? Uma volta ao mundo em três perguntas '
                                         'de geografia!\n'
                                         '\n'
                                         '#JuhQuiz #Geografia #Oceanos #PlanetaTerra',
 'Ciências: vida, plantas e água': 'CAPA_SEGUNDOS=2\n'
                                   '\n'
                                   'Células, raízes e água virando vapor: a ciência está em tudo! '
                                   'Você consegue acertar essas três sem voltar à aula?\n'
                                   '\n'
                                   '#JuhQuiz #Ciencias #Biologia #CicloDaAgua',
 'Física: som, inércia e força': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Por que o som não viaja no vácuo? Por que você vai para a frente '
                                 'quando o ônibus freia? Descubra o quanto sabe de física!\n'
                                 '\n'
                                 '#JuhQuiz #Fisica #Inercia #Forca',
 'Química: água, ouro e gelo': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'H₂O, ouro e gelo: três perguntas de química que parecem fáceis, '
                               'mas pedem atenção! Qual delas quase te enganou?\n'
                               '\n'
                               '#JuhQuiz #Quimica #ElementosQuimicos #EstadosDaMateria',
 'Escândalos famosos: o que aconteceu?': 'CAPA_SEGUNDOS=2\n'
                                         '\n'
                                         'Watergate, Dieselgate e Enron: você sabe o que estava '
                                         'por trás desses escândalos famosos? Três casos '
                                         'históricos, três respostas.\n'
                                         '\n'
                                         '#JuhQuiz #Watergate #Dieselgate #Enron',
 'Homem-Aranha: curiosidades dos quadrinhos': 'CAPA_SEGUNDOS=2\n'
                                              '\n'
                                              'Antes dos filmes, já existiam a estreia no gibi e '
                                              'os lançadores de teia! Você conhece essas '
                                              'curiosidades do Homem-Aranha original?\n'
                                              '\n'
                                              '#JuhQuiz #HomemAranha #Marvel #Quadrinhos',
 'Boi da Cara Preta: cantiga e folclore': 'CAPA_SEGUNDOS=2\n'
                                          '\n'
                                          'Você cresceu ouvindo Boi da Cara Preta? Vamos revisitar '
                                          'a cantiga de ninar e a tradição oral do nosso folclore, '
                                          'sem inventar uma origem para ela.\n'
                                          '\n'
                                          '#JuhQuiz #BoiDaCaraPreta #FolcloreBrasileiro '
                                          '#CantigasDeNinar',
 'A primeira televisão: os primeiros passos': 'CAPA_SEGUNDOS=2\n'
                                              '\n'
                                              'A TV começou muito antes das telas fininhas! Do '
                                              'sistema mecânico de Baird à TV Tupi, teste o que '
                                              'sabe sobre os primeiros passos da televisão.\n'
                                              '\n'
                                              '#JuhQuiz #HistoriaDaTelevisao #JohnLogieBaird '
                                              '#TVTupi',
 'Origami: um papel, muitas formas': 'CAPA_SEGUNDOS=2\n'
                                     '\n'
                                     'Um papel pode virar uma ave! Você conhece as dobraduras e o '
                                     'tsuru do origami? Conte se já tentou fazer um.\n'
                                     '\n'
                                     '#JuhQuiz #Origami #Dobradura #ArteEmPapel',
 'Braille: leitura pelo toque': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Seis pontos podem abrir um mundo de leitura. Descubra o que sabe '
                                'sobre braille e a importância da leitura pelo toque.\n'
                                '\n'
                                '#JuhQuiz #Braille #LeituraTatil #Acessibilidade',
 'Libras: uma língua visual': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Libras tem gramática e expressões faciais que fazem parte da '
                              'língua! Você acerta essas três sobre comunicação visual?\n'
                              '\n'
                              '#JuhQuiz #Libras #LinguaDeSinais #ComunicacaoVisual',
 'Fotografia analógica: antes do digital': 'CAPA_SEGUNDOS=2\n'
                                           '\n'
                                           'Filme, luz e revelação: a fotografia analógica tem '
                                           'seus próprios segredos. Você lembra da época de '
                                           'esperar as fotos ficarem prontas?\n'
                                           '\n'
                                           '#JuhQuiz #FotografiaAnalogica #FilmeFotografico '
                                           '#Revelacao',
 'Cerâmica: do barro ao forno': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Argila nas mãos, torno girando e uma peça indo ao forno: quanto '
                                'você sabe sobre a arte da cerâmica?\n'
                                '\n'
                                '#JuhQuiz #Ceramica #Argila #ArteCeramica',
 'Vitrais: desenhos feitos de luz': 'CAPA_SEGUNDOS=2\n'
                                    '\n'
                                    'Quando a luz atravessa o vidro, as cores viram espetáculo! '
                                    'Três perguntas sobre vitrais para quem gosta de arte e '
                                    'arquitetura.\n'
                                    '\n'
                                    '#JuhQuiz #Vitrais #ArteEmVidro #Arquitetura',
 'Bordado: histórias em cada ponto': 'CAPA_SEGUNDOS=2\n'
                                     '\n'
                                     'Agulha, bastidor e ponto cruz: você reconhece os detalhes do '
                                     'bordado? Marque alguém que transforma linha em arte.\n'
                                     '\n'
                                     '#JuhQuiz #Bordado #PontoCruz #ArteTextil',
 'Perfumes: notas e famílias': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'Notas de saída e família floral: perfume também tem vocabulário! '
                               'Descubra se você conhece o que existe por trás dos aromas.\n'
                               '\n'
                               '#JuhQuiz #Perfumes #Perfumaria #NotasOlfativas',
 'Bolhas de sabão: beleza e ciência': 'CAPA_SEGUNDOS=2\n'
                                      '\n'
                                      'Por que as bolhas são redondas e cheias de cores? Até uma '
                                      'brincadeira de sabão esconde fenômenos da física!\n'
                                      '\n'
                                      '#JuhQuiz #BolhasDeSabao #TensaoSuperficial '
                                      '#InterferenciaDaLuz',
 'Ilusões de óptica: seus olhos te enganam?': 'CAPA_SEGUNDOS=2\n'
                                              '\n'
                                              'Nem tudo parece o que realmente é! Três perguntas '
                                              'sobre ilusões de óptica e o trabalho do cérebro ao '
                                              'interpretar imagens.\n'
                                              '\n'
                                              '#JuhQuiz #IlusaoDeOptica #PercepcaoVisual #Visao',
 'Capoeira: roda, ritmo e movimento': 'CAPA_SEGUNDOS=2\n'
                                      '\n'
                                      'Berimbau tocando, roda formada e ginga no corpo: você '
                                      'conhece esses elementos da capoeira?\n'
                                      '\n'
                                      '#JuhQuiz #Capoeira #Berimbau #Ginga',
 'Peteca: esporte na palma da mão': 'CAPA_SEGUNDOS=2\n'
                                    '\n'
                                    'Base, penas e uma boa batida com a mão! Você sabe o básico da '
                                    'peteca ou vai deixar essa cair?\n'
                                    '\n'
                                    '#JuhQuiz #Peteca #EsporteBrasileiro #JogoDePeteca',
 'Curling: pedras deslizando no gelo': 'CAPA_SEGUNDOS=2\n'
                                       '\n'
                                       'Pedras, gelo e escovas: o curling parece curioso, mas tem '
                                       'muita técnica! Você acerta essas três sobre o esporte?\n'
                                       '\n'
                                       '#JuhQuiz #Curling #EsportesDeInverno #EsporteNoGelo',
 'Esgrima: toque, defesa e precisão': 'CAPA_SEGUNDOS=2\n'
                                      '\n'
                                      'Florete, máscara e defesa: será que você reconhece os '
                                      'termos da esgrima? Entre nessa pista com três perguntas!\n'
                                      '\n'
                                      '#JuhQuiz #Esgrima #Florete #EsporteDeCombate',
 'Dominó: peças e combinações': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'O duplo-seis tem quantas peças? E como elas se encaixam? Veja se '
                                'seu conhecimento do dominó vai além da mesa de jogo!\n'
                                '\n'
                                '#JuhQuiz #Domino #DuploSeis #JogoDeDomino',
 'Boliche: rumo ao strike': 'CAPA_SEGUNDOS=2\n'
                            '\n'
                            'Dez pinos, duas tentativas e aquele strike perfeito! Você conhece a '
                            'diferença entre strike e spare no boliche?\n'
                            '\n'
                            '#JuhQuiz #Boliche #Strike #Spare',
 'Cogumelos: um reino à parte': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Cogumelo não é planta! Hifas e esporos entram nesse quiz sobre o '
                                'surpreendente reino dos fungos.\n'
                                '\n'
                                '#JuhQuiz #Cogumelos #Fungos #Micologia',
 'Liquens: uma parceria da natureza': 'CAPA_SEGUNDOS=2\n'
                                      '\n'
                                      'Parece uma mancha na pedra, mas pode ser uma parceria viva! '
                                      'Descubra os liquens e a simbiose por trás deles.\n'
                                      '\n'
                                      '#JuhQuiz #Liquens #Simbiose #Botanica',
 'Bonsai: pequenas árvores, grande arte': 'CAPA_SEGUNDOS=2\n'
                                          '\n'
                                          'Bonsai não é uma única espécie de árvore! Descubra o '
                                          'papel da poda e os cuidados por trás dessa arte em '
                                          'miniatura.\n'
                                          '\n'
                                          '#JuhQuiz #Bonsai #ArvoresEmMiniatura #ArteDoBonsai',
 'Manguezais: entre a terra e o mar': 'CAPA_SEGUNDOS=2\n'
                                      '\n'
                                      'Água salobra, marés e um berçário para peixes e crustáceos: '
                                      'você conhece a riqueza dos manguezais?\n'
                                      '\n'
                                      '#JuhQuiz #Manguezais #EcossistemasCosteiros #VidaNoMangue'}

FONTES = ['https://www.senate.gov/about/powers-procedures/investigations/watergate.htm',
 'https://www.epa.gov/enforcement/volkswagen-clean-air-act-civil-settlement',
 'https://www.sec.gov/enforcement-litigation/litigation-releases/lr-18582',
 'https://www.marvel.com/comics/issue/16926',
 'https://www.marvel.com/characters/spider-man-peter-parker/in-comics',
 'https://servicos.rolandia.pr.gov.br/educacao/wp-content/uploads/aulas_online/escolas/MARIA%20DO%20CARMO%20CAMPOS/EJA/2021/ETAPA1/26%C2%BAe27%C2%BAROT-EJA1.pdf',
 'https://blog.scienceandmediamuseum.org.uk/history-of-british-television-timeline/',
 'https://blog.scienceandmediamuseum.org.uk/john-logie-baird-double-8/',
 'https://bndigital.bn.gov.br/artigos/documento-da-semana-18-de-setembro-de-1950-inauguracao-da-tv-tupi/',
 'https://www.libras.ufsc.br/colecaoLetrasLibras/eixoFormacaoEspecifica/linguaBrasileiraDeSinaisI/scos/cap18717/1.html',
 'https://revista.ibc.gov.br/index.php/BC/article/view/862',
 'https://worldcurling.org/rules/',
 'https://origamiusa.org/classes/convention/2023/tsuru-cranes-colors',
 'https://www.fs.usda.gov/sites/default/files/fs_media/fs_document/Lichen-Atlas.pdf',
 'https://annex.exploratorium.edu/ronh/bubbles/bubble_colors.html']
