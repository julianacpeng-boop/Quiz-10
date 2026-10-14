# Quiz-10 — lote 2: 30 novos temas, 90 perguntas e 30 montagens realistas.
# As alternativas A/B/C aparecem da esquerda para a direita em cada imagem.
# PNG 1536 x 1024, proporção 3:2; imagens nos 10 primeiros vídeos.
# correta: 0 = A, 1 = B, 2 = C.

QUIZZES = {'Raças de cães': [{'pergunta': 'Qual destas raças é conhecida pela pelagem encaracolada?',
                    'alternativas': ['Labrador', 'Poodle', 'Bulldog'],
                    'correta': 1,
                    'imagem': 'imagens_perguntas/lote2_realista_v01_p01.png'},
                   {'pergunta': 'Qual destas raças tem corpo alongado e pernas curtas?',
                    'alternativas': ['Dachshund', 'Dálmata', 'Beagle'],
                    'correta': 0,
                    'imagem': 'imagens_perguntas/lote2_realista_v01_p02.png'},
                   {'pergunta': 'Qual destas raças é de porte muito pequeno?',
                    'alternativas': ['Husky siberiano', 'Boxer', 'Chihuahua'],
                    'correta': 2,
                    'imagem': 'imagens_perguntas/lote2_realista_v01_p03.png'}],
 'Raças de gatos': [{'pergunta': 'Qual destes gatos costuma ter pelagem longa e rosto achatado?',
                     'alternativas': ['Persa', 'Siamês', 'Maine Coon'],
                     'correta': 0,
                     'imagem': 'imagens_perguntas/lote2_realista_v02_p01.png'},
                    {'pergunta': 'Qual destas raças é conhecida pela ausência aparente de pelos?',
                     'alternativas': ['Bengal', 'Sphynx', 'British Shorthair'],
                     'correta': 1,
                     'imagem': 'imagens_perguntas/lote2_realista_v02_p02.png'},
                    {'pergunta': 'Qual destas raças pode apresentar orelhas dobradas para a frente?',
                     'alternativas': ['Ragdoll', 'Siamês', 'Scottish Fold'],
                     'correta': 2,
                     'imagem': 'imagens_perguntas/lote2_realista_v02_p03.png'}],
 'Flores e suas características': [{'pergunta': 'Qual destas flores costuma ter um grande centro cercado por '
                                                'pétalas amarelas?',
                                    'alternativas': ['Rosa', 'Girassol', 'Orquídea'],
                                    'correta': 1,
                                    'imagem': 'imagens_perguntas/lote2_realista_v03_p01.png'},
                                   {'pergunta': 'Qual destas flores costuma ter formato de taça?',
                                    'alternativas': ['Tulipa', 'Margarida', 'Lírio'],
                                    'correta': 0,
                                    'imagem': 'imagens_perguntas/lote2_realista_v03_p02.png'},
                                   {'pergunta': 'Qual destas plantas tem flores roxas em espigas e aroma '
                                                'marcante?',
                                    'alternativas': ['Cravo', 'Hortênsia', 'Lavanda'],
                                    'correta': 2,
                                    'imagem': 'imagens_perguntas/lote2_realista_v03_p03.png'}],
 'Árvores e suas folhas': [{'pergunta': 'Qual destas árvores costuma produzir pinhas?',
                            'alternativas': ['Coqueiro', 'Pinheiro', 'Ipê'],
                            'correta': 1,
                            'imagem': 'imagens_perguntas/lote2_realista_v04_p01.png'},
                           {'pergunta': 'Qual destas árvores produz azeitonas?',
                            'alternativas': ['Oliveira', 'Mangueira', 'Laranjeira'],
                            'correta': 0,
                            'imagem': 'imagens_perguntas/lote2_realista_v04_p02.png'},
                           {'pergunta': 'Qual destas árvores produz bolotas?',
                            'alternativas': ['Castanheira', 'Eucalipto', 'Carvalho'],
                            'correta': 2,
                            'imagem': 'imagens_perguntas/lote2_realista_v04_p03.png'}],
 'Tipos de pães': [{'pergunta': 'Qual destes pães é conhecido pelo formato comprido e casca crocante?',
                    'alternativas': ['Baguete', 'Pão de forma', 'Croissant'],
                    'correta': 0,
                    'imagem': 'imagens_perguntas/lote2_realista_v05_p01.png'},
                   {'pergunta': 'Qual destes pães costuma ser assado em uma forma retangular?',
                    'alternativas': ['Pão francês', 'Pão de forma', 'Pão sírio'],
                    'correta': 1,
                    'imagem': 'imagens_perguntas/lote2_realista_v05_p02.png'},
                   {'pergunta': 'Qual destes produtos de padaria tem formato de meia-lua e massa folhada?',
                    'alternativas': ['Brioche', 'Pão de queijo', 'Croissant'],
                    'correta': 2,
                    'imagem': 'imagens_perguntas/lote2_realista_v05_p03.png'}],
 'Massas e pratos italianos': [{'pergunta': 'Qual destas massas tem formato de fios longos e finos?',
                                'alternativas': ['Lasanha', 'Espaguete', 'Ravióli'],
                                'correta': 1,
                                'imagem': 'imagens_perguntas/lote2_realista_v06_p01.png'},
                               {'pergunta': 'Qual destas massas tem formato de pequenos tubos com pontas '
                                            'diagonais?',
                                'alternativas': ['Penne', 'Fusilli', 'Farfalle'],
                                'correta': 0,
                                'imagem': 'imagens_perguntas/lote2_realista_v06_p02.png'},
                               {'pergunta': 'Qual destes pratos costuma ser montado em camadas de massa?',
                                'alternativas': ['Nhoque', 'Ravióli', 'Lasanha'],
                                'correta': 2,
                                'imagem': 'imagens_perguntas/lote2_realista_v06_p03.png'}],
 'Bebidas e seus ingredientes': [{'pergunta': 'Qual destas bebidas é preparada com grãos torrados de café?',
                                  'alternativas': ['Café', 'Chá', 'Chocolate quente'],
                                  'correta': 0,
                                  'imagem': 'imagens_perguntas/lote2_realista_v07_p01.png'},
                                 {'pergunta': 'Qual destes sucos costuma ser preparado com uma fruta '
                                              'cítrica?',
                                  'alternativas': ['Suco de uva', 'Suco de laranja', 'Suco de manga'],
                                  'correta': 1,
                                  'imagem': 'imagens_perguntas/lote2_realista_v07_p02.png'},
                                 {'pergunta': 'Qual destas bebidas costuma levar café expresso, leite e '
                                              'espuma de leite?',
                                  'alternativas': ['Chá de hortelã', 'Limonada', 'Cappuccino'],
                                  'correta': 2,
                                  'imagem': 'imagens_perguntas/lote2_realista_v07_p03.png'}],
 'Móveis da casa': [{'pergunta': 'Qual destes móveis é um assento acolchoado para uma pessoa, geralmente com '
                                 'braços?',
                     'alternativas': ['Sofá', 'Poltrona', 'Cadeira'],
                     'correta': 1,
                     'imagem': 'imagens_perguntas/lote2_realista_v08_p01.png'},
                    {'pergunta': 'Qual destes móveis tem gavetas para guardar roupas e objetos?',
                     'alternativas': ['Cômoda', 'Mesa de centro', 'Estante'],
                     'correta': 0,
                     'imagem': 'imagens_perguntas/lote2_realista_v08_p02.png'},
                    {'pergunta': 'Qual destes móveis é próprio para dormir?',
                     'alternativas': ['Escrivaninha', 'Armário', 'Cama'],
                     'correta': 2,
                     'imagem': 'imagens_perguntas/lote2_realista_v08_p03.png'}],
 'Objetos de escritório': [{'pergunta': 'Qual destes objetos une folhas usando grampos metálicos?',
                            'alternativas': ['Grampeador', 'Furador', 'Apontador'],
                            'correta': 0,
                            'imagem': 'imagens_perguntas/lote2_realista_v09_p01.png'},
                           {'pergunta': 'Qual destes objetos serve para retirar grampos do papel?',
                            'alternativas': ['Clipes', 'Extrator de grampos', 'Borracha'],
                            'correta': 1,
                            'imagem': 'imagens_perguntas/lote2_realista_v09_p02.png'},
                           {'pergunta': 'Qual destes objetos costuma ser usado para apagar marcas de lápis?',
                            'alternativas': ['Tesoura', 'Régua', 'Borracha'],
                            'correta': 2,
                            'imagem': 'imagens_perguntas/lote2_realista_v09_p03.png'}],
 'Equipamentos de camping': [{'pergunta': 'Qual destes equipamentos serve de abrigo para dormir ao ar livre?',
                              'alternativas': ['Saco de dormir', 'Barraca', 'Lanterna'],
                              'correta': 1,
                              'imagem': 'imagens_perguntas/lote2_realista_v10_p01.png'},
                             {'pergunta': 'Qual destes equipamentos é usado para iluminar no escuro?',
                              'alternativas': ['Lampião', 'Cantil', 'Bússola'],
                              'correta': 0,
                              'imagem': 'imagens_perguntas/lote2_realista_v10_p02.png'},
                             {'pergunta': 'Qual destes equipamentos é usado para cozinhar em acampamentos?',
                              'alternativas': ['Mochila', 'Colchonete', 'Fogareiro'],
                              'correta': 2,
                              'imagem': 'imagens_perguntas/lote2_realista_v10_p03.png'}],
 'Curiosidades sobre o café': [{'pergunta': 'Qual parte da planta é torrada para produzir o café?',
                                'alternativas': ['As folhas', 'As sementes', 'As raízes'],
                                'correta': 1},
                               {'pergunta': 'Como se chama a bebida preparada ao passar água sob pressão '
                                            'pelo café moído?',
                                'alternativas': ['Expresso', 'Suco', 'Infusão de frutas'],
                                'correta': 0},
                               {'pergunta': 'Qual objeto costuma reter o pó no preparo do café coado?',
                                'alternativas': ['Ralador', 'Batedor', 'Filtro'],
                                'correta': 2}],
 'A história do chocolate': [{'pergunta': 'Qual é a principal matéria-prima do chocolate?',
                              'alternativas': ['Cacau', 'Trigo', 'Arroz'],
                              'correta': 0},
                             {'pergunta': 'Em qual região surgiram tradições antigas de consumo de cacau '
                                          'entre maias e astecas?',
                              'alternativas': ['Escandinávia', 'Mesoamérica', 'Oceania'],
                              'correta': 1},
                             {'pergunta': 'Qual tipo de chocolate costuma ter maior presença de sólidos de '
                                          'cacau que o chocolate ao leite?',
                              'alternativas': ['Branco', 'Rosa sem cacau', 'Amargo'],
                              'correta': 2}],
 'Como o queijo é produzido': [{'pergunta': 'Qual ingrediente é a base da produção de muitos queijos?',
                                'alternativas': ['Óleo', 'Leite', 'Mel'],
                                'correta': 1},
                               {'pergunta': 'Como se chama o processo que forma a coalhada do leite?',
                                'alternativas': ['Coagulação', 'Evaporação total', 'Congelamento'],
                                'correta': 0},
                               {'pergunta': 'Qual líquido se separa da coalhada durante a fabricação do '
                                            'queijo?',
                                'alternativas': ['Azeite', 'Xarope', 'Soro'],
                                'correta': 2}],
 'De onde vêm os perfumes?': [{'pergunta': 'Qual planta é conhecida por fornecer aroma para perfumes?',
                               'alternativas': ['Lavanda', 'Alface', 'Batata'],
                               'correta': 0},
                              {'pergunta': 'Qual líquido é frequentemente usado como solvente em perfumes?',
                               'alternativas': ['Óleo de motor', 'Álcool', 'Água sanitária'],
                               'correta': 1},
                              {'pergunta': 'Como são chamados os aromas que compõem um perfume?',
                               'alternativas': ['Capítulos', 'Fases lunares', 'Notas'],
                               'correta': 2}],
 'Como o sabão limpa?': [{'pergunta': 'O sabão ajuda a água a remover principalmente...',
                          'alternativas': ['Luz', 'Gordura', 'Som'],
                          'correta': 1},
                         {'pergunta': 'Qual parte de uma molécula de sabão tem afinidade com a água?',
                          'alternativas': ['A parte hidrofílica', 'A parte metálica', 'A parte luminosa'],
                          'correta': 0},
                         {'pergunta': 'Como se chamam os agrupamentos de moléculas que podem envolver a '
                                      'gordura na água?',
                          'alternativas': ['Cristais de sal', 'Bolhas de ferro', 'Micelas'],
                          'correta': 2}],
 'Por que o pão cresce?': [{'pergunta': 'Qual microrganismo é usado no fermento biológico do pão?',
                            'alternativas': ['Levedura', 'Alga', 'Vírus'],
                            'correta': 0},
                           {'pergunta': 'Qual gás produzido na fermentação ajuda a massa a crescer?',
                            'alternativas': ['Oxigênio puro', 'Dióxido de carbono', 'Hélio'],
                            'correta': 1},
                           {'pergunta': 'Qual etapa costuma dar tempo para o fermento agir?',
                            'alternativas': ['Trituração', 'Congelamento imediato', 'Descanso da massa'],
                            'correta': 2}],
 'Como funciona uma geladeira?': [{'pergunta': 'A geladeira resfria seu interior principalmente ao...',
                                   'alternativas': ['Criar gelo do nada',
                                                    'Retirar calor de dentro',
                                                    'Destruir o ar'],
                                   'correta': 1},
                                  {'pergunta': 'Qual componente comprime o fluido refrigerante?',
                                   'alternativas': ['Compressor', 'Puxador', 'Prateleira'],
                                   'correta': 0},
                                  {'pergunta': 'Para onde o calor retirado do interior é transferido?',
                                   'alternativas': ['Para dentro dos alimentos',
                                                    'Para a lâmpada apenas',
                                                    'Para o ambiente externo'],
                                   'correta': 2}],
 'Por que o gelo flutua?': [{'pergunta': 'O gelo flutua na água líquida porque é...',
                             'alternativas': ['Menos denso', 'Mais denso', 'Feito de ar puro'],
                             'correta': 0},
                            {'pergunta': 'Ao congelar, a água normalmente...',
                             'alternativas': ['Desaparece', 'Aumenta de volume', 'Vira metal'],
                             'correta': 1},
                            {'pergunta': 'Em qual estado físico a água forma o gelo?',
                             'alternativas': ['Gasoso', 'Plasma', 'Sólido'],
                             'correta': 2}],
 'Como se formam as cavernas?': [{'pergunta': 'Qual tipo de rocha pode ser dissolvido lentamente e formar '
                                              'muitas cavernas?',
                                  'alternativas': ['Plástico', 'Calcário', 'Aço'],
                                  'correta': 1},
                                 {'pergunta': 'Como se chama a formação que cresce do teto de uma caverna?',
                                  'alternativas': ['Estalactite', 'Estalagmite', 'Duna'],
                                  'correta': 0},
                                 {'pergunta': 'Como se chama a formação que cresce do chão de uma caverna?',
                                  'alternativas': ['Estalactite', 'Iceberg', 'Estalagmite'],
                                  'correta': 2}],
 'Vulcões e suas curiosidades': [{'pergunta': 'Como se chama o material rochoso fundido antes de chegar à '
                                              'superfície?',
                                  'alternativas': ['Magma', 'Gelo', 'Areia'],
                                  'correta': 0},
                                 {'pergunta': 'Ao chegar à superfície, o magma passa a ser chamado de...',
                                  'alternativas': ['Granizo', 'Lava', 'Argila'],
                                  'correta': 1},
                                 {'pergunta': 'Qual abertura costuma ficar no topo de um vulcão?',
                                  'alternativas': ['Dolina', 'Estuário', 'Cratera'],
                                  'correta': 2}],
 'Como surgem as ilhas?': [{'pergunta': 'Qual destes processos pode formar uma ilha no oceano?',
                            'alternativas': ['Pintura', 'Atividade vulcânica', 'Condensação do ar'],
                            'correta': 1},
                           {'pergunta': 'Como se chama um conjunto de ilhas?',
                            'alternativas': ['Arquipélago', 'Cordilheira', 'Planície'],
                            'correta': 0},
                           {'pergunta': 'Uma ilha é uma porção de terra cercada por...',
                            'alternativas': ['Montanhas', 'Estradas', 'Água'],
                            'correta': 2}],
 'Por que existem as estações do ano?': [{'pergunta': 'Qual fator é fundamental para a ocorrência das '
                                                      'estações do ano?',
                                          'alternativas': ['Inclinação do eixo da Terra',
                                                           'Cor da Lua',
                                                           'Salinidade dos oceanos'],
                                          'correta': 0},
                                         {'pergunta': 'Quando é verão no Hemisfério Sul, no Hemisfério Norte '
                                                      'é...',
                                          'alternativas': ['Verão também', 'Inverno', 'Sempre primavera'],
                                          'correta': 1},
                                         {'pergunta': 'Como se chama o movimento da Terra ao redor do Sol?',
                                          'alternativas': ['Rotação', 'Vibração', 'Translação'],
                                          'correta': 2}],
 'Como as bússolas indicam o norte?': [{'pergunta': 'A agulha de uma bússola comum se orienta pelo...',
                                        'alternativas': ['Cheiro do vento',
                                                         'Campo magnético da Terra',
                                                         'Som dos oceanos'],
                                        'correta': 1},
                                       {'pergunta': 'Qual ponto cardeal é oposto ao norte?',
                                        'alternativas': ['Sul', 'Leste', 'Oeste'],
                                        'correta': 0},
                                       {'pergunta': 'O norte apontado pela bússola comum é o norte...',
                                        'alternativas': ['Solar', 'Lunar', 'Magnético'],
                                        'correta': 2}],
 'Como funciona um elevador?': [{'pergunta': 'Como se chama a parte do elevador em que entram os '
                                             'passageiros?',
                                 'alternativas': ['Cabina', 'Caldeira', 'Turbina'],
                                 'correta': 0},
                                {'pergunta': 'Em muitos elevadores de tração, qual peça ajuda a equilibrar a '
                                             'cabina?',
                                 'alternativas': ['Antena', 'Contrapeso', 'Filtro'],
                                 'correta': 1},
                                {'pergunta': 'Qual dispositivo impede o funcionamento normal com a porta de '
                                             'pavimento aberta?',
                                 'alternativas': ['Ventilador', 'Espelho', 'Intertravamento da porta'],
                                 'correta': 2}],
 'A história da fotografia': [{'pergunta': 'Qual dispositivo óptico projeta uma imagem invertida através de '
                                           'uma pequena abertura?',
                               'alternativas': ['Bússola', 'Câmara escura', 'Termômetro'],
                               'correta': 1},
                              {'pergunta': 'Na fotografia tradicional, onde a imagem pode ser registrada?',
                               'alternativas': ['Filme fotográfico', 'Disco de vinil', 'Fita métrica'],
                               'correta': 0},
                              {'pergunta': 'Na câmera digital, qual componente capta a luz?',
                               'alternativas': ['Alto-falante', 'Ventoinha', 'Sensor de imagem'],
                               'correta': 2}],
 'Como os livros são produzidos?': [{'pergunta': 'Qual etapa organiza o texto e as imagens nas páginas?',
                                     'alternativas': ['Diagramação', 'Fermentação', 'Destilação'],
                                     'correta': 0},
                                    {'pergunta': 'Como se chama o processo de unir as páginas de um livro?',
                                     'alternativas': ['Fundição', 'Encadernação', 'Calibração'],
                                     'correta': 1},
                                    {'pergunta': 'Qual profissional escreve o conteúdo de uma obra?',
                                     'alternativas': ['Carteiro', 'Mecânico', 'Autor'],
                                     'correta': 2}],
 'Curiosidades sobre o correio': [{'pergunta': 'Qual código ajuda a identificar endereços postais no Brasil?',
                                   'alternativas': ['CPF', 'CEP', 'ISBN'],
                                   'correta': 1},
                                  {'pergunta': 'Qual item tradicional comprova o pagamento da postagem de '
                                               'uma carta?',
                                   'alternativas': ['Selo postal', 'Ingresso', 'Cupom de cinema'],
                                   'correta': 0},
                                  {'pergunta': 'Como se chama o profissional que entrega correspondências?',
                                   'alternativas': ['Bibliotecário', 'Piloto', 'Carteiro'],
                                   'correta': 2}],
 'De onde vêm os sobrenomes?': [{'pergunta': 'Qual destes sobrenomes também é o nome de uma árvore?',
                                 'alternativas': ['Pereira', 'Santos', 'Nunes'],
                                 'correta': 0},
                                {'pergunta': 'Um sobrenome derivado do nome de um antepassado é chamado '
                                             'de...',
                                 'alternativas': ['Onomatopeia', 'Patronímico', 'Antônimo'],
                                 'correta': 1},
                                {'pergunta': 'Qual destes sobrenomes tem relação com a palavra ferro?',
                                 'alternativas': ['Costa', 'Oliveira', 'Ferreira'],
                                 'correta': 2}],
 'Festas e tradições brasileiras': [{'pergunta': 'Qual dança é muito associada às festas juninas?',
                                     'alternativas': ['Balé', 'Quadrilha', 'Tango'],
                                     'correta': 1},
                                    {'pergunta': 'Qual festa é conhecida pelos desfiles de escolas de samba?',
                                     'alternativas': ['Carnaval', 'Páscoa', 'Natal'],
                                     'correta': 0},
                                    {'pergunta': 'Qual celebração apresenta a disputa entre os bois '
                                                 'Garantido e Caprichoso?',
                                     'alternativas': ['Oktoberfest', 'Festa da Uva', 'Festival de Parintins'],
                                     'correta': 2}],
 'Invenções que mudaram a comunicação': [{'pergunta': 'Qual invenção permite transmitir a voz por meio de '
                                                      'chamadas?',
                                          'alternativas': ['Telefone', 'Microscópio', 'Termômetro'],
                                          'correta': 0},
                                         {'pergunta': 'Qual sistema transmitia mensagens usando sinais como '
                                                      'pontos e traços?',
                                          'alternativas': ['Fonógrafo', 'Telégrafo', 'Projetor'],
                                          'correta': 1},
                                         {'pergunta': 'Qual tecnologia conecta redes de computadores em '
                                                      'escala mundial?',
                                          'alternativas': ['Máquina de escrever',
                                                           'Rádio de pilha',
                                                           'Internet'],
                                          'correta': 2}]}

