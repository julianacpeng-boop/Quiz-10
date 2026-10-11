# Juh Quiz — rodada 3: 30 vídeos, 90 perguntas e exatamente 4 hashtags por legenda.
# Os vídeos 1, 2 e 3 usam imagens nas três perguntas.
# correta: 0=A, 1=B, 2=C.

QUIZZES = {'Frutas: descubra pela imagem': [{'pergunta': 'Qual fruta aparece na imagem?',
                                   'alternativas': ['Pitaya', 'Goiaba', 'Pera'],
                                   'correta': 0,
                                   'imagem': 'imagens_perguntas/rodada3_v01_p01.png'},
                                  {'pergunta': 'Qual fruta aparece na imagem?',
                                   'alternativas': ['Pêssego', 'Carambola', 'Mamão'],
                                   'correta': 1,
                                   'imagem': 'imagens_perguntas/rodada3_v01_p02.png'},
                                  {'pergunta': 'Qual fruta aparece na imagem?',
                                   'alternativas': ['Limão', 'Caju', 'Romã'],
                                   'correta': 2,
                                   'imagem': 'imagens_perguntas/rodada3_v01_p03.png'}],
 'Animais: quem está na foto?': [{'pergunta': 'Qual animal aparece na imagem?',
                                  'alternativas': ['Lobo', 'Raposa', 'Capivara'],
                                  'correta': 2,
                                  'imagem': 'imagens_perguntas/rodada3_v02_p01.png'},
                                 {'pergunta': 'Qual animal aparece na imagem?',
                                  'alternativas': ['Tucano', 'Arara', 'Coruja'],
                                  'correta': 0,
                                  'imagem': 'imagens_perguntas/rodada3_v02_p02.png'},
                                 {'pergunta': 'Qual animal aparece na imagem?',
                                  'alternativas': ['Pinguim', 'Tamanduá-bandeira', 'Jacaré'],
                                  'correta': 1,
                                  'imagem': 'imagens_perguntas/rodada3_v02_p03.png'}],
 'Comidas: reconheça o prato': [{'pergunta': 'Qual comida aparece na imagem?',
                                 'alternativas': ['Quindim', 'Pamonha', 'Coxinha'],
                                 'correta': 1,
                                 'imagem': 'imagens_perguntas/rodada3_v03_p01.png'},
                                {'pergunta': 'Qual comida aparece na imagem?',
                                 'alternativas': ['Pastel', 'Empada', 'Acarajé'],
                                 'correta': 2,
                                 'imagem': 'imagens_perguntas/rodada3_v03_p02.png'},
                                {'pergunta': 'Qual comida aparece na imagem?',
                                 'alternativas': ['Brigadeiro', 'Paçoca', 'Bolo de cenoura'],
                                 'correta': 0,
                                 'imagem': 'imagens_perguntas/rodada3_v03_p03.png'}],
 'Futebol: dentro do campo': [{'pergunta': 'Como se chama a cobrança realizada a partir do canto '
                                           'do campo?',
                               'alternativas': ['Escanteio', 'Pênalti', 'Tiro de meta'],
                               'correta': 0},
                              {'pergunta': 'Qual jogador pode usar as mãos dentro da própria área '
                                           'durante o jogo?',
                               'alternativas': ['Atacante', 'Goleiro', 'Zagueiro'],
                               'correta': 1},
                              {'pergunta': 'Qual cartão normalmente indica expulsão?',
                               'alternativas': ['Azul', 'Amarelo', 'Vermelho'],
                               'correta': 2}],
 'Relacionamento: respeito no cotidiano': [{'pergunta': 'Qual atitude respeita a privacidade do '
                                                        'parceiro?',
                                            'alternativas': ['Pedir permissão antes de '
                                                             'compartilhar algo pessoal',
                                                             'Ler mensagens escondido',
                                                             'Expor conversas privadas'],
                                            'correta': 0},
                                           {'pergunta': 'Qual atitude ajuda a resolver uma '
                                                        'discordância?',
                                            'alternativas': ['Ironizar',
                                                             'Ouvir antes de responder',
                                                             'Fazer ameaças'],
                                            'correta': 1},
                                           {'pergunta': 'Qual atitude demonstra responsabilidade '
                                                        'após magoar alguém?',
                                            'alternativas': ['Negar tudo',
                                                             'Culpar a outra pessoa',
                                                             'Pedir desculpas e mudar a atitude'],
                                            'correta': 2}],
 'Amizade: pequenos gestos': [{'pergunta': 'Como incluir alguém novo numa conversa?',
                               'alternativas': ['Apresentar as pessoas e dar espaço',
                                                'Ignorar a presença',
                                                'Falar apenas de histórias internas'],
                               'correta': 0},
                              {'pergunta': 'Qual atitude respeita um amigo que não quer sair?',
                               'alternativas': ['Insistir sem parar',
                                                'Aceitar a decisão',
                                                'Fazer chantagem'],
                               'correta': 1},
                              {'pergunta': 'Como agir diante de um boato sobre um amigo?',
                               'alternativas': ['Espalhar no grupo',
                                                'Publicar nas redes',
                                                'Evitar repassar sem verificar'],
                               'correta': 2}],
 'Frutas: nomes e formatos': [{'pergunta': '🍽️ Qual destas frutas costuma crescer em cachos?',
                               'alternativas': ['🍎 Maçã', '🍐 Pera', '🍇 Uva'],
                               'correta': 2},
                              {'pergunta': '🍽️ Qual destas frutas tem um caroço grande no centro?',
                               'alternativas': ['🥑 Abacate', '🍓 Morango', '🍌 Banana'],
                               'correta': 0},
                              {'pergunta': '🍽️ Qual destas frutas é cítrica?',
                               'alternativas': ['🍉 Melancia', '🍊 Laranja', '🍇 Uva'],
                               'correta': 1}],
 'Animais: onde vivem?': [{'pergunta': '🐾 Qual destes animais vive naturalmente no mar?',
                           'alternativas': ['🦒 Girafa', '🐬 Golfinho', '🐎 Cavalo'],
                           'correta': 1},
                          {'pergunta': '🐾 Qual destes animais é uma ave?',
                           'alternativas': ['🦋 Borboleta', '🐢 Tartaruga', '🦉 Coruja'],
                           'correta': 2},
                          {'pergunta': '🐾 Qual destes animais é um anfíbio?',
                           'alternativas': ['🐸 Sapo', '🐍 Cobra', '🐈 Gato'],
                           'correta': 0}],
 'Insetos: mundo pequeno': [{'pergunta': 'Quantas antenas tem um inseto adulto típico?',
                             'alternativas': ['Duas', 'Quatro', 'Seis'],
                             'correta': 0},
                            {'pergunta': 'Qual destes animais é um inseto?',
                             'alternativas': ['Aranha', 'Abelha', 'Escorpião'],
                             'correta': 1},
                            {'pergunta': 'Qual fase vem antes da borboleta adulta?',
                             'alternativas': ['Girino', 'Filhote de peixe', 'Pupa'],
                             'correta': 2}],
 'Plantas: partes e funções': [{'pergunta': 'Qual parte da planta costuma absorver água do solo?',
                                'alternativas': ['Flor', 'Raiz', 'Fruto'],
                                'correta': 1},
                               {'pergunta': 'Qual parte da planta geralmente contém sementes?',
                                'alternativas': ['Caule', 'Folha', 'Fruto'],
                                'correta': 2},
                               {'pergunta': 'Qual destas plantas é conhecida pelos espinhos?',
                                'alternativas': ['Cacto', 'Alface', 'Samambaia'],
                                'correta': 0}],
 'Comidas: ingredientes conhecidos': [{'pergunta': 'Qual grão é a base do risoto tradicional?',
                                       'alternativas': ['Arroz', 'Feijão', 'Lentilha'],
                                       'correta': 0},
                                      {'pergunta': 'Qual destes ingredientes é usado no guacamole '
                                                   'tradicional?',
                                       'alternativas': ['Batata', 'Abacate', 'Morango'],
                                       'correta': 1},
                                      {'pergunta': 'Qual ingrediente dá origem ao chocolate?',
                                       'alternativas': ['Trigo', 'Milho', 'Cacau'],
                                       'correta': 2}],
 'Na cozinha: utensílios': [{'pergunta': '🍳 Qual utensílio serve para escorrer massa?',
                             'alternativas': ['🥄 Colher', '🧺 Escorredor', '🔪 Faca'],
                             'correta': 1},
                            {'pergunta': '🍳 Qual utensílio serve para cortar alimentos?',
                             'alternativas': ['🍽️ Prato', '🥣 Tigela', '🔪 Faca'],
                             'correta': 2},
                            {'pergunta': '🍳 Qual utensílio ajuda a mexer uma sopa?',
                             'alternativas': ['🥄 Colher', '🍴 Garfo', '🍽️ Prato'],
                             'correta': 0}],
 'Doces: sabores brasileiros': [{'pergunta': 'Qual destes doces é preparado tradicionalmente com '
                                             'leite e açúcar?',
                                 'alternativas': ['Doce de leite',
                                                  'Gelatina de uva',
                                                  'Pé de moleque'],
                                 'correta': 0},
                                {'pergunta': 'Qual fruta aparece no nome da goiabada?',
                                 'alternativas': ['Banana', 'Goiaba', 'Manga'],
                                 'correta': 1},
                                {'pergunta': 'Qual destas sobremesas costuma ter calda de '
                                             'caramelo?',
                                 'alternativas': ['Salada de frutas',
                                                  'Sorvete de morango',
                                                  'Pudim de leite'],
                                 'correta': 2}],
 'Português: aumentativo e diminutivo': [{'pergunta': 'Qual é um diminutivo de casa?',
                                          'alternativas': ['Casarão', 'Casinha', 'Casamento'],
                                          'correta': 1},
                                         {'pergunta': 'Qual é um aumentativo de boca?',
                                          'alternativas': ['Boquinha', 'Bocadinho', 'Bocarra'],
                                          'correta': 2},
                                         {'pergunta': 'Qual palavra está no diminutivo?',
                                          'alternativas': ['Livrinho', 'Livraria', 'Livreiro'],
                                          'correta': 0}],
 'Português: significados': [{'pergunta': 'Qual palavra é sinônimo de alegre?',
                              'alternativas': ['Contente', 'Triste', 'Bravo'],
                              'correta': 0},
                             {'pergunta': 'Qual palavra é antônimo de perto?',
                              'alternativas': ['Próximo', 'Longe', 'Junto'],
                              'correta': 1},
                             {'pergunta': 'Qual palavra é sinônimo de rápido?',
                              'alternativas': ['Lento', 'Demorado', 'Veloz'],
                              'correta': 2}],
 'Português: classes de palavras': [{'pergunta': 'Na frase Ana corre, qual palavra é o verbo?',
                                     'alternativas': ['Ana', 'Corre', 'Nenhuma'],
                                     'correta': 1},
                                    {'pergunta': 'Na expressão casa bonita, qual palavra é o '
                                                 'adjetivo?',
                                     'alternativas': ['Casa', 'Nenhuma', 'Bonita'],
                                     'correta': 2},
                                    {'pergunta': 'Qual destas palavras é um substantivo?',
                                     'alternativas': ['Mesa', 'Correr', 'Rapidamente'],
                                     'correta': 0}],
 'Inglês: cores': [{'pergunta': '🎨 Como se diz vermelho em inglês?',
                    'alternativas': ['🔴 Red', '🔵 Blue', '🟢 Green'],
                    'correta': 0},
                   {'pergunta': '🎨 Como se diz amarelo em inglês?',
                    'alternativas': ['⚫ Black', '🟡 Yellow', '⚪ White'],
                    'correta': 1},
                   {'pergunta': '🎨 Como se diz verde em inglês?',
                    'alternativas': ['🟠 Orange', '🟣 Purple', '🟢 Green'],
                    'correta': 2}],
 'Espanhol: números': [{'pergunta': 'Qual número significa cinco em espanhol?',
                        'alternativas': ['Quatro', 'Cinco', 'Seis'],
                        'correta': 1},
                       {'pergunta': 'Qual número significa ocho em português?',
                        'alternativas': ['Sete', 'Nove', 'Oito'],
                        'correta': 2},
                       {'pergunta': 'Como se diz três em espanhol?',
                        'alternativas': ['Tres', 'Dos', 'Diez'],
                        'correta': 0}],
 'Ditados: termine a frase': [{'pergunta': 'Quem espera sempre...',
                               'alternativas': ['Alcança', 'Esquece', 'Corre'],
                               'correta': 0},
                              {'pergunta': 'Antes só do que...',
                               'alternativas': ['Bem vestido', 'Mal acompanhado', 'Com pressa'],
                               'correta': 1},
                              {'pergunta': 'Casa de ferreiro, espeto de...',
                               'alternativas': ['Ferro', 'Aço', 'Pau'],
                               'correta': 2}],
 'Adivinhas: coisas do dia a dia': [{'pergunta': 'O que tem folhas, mas não é uma planta, e pode '
                                                 'contar uma história?',
                                     'alternativas': ['Janela', 'Livro', 'Panela'],
                                     'correta': 1},
                                    {'pergunta': 'O que anda com os pés dos outros e se usa para '
                                                 'calçar?',
                                     'alternativas': ['Chapéu', 'Luva', 'Sapato'],
                                     'correta': 2},
                                    {'pergunta': 'O que abre caminhos no papel e diminui ao ser '
                                                 'apontado?',
                                     'alternativas': ['Lápis', 'Borracha', 'Régua'],
                                     'correta': 0}],
 'Lógica: sequência de números': [{'pergunta': 'Qual número continua a sequência: 3, 6, 9, 12...?',
                                   'alternativas': ['15', '18', '21'],
                                   'correta': 0},
                                  {'pergunta': 'Qual número continua a sequência: 1, 3, 5, 7...?',
                                   'alternativas': ['8', '9', '10'],
                                   'correta': 1},
                                  {'pergunta': 'Qual número continua a sequência: 20, 18, 16, '
                                               '14...?',
                                   'alternativas': ['10', '11', '12'],
                                   'correta': 2}],
 'Matemática: compras rápidas': [{'pergunta': 'Três itens de 10 reais custam quanto ao todo?',
                                  'alternativas': ['20 reais', '30 reais', '40 reais'],
                                  'correta': 1},
                                 {'pergunta': 'Você paga 50 reais por algo de 35 reais. Qual é o '
                                              'troco?',
                                  'alternativas': ['5 reais', '10 reais', '15 reais'],
                                  'correta': 2},
                                 {'pergunta': 'Dois ingressos de 12 reais custam quanto?',
                                  'alternativas': ['24 reais', '26 reais', '30 reais'],
                                  'correta': 0}],
 'Brasil: regiões': [{'pergunta': 'Em qual região fica o Ceará?',
                      'alternativas': ['Nordeste', 'Sul', 'Centro-Oeste'],
                      'correta': 0},
                     {'pergunta': 'Em qual região fica o Rio Grande do Sul?',
                      'alternativas': ['Norte', 'Sul', 'Sudeste'],
                      'correta': 1},
                     {'pergunta': 'Em qual região fica Goiás?',
                      'alternativas': ['Nordeste', 'Sudeste', 'Centro-Oeste'],
                      'correta': 2}],
 'Geografia: continentes': [{'pergunta': 'Em qual continente fica o Brasil?',
                             'alternativas': ['Europa', 'América do Sul', 'Ásia'],
                             'correta': 1},
                            {'pergunta': 'Em qual continente fica o Japão?',
                             'alternativas': ['África', 'Europa', 'Ásia'],
                             'correta': 2},
                            {'pergunta': 'Em qual continente fica a França?',
                             'alternativas': ['Europa', 'Oceania', 'África'],
                             'correta': 0}],
 'Espaço: nomes conhecidos': [{'pergunta': 'Como se chama nossa galáxia?',
                               'alternativas': ['Via Láctea', 'Andrômeda', 'Sistema Solar'],
                               'correta': 0},
                              {'pergunta': 'Qual planeta fica mais próximo do Sol?',
                               'alternativas': ['Vênus', 'Mercúrio', 'Marte'],
                               'correta': 1},
                              {'pergunta': 'Qual é o maior planeta do Sistema Solar?',
                               'alternativas': ['Terra', 'Netuno', 'Júpiter'],
                               'correta': 2}],
 'Tecnologia: arquivos e funções': [{'pergunta': 'Qual extensão costuma identificar um arquivo de '
                                                 'vídeo?',
                                     'alternativas': ['TXT', 'MP4', 'CSV'],
                                     'correta': 1},
                                    {'pergunta': 'Qual extensão costuma identificar uma imagem?',
                                     'alternativas': ['MP3', 'WAV', 'PNG'],
                                     'correta': 2},
                                    {'pergunta': 'Qual função faz uma cópia de um arquivo para '
                                                 'outro local?',
                                     'alternativas': ['Copiar', 'Apagar', 'Renomear'],
                                     'correta': 0}],
 'Cinema: mundos de fantasia': [{'pergunta': 'Qual personagem é um leão em O Rei Leão?',
                                 'alternativas': ['Simba', 'Dory', 'Olaf'],
                                 'correta': 0},
                                {'pergunta': 'Em Frozen, qual personagem é um boneco de neve?',
                                 'alternativas': ['Kristoff', 'Olaf', 'Hans'],
                                 'correta': 1},
                                {'pergunta': 'Qual personagem é um peixe-palhaço?',
                                 'alternativas': ['Dumbo', 'Bambi', 'Nemo'],
                                 'correta': 2}],
 'Desenhos: duplas famosas': [{'pergunta': 'Qual personagem é o rato da dupla Tom e Jerry?',
                               'alternativas': ['Tom', 'Jerry', 'Pateta'],
                               'correta': 1},
                              {'pergunta': 'Qual personagem é o amigo cachorro de Charlie Brown?',
                               'alternativas': ['Garfield', 'Felix', 'Snoopy'],
                               'correta': 2},
                              {'pergunta': 'Qual personagem é amigo de Patrick Estrela?',
                               'alternativas': ['Bob Esponja', 'Pernalonga', 'Pica-Pau'],
                               'correta': 0}],
 'Música: ritmo e voz': [{'pergunta': 'Como se chama uma pessoa que canta?',
                          'alternativas': ['Cantor', 'Pintor', 'Escultor'],
                          'correta': 0},
                         {'pergunta': 'Qual instrumento costuma ter seis cordas na versão '
                                      'tradicional?',
                          'alternativas': ['Flauta', 'Violão', 'Tambor'],
                          'correta': 1},
                         {'pergunta': 'Qual destes instrumentos pertence à percussão?',
                          'alternativas': ['Violino', 'Flauta', 'Pandeiro'],
                          'correta': 2}],
 'Esportes: equipamentos': [{'pergunta': '🏅 Qual objeto é usado no badminton?',
                             'alternativas': ['⚽ Bola de futebol',
                                              '🏸 Peteca',
                                              '🏀 Bola de basquete'],
                             'correta': 1},
                            {'pergunta': '🏅 Qual equipamento é usado para remar?',
                             'alternativas': ['🎾 Raquete', '🥊 Luva', '🚣 Remo'],
                             'correta': 2},
                            {'pergunta': '🏅 Qual objeto é usado no hóquei sobre o gelo?',
                             'alternativas': ['🏒 Taco', '🏓 Raquete', '🎯 Dardo'],
                             'correta': 0}]}

