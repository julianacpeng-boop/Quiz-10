# Quiz-10: 30 temas, 90 perguntas e 30 caricaturas distintas.
# As imagens mostram as alternativas A, B e C da esquerda para a direita.
# PNG 1536 x 1024 pixels, proporção 3:2.
# correta: 0 = A, 1 = B, 2 = C.

QUIZZES = {'Comidas e pratos brasileiros': [{'pergunta': 'Qual prato costuma ser preparado com feijão preto?',
                                   'alternativas': ['Feijoada', 'Moqueca', 'Acarajé'],
                                   'correta': 0,
                                   'imagem': 'imagens_perguntas/lote_comparativo_v01_p01.png'},
                                  {'pergunta': 'Qual destes salgados costuma ter formato de gota e recheio '
                                               'de frango?',
                                   'alternativas': ['Pastel', 'Coxinha', 'Pão de queijo'],
                                   'correta': 1,
                                   'imagem': 'imagens_perguntas/lote_comparativo_v01_p02.png'},
                                  {'pergunta': 'Qual destas comidas é feita com goma de mandioca?',
                                   'alternativas': ['Pizza', 'Hambúrguer', 'Tapioca'],
                                   'correta': 2,
                                   'imagem': 'imagens_perguntas/lote_comparativo_v01_p03.png'}],
 'Animais terrestres': [{'pergunta': 'Qual destes animais possui uma tromba?',
                         'alternativas': ['Girafa', 'Elefante', 'Leão'],
                         'correta': 1,
                         'imagem': 'imagens_perguntas/lote_comparativo_v02_p01.png'},
                        {'pergunta': 'Qual destes animais é um roedor?',
                         'alternativas': ['Gato', 'Cachorro', 'Rato'],
                         'correta': 2,
                         'imagem': 'imagens_perguntas/lote_comparativo_v02_p02.png'},
                        {'pergunta': 'Qual destes animais possui listras pretas e brancas?',
                         'alternativas': ['Zebra', 'Rinoceronte', 'Hipopótamo'],
                         'correta': 0,
                         'imagem': 'imagens_perguntas/lote_comparativo_v02_p03.png'}],
 'Placas de trânsito': [{'pergunta': 'Qual destas placas exige parada obrigatória?',
                         'alternativas': ['PARE', 'Dê a preferência', 'Sentido proibido'],
                         'correta': 0,
                         'imagem': 'imagens_perguntas/lote_comparativo_v03_p01.png'},
                        {'pergunta': 'Qual destas placas proíbe estacionar?',
                         'alternativas': ['Velocidade máxima de 30 km/h',
                                          'Proibido estacionar',
                                          'Sentido proibido'],
                         'correta': 1,
                         'imagem': 'imagens_perguntas/lote_comparativo_v03_p02.png'},
                        {'pergunta': 'Qual destas placas alerta para uma curva acentuada à direita?',
                         'alternativas': ['Curva acentuada à esquerda',
                                          'Cruzamento de vias',
                                          'Curva acentuada à direita'],
                         'correta': 2,
                         'imagem': 'imagens_perguntas/lote_comparativo_v03_p03.png'}],
 'Animais marinhos': [{'pergunta': 'Qual destes animais é um mamífero?',
                       'alternativas': ['Polvo', 'Tubarão', 'Golfinho'],
                       'correta': 2,
                       'imagem': 'imagens_perguntas/lote_comparativo_v04_p01.png'},
                      {'pergunta': 'Qual destes animais tem oito braços?',
                       'alternativas': ['Polvo', 'Cavalo-marinho', 'Estrela-do-mar'],
                       'correta': 0,
                       'imagem': 'imagens_perguntas/lote_comparativo_v04_p02.png'},
                      {'pergunta': 'Qual destes animais marinhos possui uma carapaça?',
                       'alternativas': ['Água-viva', 'Tartaruga-marinha', 'Lula'],
                       'correta': 1,
                       'imagem': 'imagens_perguntas/lote_comparativo_v04_p03.png'}],
 'Frutas': [{'pergunta': 'Qual destas frutas costuma ter a casca amarela quando madura?',
             'alternativas': ['Morango', 'Uva roxa', 'Banana'],
             'correta': 2,
             'imagem': 'imagens_perguntas/lote_comparativo_v05_p01.png'},
            {'pergunta': 'Qual destas frutas tem uma coroa de folhas?',
             'alternativas': ['Abacaxi', 'Laranja', 'Maçã'],
             'correta': 0,
             'imagem': 'imagens_perguntas/lote_comparativo_v05_p02.png'},
            {'pergunta': 'Qual destas frutas tem um grande caroço no centro?',
             'alternativas': ['Limão', 'Manga', 'Uva'],
             'correta': 1,
             'imagem': 'imagens_perguntas/lote_comparativo_v05_p03.png'}],
 'Objetos da cozinha': [{'pergunta': 'Qual destes objetos é usado para escorrer macarrão?',
                         'alternativas': ['Panela', 'Escorredor', 'Frigideira'],
                         'correta': 1,
                         'imagem': 'imagens_perguntas/lote_comparativo_v06_p01.png'},
                        {'pergunta': 'Qual destes objetos é usado para ralar queijo?',
                         'alternativas': ['Ralador', 'Concha', 'Espátula'],
                         'correta': 0,
                         'imagem': 'imagens_perguntas/lote_comparativo_v06_p02.png'},
                        {'pergunta': 'Qual destes objetos serve para abrir garrafas com rolha?',
                         'alternativas': ['Batedor de arame', 'Pegador', 'Saca-rolhas'],
                         'correta': 2,
                         'imagem': 'imagens_perguntas/lote_comparativo_v06_p03.png'}],
 'Meios de transporte': [{'pergunta': 'Qual destes veículos se desloca sobre trilhos?',
                          'alternativas': ['Ônibus', 'Carro', 'Trem'],
                          'correta': 2,
                          'imagem': 'imagens_perguntas/lote_comparativo_v07_p01.png'},
                         {'pergunta': 'Qual destes transportes pode navegar em rios?',
                          'alternativas': ['Barco', 'Avião', 'Bicicleta'],
                          'correta': 0,
                          'imagem': 'imagens_perguntas/lote_comparativo_v07_p02.png'},
                         {'pergunta': 'Qual destes transportes costuma ser movido por pedais?',
                          'alternativas': ['Helicóptero', 'Bicicleta', 'Motocicleta'],
                          'correta': 1,
                          'imagem': 'imagens_perguntas/lote_comparativo_v07_p03.png'}],
 'Instrumentos musicais': [{'pergunta': 'Qual destes instrumentos possui seis cordas no modelo mais comum?',
                            'alternativas': ['Violão', 'Flauta', 'Tambor'],
                            'correta': 0,
                            'imagem': 'imagens_perguntas/lote_comparativo_v08_p01.png'},
                           {'pergunta': 'Qual destes instrumentos é tocado soprando?',
                            'alternativas': ['Piano', 'Flauta', 'Violino'],
                            'correta': 1,
                            'imagem': 'imagens_perguntas/lote_comparativo_v08_p02.png'},
                           {'pergunta': 'Qual destes instrumentos é de percussão?',
                            'alternativas': ['Saxofone', 'Harpa', 'Tambor'],
                            'correta': 2,
                            'imagem': 'imagens_perguntas/lote_comparativo_v08_p03.png'}],
 'Ferramentas e suas funções': [{'pergunta': 'Qual destas ferramentas é usada para apertar parafusos de '
                                             'fenda?',
                                 'alternativas': ['Martelo', 'Chave de fenda', 'Serrote'],
                                 'correta': 1,
                                 'imagem': 'imagens_perguntas/lote_comparativo_v09_p01.png'},
                                {'pergunta': 'Qual destas ferramentas é usada para bater pregos?',
                                 'alternativas': ['Martelo', 'Alicate', 'Trena'],
                                 'correta': 0,
                                 'imagem': 'imagens_perguntas/lote_comparativo_v09_p02.png'},
                                {'pergunta': 'Qual destas ferramentas é usada para medir comprimentos?',
                                 'alternativas': ['Serrote', 'Chave inglesa', 'Trena'],
                                 'correta': 2,
                                 'imagem': 'imagens_perguntas/lote_comparativo_v09_p03.png'}],
 'Esportes e seus equipamentos': [{'pergunta': 'Qual destes objetos é usado no tênis?',
                                   'alternativas': ['Raquete de tênis',
                                                    'Bola de futebol',
                                                    'Bola de basquete'],
                                   'correta': 0,
                                   'imagem': 'imagens_perguntas/lote_comparativo_v10_p01.png'},
                                  {'pergunta': 'Qual destes equipamentos é usado no surfe?',
                                   'alternativas': ['Patins', 'Prancha de surfe', 'Bicicleta'],
                                   'correta': 1,
                                   'imagem': 'imagens_perguntas/lote_comparativo_v10_p02.png'},
                                  {'pergunta': 'Qual destes objetos é usado para rebater a bola no beisebol?',
                                   'alternativas': ['Peteca', 'Raquete de tênis de mesa', 'Taco de beisebol'],
                                   'correta': 2,
                                   'imagem': 'imagens_perguntas/lote_comparativo_v10_p03.png'}],
 'Temperos e sabores': [{'pergunta': 'Qual tempero é obtido da casca de uma árvore?',
                         'alternativas': ['Canela', 'Sal', 'Pimenta-do-reino'],
                         'correta': 0},
                        {'pergunta': 'Qual destes ingredientes é tradicionalmente salgado?',
                         'alternativas': ['Açúcar', 'Sal', 'Mel'],
                         'correta': 1},
                        {'pergunta': 'Qual destes temperos vem de um bulbo?',
                         'alternativas': ['Canela', 'Cravo', 'Alho'],
                         'correta': 2}],
 'Doces típicos brasileiros': [{'pergunta': 'Qual doce costuma levar leite condensado e chocolate?',
                                'alternativas': ['Paçoca', 'Brigadeiro', 'Quindim'],
                                'correta': 1},
                               {'pergunta': 'Qual doce é tradicionalmente feito com amendoim?',
                                'alternativas': ['Paçoca', 'Goiabada', 'Cocada'],
                                'correta': 0},
                               {'pergunta': 'Qual doce é feito principalmente com coco?',
                                'alternativas': ['Pé de moleque', 'Goiabada', 'Cocada'],
                                'correta': 2}],
 'Verduras e legumes': [{'pergunta': 'Qual destes alimentos é uma raiz?',
                         'alternativas': ['Alface', 'Repolho', 'Cenoura'],
                         'correta': 2},
                        {'pergunta': 'Qual destes alimentos é consumido principalmente pelas folhas?',
                         'alternativas': ['Alface', 'Batata', 'Beterraba'],
                         'correta': 0},
                        {'pergunta': 'Qual destes legumes é conhecido por seu sabor picante?',
                         'alternativas': ['Abóbora', 'Rabanete', 'Chuchu'],
                         'correta': 1}],
 'Aves e suas características': [{'pergunta': 'Qual destas aves não voa?',
                                  'alternativas': ['Avestruz', 'Andorinha', 'Águia'],
                                  'correta': 0},
                                 {'pergunta': 'Qual ave é conhecida por imitar sons e palavras?',
                                  'alternativas': ['Pinguim', 'Papagaio', 'Avestruz'],
                                  'correta': 1},
                                 {'pergunta': 'Qual destas aves costuma ter hábitos noturnos?',
                                  'alternativas': ['Galinha', 'Pato', 'Coruja'],
                                  'correta': 2}],
 'Insetos e suas curiosidades': [{'pergunta': 'Quantas pernas possui um inseto adulto típico?',
                                  'alternativas': ['Quatro', 'Seis', 'Oito'],
                                  'correta': 1},
                                 {'pergunta': 'Qual inseto produz mel?',
                                  'alternativas': ['Abelha', 'Borboleta', 'Grilo'],
                                  'correta': 0},
                                 {'pergunta': 'Qual inseto passa por uma fase de lagarta?',
                                  'alternativas': ['Formiga', 'Mosca', 'Borboleta'],
                                  'correta': 2}],
 'Répteis': [{'pergunta': 'Qual destes animais é um réptil?',
              'alternativas': ['Sapo', 'Salamandra', 'Jacaré'],
              'correta': 2},
             {'pergunta': 'Qual réptil possui um casco?',
              'alternativas': ['Tartaruga', 'Cobra', 'Lagartixa'],
              'correta': 0},
             {'pergunta': 'Qual destes répteis não tem pernas?',
              'alternativas': ['Iguana', 'Cobra', 'Crocodilo'],
              'correta': 1}],
 'Animais de água doce': [{'pergunta': 'Qual destes animais é um peixe de água doce?',
                           'alternativas': ['Piranha', 'Golfinho-nariz-de-garrafa', 'Tubarão-branco'],
                           'correta': 0},
                          {'pergunta': 'Qual grande mamífero semiaquático vive em rios e lagos africanos?',
                           'alternativas': ['Leão', 'Hipopótamo', 'Girafa'],
                           'correta': 1},
                          {'pergunta': 'Qual destes animais é conhecido por construir represas?',
                           'alternativas': ['Lontra', 'Capivara', 'Castor'],
                           'correta': 2}],
 'Filhotes e seus nomes': [{'pergunta': 'Como se chama o filhote do cavalo?',
                            'alternativas': ['Bezerro', 'Potro', 'Cordeiro'],
                            'correta': 1},
                           {'pergunta': 'Como se chama o filhote da vaca?',
                            'alternativas': ['Bezerro', 'Potro', 'Leitão'],
                            'correta': 0},
                           {'pergunta': 'Como se chama o filhote da ovelha?',
                            'alternativas': ['Pintinho', 'Cabrito', 'Cordeiro'],
                            'correta': 2}],
 'Sons dos animais': [{'pergunta': 'Qual animal costuma relinchar?',
                       'alternativas': ['Cavalo', 'Gato', 'Galinha'],
                       'correta': 0},
                      {'pergunta': 'Qual animal costuma miar?',
                       'alternativas': ['Pato', 'Gato', 'Vaca'],
                       'correta': 1},
                      {'pergunta': 'Qual animal costuma mugir?',
                       'alternativas': ['Cachorro', 'Ovelha', 'Vaca'],
                       'correta': 2}],
 'Bandeiras dos países': [{'pergunta': 'Qual bandeira tem uma folha de bordo vermelha?',
                           'alternativas': ['Japão', 'Canadá', 'Brasil'],
                           'correta': 1},
                          {'pergunta': 'Qual bandeira tem um círculo vermelho sobre fundo branco?',
                           'alternativas': ['Japão', 'Itália', 'Argentina'],
                           'correta': 0},
                          {'pergunta': 'Qual bandeira tem um losango amarelo sobre fundo verde?',
                           'alternativas': ['França', 'Chile', 'Brasil'],
                           'correta': 2}],
 'Capitais brasileiras': [{'pergunta': 'Qual é a capital da Paraíba?',
                           'alternativas': ['Recife', 'Natal', 'João Pessoa'],
                           'correta': 2},
                          {'pergunta': 'Qual é a capital do Ceará?',
                           'alternativas': ['Fortaleza', 'Teresina', 'Maceió'],
                           'correta': 0},
                          {'pergunta': 'Qual é a capital do Amazonas?',
                           'alternativas': ['Belém', 'Manaus', 'Porto Velho'],
                           'correta': 1}],
 'Pontos turísticos do Brasil': [{'pergunta': 'Em qual cidade fica o Cristo Redentor?',
                                  'alternativas': ['Rio de Janeiro', 'Salvador', 'Curitiba'],
                                  'correta': 0},
                                 {'pergunta': 'Em qual estado ficam as Cataratas do Iguaçu no lado '
                                              'brasileiro?',
                                  'alternativas': ['Bahia', 'Paraná', 'Ceará'],
                                  'correta': 1},
                                 {'pergunta': 'Em qual cidade fica o Pelourinho?',
                                  'alternativas': ['Brasília', 'Recife', 'Salvador'],
                                  'correta': 2}],
 'Planetas do Sistema Solar': [{'pergunta': 'Qual planeta é conhecido como planeta vermelho?',
                                'alternativas': ['Vênus', 'Marte', 'Netuno'],
                                'correta': 1},
                               {'pergunta': 'Qual planeta é famoso por seus anéis?',
                                'alternativas': ['Saturno', 'Mercúrio', 'Terra'],
                                'correta': 0},
                               {'pergunta': 'Qual é o maior planeta do Sistema Solar?',
                                'alternativas': ['Marte', 'Urano', 'Júpiter'],
                                'correta': 2}],
 'Fenômenos da natureza': [{'pergunta': 'Qual fenômeno é uma descarga elétrica na atmosfera?',
                            'alternativas': ['Arco-íris', 'Nevoeiro', 'Raio'],
                            'correta': 2},
                           {'pergunta': 'Qual fenômeno forma um arco de cores no céu?',
                            'alternativas': ['Arco-íris', 'Terremoto', 'Geada'],
                            'correta': 0},
                           {'pergunta': 'Qual fenômeno envolve tremores na crosta terrestre?',
                            'alternativas': ['Orvalho', 'Terremoto', 'Granizo'],
                            'correta': 1}],
 'Pedras preciosas': [{'pergunta': 'Qual pedra preciosa é uma variedade vermelha do coríndon?',
                       'alternativas': ['Rubi', 'Esmeralda', 'Diamante'],
                       'correta': 0},
                      {'pergunta': 'Qual pedra preciosa é uma variedade verde do berilo?',
                       'alternativas': ['Rubi', 'Esmeralda', 'Safira'],
                       'correta': 1},
                      {'pergunta': 'Qual destas pedras é formada por carbono cristalizado?',
                       'alternativas': ['Ametista', 'Topázio', 'Diamante'],
                       'correta': 2}],
 'Materiais e reciclagem': [{'pergunta': 'Na coleta seletiva brasileira, qual cor identifica papel?',
                             'alternativas': ['Verde', 'Azul', 'Amarelo'],
                             'correta': 1},
                            {'pergunta': 'Qual destes materiais pode ser reciclado como metal?',
                             'alternativas': ['Lata de alumínio', 'Casca de banana', 'Guardanapo usado'],
                             'correta': 0},
                            {'pergunta': 'Qual cor identifica vidro na coleta seletiva brasileira?',
                             'alternativas': ['Vermelho', 'Azul', 'Verde'],
                             'correta': 2}],
 'Profissões e seus instrumentos': [{'pergunta': 'Qual profissional costuma usar um estetoscópio?',
                                     'alternativas': ['Médico', 'Marceneiro', 'Fotógrafo'],
                                     'correta': 0},
                                    {'pergunta': 'Qual profissional trabalha com câmera para registrar '
                                                 'imagens?',
                                     'alternativas': ['Padeiro', 'Fotógrafo', 'Encanador'],
                                     'correta': 1},
                                    {'pergunta': 'Qual profissional costuma usar tesoura para cortar '
                                                 'cabelos?',
                                     'alternativas': ['Dentista', 'Eletricista', 'Cabeleireiro'],
                                     'correta': 2}],
 'Eletrodomésticos e suas funções': [{'pergunta': 'Qual aparelho mantém alimentos refrigerados?',
                                      'alternativas': ['Torradeira', 'Geladeira', 'Liquidificador'],
                                      'correta': 1},
                                     {'pergunta': 'Qual aparelho mistura e tritura ingredientes?',
                                      'alternativas': ['Liquidificador', 'Ferro de passar', 'Ventilador'],
                                      'correta': 0},
                                     {'pergunta': 'Qual aparelho é usado para passar roupas?',
                                      'alternativas': ['Micro-ondas', 'Aspirador de pó', 'Ferro de passar'],
                                      'correta': 2}],
 'Brincadeiras tradicionais': [{'pergunta': 'Qual brincadeira usa casas numeradas desenhadas no chão?',
                                'alternativas': ['Esconde-esconde', 'Pega-pega', 'Amarelinha'],
                                'correta': 2},
                               {'pergunta': 'Qual brincadeira consiste em procurar participantes escondidos?',
                                'alternativas': ['Esconde-esconde', 'Cabo de guerra', 'Queimada'],
                                'correta': 0},
                               {'pergunta': 'Qual brincadeira envolve duas equipes puxando uma corda?',
                                'alternativas': ['Peteca', 'Cabo de guerra', 'Pular corda'],
                                'correta': 1}],
 'Roupas e acessórios de diferentes épocas': [{'pergunta': 'Qual acessório era usado para consultar as horas '
                                                           'antes dos relógios de pulso?',
                                               'alternativas': ['Relógio de bolso', 'Monóculo', 'Cartola'],
                                               'correta': 0},
                                              {'pergunta': 'Qual acessório de um só vidro era colocado '
                                                           'diante de um olho?',
                                               'alternativas': ['Gravata', 'Monóculo', 'Broche'],
                                               'correta': 1},
                                              {'pergunta': 'Qual chapéu tem copa alta e formato cilíndrico?',
                                               'alternativas': ['Boné', 'Boina', 'Cartola'],
                                               'correta': 2}]}