LEGENDAS = {'Raças de cães': 'CAPA_SEGUNDOS=2\n'
                  '\n'
                  'Raças de cães: você acerta as três perguntas? Conte sua pontuação nos comentários!\n'
                  '#RacasDeCaes #Poodle #Dachshund #Chihuahua',
 'Raças de gatos': 'CAPA_SEGUNDOS=2\n'
                   '\n'
                   'Raças de gatos: você acerta as três perguntas? Conte sua pontuação nos comentários!\n'
                   '#RacasDeGatos #Persa #Sphynx #ScottishFold',
 'Flores e suas características': 'CAPA_SEGUNDOS=2\n'
                                  '\n'
                                  'Flores e suas características: você acerta as três perguntas? Conte sua '
                                  'pontuação nos comentários!\n'
                                  '#Flores #Girassol #Tulipa #Lavanda',
 'Árvores e suas folhas': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Árvores e suas folhas: você acerta as três perguntas? Conte sua pontuação nos '
                          'comentários!\n'
                          '#Arvores #Pinheiro #Oliveira #Carvalho',
 'Tipos de pães': 'CAPA_SEGUNDOS=2\n'
                  '\n'
                  'Tipos de pães: você acerta as três perguntas? Conte sua pontuação nos comentários!\n'
                  '#Paes #Baguete #PaoDeForma #Croissant',
 'Massas e pratos italianos': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Massas e pratos italianos: você acerta as três perguntas? Conte sua pontuação '
                              'nos comentários!\n'
                              '#MassasItalianas #Espaguete #Penne #Lasanha',
 'Bebidas e seus ingredientes': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Bebidas e seus ingredientes: você acerta as três perguntas? Conte sua '
                                'pontuação nos comentários!\n'
                                '#Bebidas #Cafe #SucoDeLaranja #Cappuccino',
 'Móveis da casa': 'CAPA_SEGUNDOS=2\n'
                   '\n'
                   'Móveis da casa: você acerta as três perguntas? Conte sua pontuação nos comentários!\n'
                   '#Moveis #Poltrona #Comoda #Cama',
 'Objetos de escritório': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Objetos de escritório: você acerta as três perguntas? Conte sua pontuação nos '
                          'comentários!\n'
                          '#Escritorio #Grampeador #ExtratorDeGrampos #Borracha',
 'Equipamentos de camping': 'CAPA_SEGUNDOS=2\n'
                            '\n'
                            'Equipamentos de camping: você acerta as três perguntas? Conte sua pontuação nos '
                            'comentários!\n'
                            '#Camping #Barraca #Lanterna #Fogareiro',
 'Curiosidades sobre o café': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Curiosidades sobre o café: você acerta as três perguntas? Conte sua pontuação '
                              'nos comentários!\n'
                              '#Cafe #CafeExpresso #CafeCoado #GraosDeCafe',
 'A história do chocolate': 'CAPA_SEGUNDOS=2\n'
                            '\n'
                            'A história do chocolate: você acerta as três perguntas? Conte sua pontuação nos '
                            'comentários!\n'
                            '#Chocolate #Cacau #ChocolateAmargo #HistoriaDoChocolate',
 'Como o queijo é produzido': 'CAPA_SEGUNDOS=2\n'
                              '\n'
                              'Como o queijo é produzido: você acerta as três perguntas? Conte sua pontuação '
                              'nos comentários!\n'
                              '#Queijo #Leite #Coalhada #FabricacaoDeQueijo',
 'De onde vêm os perfumes?': 'CAPA_SEGUNDOS=2\n'
                             '\n'
                             'De onde vêm os perfumes?: você acerta as três perguntas? Conte sua pontuação '
                             'nos comentários!\n'
                             '#Perfumes #Lavanda #NotasOlfativas #Perfumaria',
 'Como o sabão limpa?': 'CAPA_SEGUNDOS=2\n'
                        '\n'
                        'Como o sabão limpa?: você acerta as três perguntas? Conte sua pontuação nos '
                        'comentários!\n'
                        '#Sabao #Gordura #Micelas #QuimicaDoCotidiano',
 'Por que o pão cresce?': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Por que o pão cresce?: você acerta as três perguntas? Conte sua pontuação nos '
                          'comentários!\n'
                          '#Pao #Fermentacao #Leveduras #FermentoBiologico',
 'Como funciona uma geladeira?': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Como funciona uma geladeira?: você acerta as três perguntas? Conte sua '
                                 'pontuação nos comentários!\n'
                                 '#Geladeira #Refrigeracao #Compressor #TrocaDeCalor',
 'Por que o gelo flutua?': 'CAPA_SEGUNDOS=2\n'
                           '\n'
                           'Por que o gelo flutua?: você acerta as três perguntas? Conte sua pontuação nos '
                           'comentários!\n'
                           '#Gelo #Agua #Densidade #EstadosFisicos',
 'Como se formam as cavernas?': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Como se formam as cavernas?: você acerta as três perguntas? Conte sua '
                                'pontuação nos comentários!\n'
                                '#Cavernas #Calcario #Estalactites #Estalagmites',
 'Vulcões e suas curiosidades': 'CAPA_SEGUNDOS=2\n'
                                '\n'
                                'Vulcões e suas curiosidades: você acerta as três perguntas? Conte sua '
                                'pontuação nos comentários!\n'
                                '#Vulcoes #Magma #Lava #Cratera',
 'Como surgem as ilhas?': 'CAPA_SEGUNDOS=2\n'
                          '\n'
                          'Como surgem as ilhas?: você acerta as três perguntas? Conte sua pontuação nos '
                          'comentários!\n'
                          '#Ilhas #Arquipelagos #IlhasVulcanicas #Geografia',
 'Por que existem as estações do ano?': 'CAPA_SEGUNDOS=2\n'
                                        '\n'
                                        'Por que existem as estações do ano?: você acerta as três perguntas? '
                                        'Conte sua pontuação nos comentários!\n'
                                        '#EstacoesDoAno #Terra #Hemisferios #Translacao',
 'Como as bússolas indicam o norte?': 'CAPA_SEGUNDOS=2\n'
                                      '\n'
                                      'Como as bússolas indicam o norte?: você acerta as três perguntas? '
                                      'Conte sua pontuação nos comentários!\n'
                                      '#Bussola #NorteMagnetico #CampoMagnetico #Orientacao',
 'Como funciona um elevador?': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'Como funciona um elevador?: você acerta as três perguntas? Conte sua '
                               'pontuação nos comentários!\n'
                               '#Elevadores #Cabina #Contrapeso #Engenharia',
 'A história da fotografia': 'CAPA_SEGUNDOS=2\n'
                             '\n'
                             'A história da fotografia: você acerta as três perguntas? Conte sua pontuação '
                             'nos comentários!\n'
                             '#Fotografia #CamaraEscura #FilmeFotografico #CameraDigital',
 'Como os livros são produzidos?': 'CAPA_SEGUNDOS=2\n'
                                   '\n'
                                   'Como os livros são produzidos?: você acerta as três perguntas? Conte sua '
                                   'pontuação nos comentários!\n'
                                   '#Livros #Diagramacao #Encadernacao #ProducaoEditorial',
 'Curiosidades sobre o correio': 'CAPA_SEGUNDOS=2\n'
                                 '\n'
                                 'Curiosidades sobre o correio: você acerta as três perguntas? Conte sua '
                                 'pontuação nos comentários!\n'
                                 '#Correio #CEP #SeloPostal #Carteiro',
 'De onde vêm os sobrenomes?': 'CAPA_SEGUNDOS=2\n'
                               '\n'
                               'De onde vêm os sobrenomes?: você acerta as três perguntas? Conte sua '
                               'pontuação nos comentários!\n'
                               '#Sobrenomes #Pereira #Patronimicos #Ferreira',
 'Festas e tradições brasileiras': 'CAPA_SEGUNDOS=2\n'
                                   '\n'
                                   'Festas e tradições brasileiras: você acerta as três perguntas? Conte sua '
                                   'pontuação nos comentários!\n'
                                   '#FestasBrasileiras #FestasJuninas #Carnaval #Parintins',
 'Invenções que mudaram a comunicação': 'CAPA_SEGUNDOS=2\n'
                                        '\n'
                                        'Invenções que mudaram a comunicação: você acerta as três perguntas? '
                                        'Conte sua pontuação nos comentários!\n'
                                        '#Comunicacao #Telefone #Telegrafo #Internet'}