LEGENDAS = {'Frutas: descubra pela imagem': 'Frutas: descubra pela imagem! Você acerta as três? Comente seu '
                                 'resultado e desafie um amigo. 🧠\n'
                                 '\n'
                                 '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Animais: quem está na foto?': 'Animais: quem está na foto?! Você acerta as três? Comente seu '
                                'resultado e desafie um amigo. 🧠\n'
                                '\n'
                                '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Comidas: reconheça o prato': 'Comidas: reconheça o prato! Você acerta as três? Comente seu '
                               'resultado e desafie um amigo. 🧠\n'
                               '\n'
                               '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Futebol: dentro do campo': 'Futebol: dentro do campo! Você acerta as três? Comente seu resultado '
                             'e desafie um amigo. 🧠\n'
                             '\n'
                             '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Relacionamento: respeito no cotidiano': 'Relacionamento: respeito no cotidiano! Você acerta as '
                                          'três? Comente seu resultado e desafie um amigo. 🧠\n'
                                          '\n'
                                          '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Amizade: pequenos gestos': 'Amizade: pequenos gestos! Você acerta as três? Comente seu resultado '
                             'e desafie um amigo. 🧠\n'
                             '\n'
                             '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Frutas: nomes e formatos': 'Frutas: nomes e formatos! Você acerta as três? Comente seu resultado '
                             'e desafie um amigo. 🧠\n'
                             '\n'
                             '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Animais: onde vivem?': 'Animais: onde vivem?! Você acerta as três? Comente seu resultado e '
                         'desafie um amigo. 🧠\n'
                         '\n'
                         '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Insetos: mundo pequeno': 'Insetos: mundo pequeno! Você acerta as três? Comente seu resultado e '
                           'desafie um amigo. 🧠\n'
                           '\n'
                           '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Plantas: partes e funções': 'Plantas: partes e funções! Você acerta as três? Comente seu '
                              'resultado e desafie um amigo. 🧠\n'
                              '\n'
                              '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Comidas: ingredientes conhecidos': 'Comidas: ingredientes conhecidos! Você acerta as três? '
                                     'Comente seu resultado e desafie um amigo. 🧠\n'
                                     '\n'
                                     '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Na cozinha: utensílios': 'Na cozinha: utensílios! Você acerta as três? Comente seu resultado e '
                           'desafie um amigo. 🧠\n'
                           '\n'
                           '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Doces: sabores brasileiros': 'Doces: sabores brasileiros! Você acerta as três? Comente seu '
                               'resultado e desafie um amigo. 🧠\n'
                               '\n'
                               '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Português: aumentativo e diminutivo': 'Português: aumentativo e diminutivo! Você acerta as três? '
                                        'Comente seu resultado e desafie um amigo. 🧠\n'
                                        '\n'
                                        '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Português: significados': 'Português: significados! Você acerta as três? Comente seu resultado e '
                            'desafie um amigo. 🧠\n'
                            '\n'
                            '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Português: classes de palavras': 'Português: classes de palavras! Você acerta as três? Comente '
                                   'seu resultado e desafie um amigo. 🧠\n'
                                   '\n'
                                   '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Inglês: cores': 'Inglês: cores! Você acerta as três? Comente seu resultado e desafie um amigo. '
                  '🧠\n'
                  '\n'
                  '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Espanhol: números': 'Espanhol: números! Você acerta as três? Comente seu resultado e desafie um '
                      'amigo. 🧠\n'
                      '\n'
                      '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Ditados: termine a frase': 'Ditados: termine a frase! Você acerta as três? Comente seu resultado '
                             'e desafie um amigo. 🧠\n'
                             '\n'
                             '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Adivinhas: coisas do dia a dia': 'Adivinhas: coisas do dia a dia! Você acerta as três? Comente '
                                   'seu resultado e desafie um amigo. 🧠\n'
                                   '\n'
                                   '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Lógica: sequência de números': 'Lógica: sequência de números! Você acerta as três? Comente seu '
                                 'resultado e desafie um amigo. 🧠\n'
                                 '\n'
                                 '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Matemática: compras rápidas': 'Matemática: compras rápidas! Você acerta as três? Comente seu '
                                'resultado e desafie um amigo. 🧠\n'
                                '\n'
                                '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Brasil: regiões': 'Brasil: regiões! Você acerta as três? Comente seu resultado e desafie um '
                    'amigo. 🧠\n'
                    '\n'
                    '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Geografia: continentes': 'Geografia: continentes! Você acerta as três? Comente seu resultado e '
                           'desafie um amigo. 🧠\n'
                           '\n'
                           '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Espaço: nomes conhecidos': 'Espaço: nomes conhecidos! Você acerta as três? Comente seu resultado '
                             'e desafie um amigo. 🧠\n'
                             '\n'
                             '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Tecnologia: arquivos e funções': 'Tecnologia: arquivos e funções! Você acerta as três? Comente '
                                   'seu resultado e desafie um amigo. 🧠\n'
                                   '\n'
                                   '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Cinema: mundos de fantasia': 'Cinema: mundos de fantasia! Você acerta as três? Comente seu '
                               'resultado e desafie um amigo. 🧠\n'
                               '\n'
                               '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Desenhos: duplas famosas': 'Desenhos: duplas famosas! Você acerta as três? Comente seu resultado '
                             'e desafie um amigo. 🧠\n'
                             '\n'
                             '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Música: ritmo e voz': 'Música: ritmo e voz! Você acerta as três? Comente seu resultado e desafie '
                        'um amigo. 🧠\n'
                        '\n'
                        '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais',
 'Esportes: equipamentos': 'Esportes: equipamentos! Você acerta as três? Comente seu resultado e '
                           'desafie um amigo. 🧠\n'
                           '\n'
                           '#JuhQuiz #Quiz #Desafio #ConhecimentosGerais'}