LEGENDAS = {'Comidas e pratos brasileiros': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Comidas e pratos brasileiros: você consegue acertar as três? Conte sua '
                                 'pontuação nos comentários!\n'
                                 '#ComidaBrasileira #Feijoada #Coxinha #Tapioca',
 'Animais terrestres': 'CAPA_SEGUNDOS=2\n'
                       '\n'
                       'Animais terrestres: você consegue acertar as três? Conte sua pontuação nos '
                       'comentários!\n'
                       '#AnimaisTerrestres #Elefante #Roedores #Zebra',
 'Placas de trânsito': 'CAPA_SEGUNDOS=2\n'
                       '\n'
                       'Placas de trânsito: você consegue acertar as três? Conte sua pontuação nos '
                       'comentários!\n'
                       '#PlacasDeTransito #Sinalizacao #TransitoBrasileiro #EducacaoNoTransito',
 'Animais marinhos': 'CAPA_SEGUNDOS=2\n'
                     '\n'
                     'Animais marinhos: você consegue acertar as três? Conte sua pontuação nos comentários!\n'
                     '#AnimaisMarinhos #Golfinho #Polvo #TartarugaMarinha',
 'Frutas': 'CAPA_SEGUNDOS=2\n'
           '\n'
           'Frutas: você consegue acertar as três? Conte sua pontuação nos comentários!\n'
           '#Frutas #Banana #Abacaxi #Manga',
 'Objetos da cozinha': 'CAPA_SEGUNDOS=2\n'
                       '\n'
                       'Objetos da cozinha: você consegue acertar as três? Conte sua pontuação nos '
                       'comentários!\n'
                       '#Cozinha #Utensilios #Ralador #SacaRolhas',
 'Meios de transporte': 'CAPA_SEGUNDOS=2\n'
                        '\n'
                        'Meios de transporte: você consegue acertar as três? Conte sua pontuação nos '
                        'comentários!\n'
                        '#Transportes #Trem #Barco #Bicicleta',
 'Instrumentos musicais': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Instrumentos musicais: você consegue acertar as três? Conte sua pontuação nos '
                          'comentários!\n'
                          '#InstrumentosMusicais #Violao #Flauta #Percussao',
 'Ferramentas e suas funções': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'Ferramentas e suas funções: você consegue acertar as três? Conte sua '
                               'pontuação nos comentários!\n'
                               '#Ferramentas #ChaveDeFenda #Martelo #Trena',
 'Esportes e seus equipamentos': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Esportes e seus equipamentos: você consegue acertar as três? Conte sua '
                                 'pontuação nos comentários!\n'
                                 '#Esportes #Tenis #Surfe #Beisebol',
 'Temperos e sabores': 'CAPA_SEGUNDOS=2\n'
                       '\n'
                       'Temperos e sabores: você consegue acertar as três? Conte sua pontuação nos '
                       'comentários!\n'
                       '#Temperos #Canela #Alho #Sabores',
 'Doces típicos brasileiros': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Doces típicos brasileiros: você consegue acertar as três? Conte sua pontuação '
                              'nos comentários!\n'
                              '#DocesBrasileiros #Brigadeiro #Pacoca #Cocada',
 'Verduras e legumes': 'CAPA_SEGUNDOS=2\n'
                       '\n'
                       'Verduras e legumes: você consegue acertar as três? Conte sua pontuação nos '
                       'comentários!\n'
                       '#Verduras #Legumes #Cenoura #Rabanete',
 'Aves e suas características': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Aves e suas características: você consegue acertar as três? Conte sua '
                                'pontuação nos comentários!\n'
                                '#Aves #Avestruz #Papagaio #Coruja',
 'Insetos e suas curiosidades': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Insetos e suas curiosidades: você consegue acertar as três? Conte sua '
                                'pontuação nos comentários!\n'
                                '#Insetos #Abelhas #Borboletas #Entomologia',
 'Répteis': 'CAPA_SEGUNDOS=2\n'
            '\n'
            'Répteis: você consegue acertar as três? Conte sua pontuação nos comentários!\n'
            '#Repteis #Jacare #Tartaruga #Cobras',
 'Animais de água doce': 'CAPA_SEGUNDOS=2\n'
                         '\n'
                         'Animais de água doce: você consegue acertar as três? Conte sua pontuação nos '
                         'comentários!\n'
                         '#AguaDoce #Piranha #Hipopotamo #Castor',
 'Filhotes e seus nomes': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Filhotes e seus nomes: você consegue acertar as três? Conte sua pontuação nos '
                          'comentários!\n'
                          '#Filhotes #Potro #Bezerro #Cordeiro',
 'Sons dos animais': 'CAPA_SEGUNDOS=2\n'
                     '\n'
                     'Sons dos animais: você consegue acertar as três? Conte sua pontuação nos comentários!\n'
                     '#SonsDosAnimais #Relincho #Miado #Mugido',
 'Bandeiras dos países': 'CAPA_SEGUNDOS=2\n'
                         '\n'
                         'Bandeiras dos países: você consegue acertar as três? Conte sua pontuação nos '
                         'comentários!\n'
                         '#Bandeiras #Canada #Japao #Brasil',
 'Capitais brasileiras': 'CAPA_SEGUNDOS=2\n'
                         '\n'
                         'Capitais brasileiras: você consegue acertar as três? Conte sua pontuação nos '
                         'comentários!\n'
                         '#CapitaisBrasileiras #JoaoPessoa #Fortaleza #Manaus',
 'Pontos turísticos do Brasil': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Pontos turísticos do Brasil: você consegue acertar as três? Conte sua '
                                'pontuação nos comentários!\n'
                                '#TurismoNoBrasil #CristoRedentor #CataratasDoIguacu #Pelourinho',
 'Planetas do Sistema Solar': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Planetas do Sistema Solar: você consegue acertar as três? Conte sua pontuação '
                              'nos comentários!\n'
                              '#SistemaSolar #Marte #Saturno #Jupiter',
 'Fenômenos da natureza': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Fenômenos da natureza: você consegue acertar as três? Conte sua pontuação nos '
                          'comentários!\n'
                          '#FenomenosNaturais #Raios #ArcoIris #Terremotos',
 'Pedras preciosas': 'CAPA_SEGUNDOS=2\n'
                     '\n'
                     'Pedras preciosas: você consegue acertar as três? Conte sua pontuação nos comentários!\n'
                     '#PedrasPreciosas #Rubi #Esmeralda #Diamante',
 'Materiais e reciclagem': 'CAPA_SEGUNDOS=2\n'
                           '\n'
                           'Materiais e reciclagem: você consegue acertar as três? Conte sua pontuação nos '
                           'comentários!\n'
                           '#Reciclagem #ColetaSeletiva #Aluminio #Vidro',
 'Profissões e seus instrumentos': 'CAPA_SEGUNDOS=2\n'
                                   '\n'
                                   'Profissões e seus instrumentos: você consegue acertar as três? Conte sua '
                                   'pontuação nos comentários!\n'
                                   '#Profissoes #Medicina #Fotografia #Cabeleireiro',
 'Eletrodomésticos e suas funções': 'CAPA_SEGUNDOS=2\n'
                                    '\n'
                                    'Eletrodomésticos e suas funções: você consegue acertar as três? Conte '
                                    'sua pontuação nos comentários!\n'
                                    '#Eletrodomesticos #Geladeira #Liquidificador #FerroDePassar',
 'Brincadeiras tradicionais': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Brincadeiras tradicionais: você consegue acertar as três? Conte sua pontuação '
                              'nos comentários!\n'
                              '#Brincadeiras #Amarelinha #EscondeEsconde #CaboDeGuerra',
 'Roupas e acessórios de diferentes épocas': 'CAPA_SEGUNDOS=2\n'
                                             '\n'
                                             'Roupas e acessórios de diferentes épocas: você consegue '
                                             'acertar as três? Conte sua pontuação nos comentários!\n'
                                             '#ModaAntiga #RelogioDeBolso #Monoculo #Cartola'}
