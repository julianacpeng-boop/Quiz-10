# Juh Quiz — rodada 2: 30 temas novos, 90 perguntas.
# Substitua dados_quiz.py no repositório. Imagens opcionais.
# correta: 0=A, 1=B, 2=C.

QUIZZES = {'Futebol: apelidos famosos': [{'pergunta': 'Qual clube é conhecido como Timão?',
                                'alternativas': ['Corinthians', 'Santos', 'Grêmio'],
                                'correta': 0},
                               {'pergunta': 'Qual clube é conhecido como Peixe?',
                                'alternativas': ['Palmeiras', 'Santos', 'Fluminense'],
                                'correta': 1},
                               {'pergunta': 'Qual seleção masculina é conhecida como Azzurra?',
                                'alternativas': ['França', 'Espanha', 'Itália'],
                                'correta': 2}],
 'Relacionamento: combinados': [{'pergunta': 'Qual atitude ajuda a organizar planos do casal?',
                                 'alternativas': ['Decidir sozinho',
                                                  'Conversar sobre expectativas',
                                                  'Fazer promessas vagas'],
                                 'correta': 1},
                                {'pergunta': 'Como lidar com um combinado que ficou inviável?',
                                 'alternativas': ['Esconder o problema',
                                                  'Culpar o parceiro',
                                                  'Conversar e renegociar'],
                                 'correta': 2},
                                {'pergunta': 'Qual atitude ajuda depois de um erro?',
                                 'alternativas': ['Reconhecer e reparar',
                                                  'Fingir que nada aconteceu',
                                                  'Repetir o erro'],
                                 'correta': 0}],
 'Amizade: quem é você no grupo?': [{'pergunta': 'O que significa guardar uma confidência?',
                                     'alternativas': ['Contar para todos',
                                                      'Preservar o que foi confiado',
                                                      'Publicar sem nome'],
                                     'correta': 1},
                                    {'pergunta': 'Qual atitude demonstra apoio a um amigo?',
                                     'alternativas': ['Ouvir com atenção',
                                                      'Desvalorizar o problema',
                                                      'Mudar sempre de assunto'],
                                     'correta': 0},
                                    {'pergunta': 'Qual atitude respeita o tempo de um amigo?',
                                     'alternativas': ['Exigir resposta imediata',
                                                      'Mandar cobranças repetidas',
                                                      'Aceitar que ele pode estar ocupado'],
                                     'correta': 2}],
 'Frutas: por dentro e por fora': [{'pergunta': '🍽️ Qual destas frutas costuma ter sementes pretas '
                                                'espalhadas na polpa?',
                                    'alternativas': ['🍌 Banana', '🥝 Kiwi', '🍊 Laranja'],
                                    'correta': 1},
                                   {'pergunta': '🍽️ Qual destas frutas tem gomos?',
                                    'alternativas': ['🍊 Tangerina', '🍎 Maçã', '🍓 Morango'],
                                    'correta': 0},
                                   {'pergunta': '🍽️ Qual destas frutas é conhecida pela casca '
                                                'coberta de espinhos?',
                                    'alternativas': ['🍉 Melancia', '🍇 Uva', '🍍 Abacaxi'],
                                    'correta': 2}],
 'Animais: habilidades incríveis': [{'pergunta': '🐾 Qual destes animais pode mudar de cor?',
                                     'alternativas': ['🐘 Elefante', '🦎 Camaleão', '🐎 Cavalo'],
                                     'correta': 1},
                                    {'pergunta': '🐾 Qual destes mamíferos põe ovos?',
                                     'alternativas': ['🐕 Cachorro', '🐈 Gato', '🦆 Ornitorrinco'],
                                     'correta': 2},
                                    {'pergunta': '🐾 Qual destes animais tem oito braços?',
                                     'alternativas': ['🐙 Polvo', '🦀 Caranguejo', '🐟 Sardinha'],
                                     'correta': 0}],
 'Pets: curiosidades': [{'pergunta': '🐾 Qual destes animais costuma ronronar?',
                         'alternativas': ['🐈 Gato', '🐕 Cachorro', '🐇 Coelho'],
                         'correta': 0},
                        {'pergunta': '🐾 Qual destes pets é um roedor?',
                         'alternativas': ['🐦 Canário', '🐹 Hamster', '🐈 Gato'],
                         'correta': 1},
                        {'pergunta': '🐾 Qual destes animais pertence ao grupo das aves?',
                         'alternativas': ['🐢 Tartaruga', '🐠 Peixe', '🦜 Papagaio'],
                         'correta': 2}],
 'Culinária brasileira': [{'pergunta': 'Qual prato é feito tradicionalmente com feijão e carnes?',
                           'alternativas': ['Moqueca', 'Feijoada', 'Cuscuz'],
                           'correta': 1},
                          {'pergunta': 'Qual ingrediente é a base do pão de queijo tradicional?',
                           'alternativas': ['Polvilho', 'Farinha de arroz', 'Aveia'],
                           'correta': 0},
                          {'pergunta': 'Qual destas comidas é preparada com goma de mandioca?',
                           'alternativas': ['Risoto', 'Macarrão', 'Tapioca'],
                           'correta': 2}],
 'Doces: adivinhe o ingrediente': [{'pergunta': 'Qual ingrediente dá o sabor tradicional ao '
                                                'beijinho?',
                                    'alternativas': ['Café', 'Coco', 'Limão'],
                                    'correta': 1},
                                   {'pergunta': 'Qual doce é feito tradicionalmente com amendoim e '
                                                'açúcar?',
                                    'alternativas': ['Pé de moleque', 'Quindim', 'Pudim de leite'],
                                    'correta': 0},
                                   {'pergunta': 'Qual ingrediente é característico do quindim?',
                                    'alternativas': ['Morango', 'Chocolate', 'Gemas'],
                                    'correta': 2}],
 'Bebidas e sabores': [{'pergunta': 'Qual bebida é preparada a partir de grãos torrados e moídos?',
                        'alternativas': ['Chá de camomila', 'Suco de uva', 'Café'],
                        'correta': 2},
                       {'pergunta': 'Qual fruta dá nome à limonada?',
                        'alternativas': ['Limão', 'Melancia', 'Pera'],
                        'correta': 0},
                       {'pergunta': 'Qual bebida costuma ser preparada com folhas de erva-mate?',
                        'alternativas': ['Chocolate quente', 'Chimarrão', 'Limonada'],
                        'correta': 1}],
 'Objetos de casa': [{'pergunta': '🏠 Qual objeto ajuda a medir a temperatura?',
                      'alternativas': ['🔑 Chave', '🌡️ Termômetro', '🪞 Espelho'],
                      'correta': 1},
                     {'pergunta': '🏠 Qual objeto é usado para passar roupas?',
                      'alternativas': ['🧹 Vassoura', '🪣 Balde', '♨️ Ferro de passar'],
                      'correta': 2},
                     {'pergunta': '🏠 Qual objeto ajuda a abrir uma porta trancada?',
                      'alternativas': ['🔑 Chave', '✂️ Tesoura', '🥄 Colher'],
                      'correta': 0}],
 'Português: palavras parecidas': [{'pergunta': 'Qual palavra indica uma quantidade maior?',
                                    'alternativas': ['Mas', 'Mais', 'Más'],
                                    'correta': 1},
                                   {'pergunta': 'Qual palavra se refere a uma pessoa que toca '
                                                'violino?',
                                    'alternativas': ['Violista', 'Violonista', 'Violinista'],
                                    'correta': 2},
                                   {'pergunta': 'Qual é o plural de papel?',
                                    'alternativas': ['Papéis', 'Papels', 'Papeis sem acento'],
                                    'correta': 0}],
 'Português: acerte a escrita': [{'pergunta': 'Qual palavra está escrita corretamente?',
                                  'alternativas': ['Exceção', 'Excessão', 'Esseção'],
                                  'correta': 0},
                                 {'pergunta': 'Qual palavra está escrita corretamente?',
                                  'alternativas': ['Enchergar', 'Enxergar', 'Enxerguar'],
                                  'correta': 1},
                                 {'pergunta': 'Qual palavra está escrita corretamente?',
                                  'alternativas': ['Geito', 'Jeitto', 'Jeito'],
                                  'correta': 2}],
 'Inglês: palavras do dia a dia': [{'pergunta': 'Como se diz janela em inglês?',
                                    'alternativas': ['Door', 'Window', 'Floor'],
                                    'correta': 1},
                                   {'pergunta': 'Como se diz cadeira em inglês?',
                                    'alternativas': ['Chair', 'Table', 'Bed'],
                                    'correta': 0},
                                   {'pergunta': 'Como se diz noite em inglês?',
                                    'alternativas': ['Morning', 'Afternoon', 'Night'],
                                    'correta': 2}],
 'Espanhol: palavras básicas': [{'pergunta': 'Como se diz cachorro em espanhol?',
                                 'alternativas': ['Gato', 'Pájaro', 'Perro'],
                                 'correta': 2},
                                {'pergunta': 'O que significa gracias em português?',
                                 'alternativas': ['Obrigado', 'Desculpe', 'Até amanhã'],
                                 'correta': 0},
                                {'pergunta': 'Como se diz segunda-feira em espanhol?',
                                 'alternativas': ['Martes', 'Lunes', 'Viernes'],
                                 'correta': 1}],
 'Gírias: você entende?': [{'pergunta': 'Na expressão que perrengue, perrengue significa o quê?',
                            'alternativas': ['Um elogio', 'Uma dificuldade', 'Uma festa'],
                            'correta': 1},
                           {'pergunta': 'O que significa dizer que algo é massa, como gíria?',
                            'alternativas': ['Que é legal', 'Que é pesado', 'Que é salgado'],
                            'correta': 0},
                           {'pergunta': 'O que significa dar um perdido em alguém?',
                            'alternativas': ['Entregar um presente',
                                             'Ensinar um caminho',
                                             'Sumir ou evitar contato'],
                            'correta': 2}],
 'Ditados: complete': [{'pergunta': 'Água mole em pedra dura, tanto bate até que...',
                        'alternativas': ['Some', 'Fura', 'Esfria'],
                        'correta': 1},
                       {'pergunta': 'Quem não arrisca, não...',
                        'alternativas': ['Petisca', 'Caminha', 'Conversa'],
                        'correta': 0},
                       {'pergunta': 'De grão em grão, a galinha enche o...',
                        'alternativas': ['Ninho', 'Quintal', 'Papo'],
                        'correta': 2}],
 'Adivinhas: objetos': [{'pergunta': 'O que tem dentes, mas não morde?',
                         'alternativas': ['Pente', 'Sapato', 'Copo'],
                         'correta': 0},
                        {'pergunta': 'O que tem braços, mas não abraça, e pode ficar na sala?',
                         'alternativas': ['Tapete', 'Poltrona', 'Espelho'],
                         'correta': 1},
                        {'pergunta': 'O que tem ponteiros e marca as horas?',
                         'alternativas': ['Caderno', 'Telefone sem relógio', 'Relógio'],
                         'correta': 2}],
 'Lógica: pense rápido': [{'pergunta': 'Se você ultrapassa o segundo colocado numa corrida, fica '
                                       'em qual posição?',
                           'alternativas': ['Primeiro', 'Segundo', 'Terceiro'],
                           'correta': 1},
                          {'pergunta': 'Qual número vem depois: 2, 4, 8, 16...?',
                           'alternativas': ['18', '24', '32'],
                           'correta': 2},
                          {'pergunta': 'Um quilo de algodão e um quilo de ferro: qual pesa mais?',
                           'alternativas': ['Pesam o mesmo', 'O ferro', 'O algodão'],
                           'correta': 0}],
 'Matemática do cotidiano': [{'pergunta': 'Quanto é 25% de 100?',
                              'alternativas': ['25', '50', '75'],
                              'correta': 0},
                             {'pergunta': 'Um produto custa 80 reais e tem desconto de 10 reais. '
                                          'Quanto você paga?',
                              'alternativas': ['60 reais', '70 reais', '90 reais'],
                              'correta': 1},
                             {'pergunta': 'Quanto é metade de 3 horas?',
                              'alternativas': ['30 minutos', '60 minutos', '90 minutos'],
                              'correta': 2}],
 'Brasil: capitais': [{'pergunta': 'Qual é a capital de Pernambuco?',
                       'alternativas': ['Maceió', 'Recife', 'Natal'],
                       'correta': 1},
                      {'pergunta': 'Qual é a capital do Paraná?',
                       'alternativas': ['Curitiba', 'Florianópolis', 'Porto Alegre'],
                       'correta': 0},
                      {'pergunta': 'Qual é a capital do Pará?',
                       'alternativas': ['Manaus', 'Macapá', 'Belém'],
                       'correta': 2}],
 'Mundo: lugares famosos': [{'pergunta': 'Em qual país fica a Torre Eiffel?',
                             'alternativas': ['Itália', 'França', 'Portugal'],
                             'correta': 1},
                            {'pergunta': 'Em qual país fica o Coliseu de Roma?',
                             'alternativas': ['Itália', 'Grécia', 'Espanha'],
                             'correta': 0},
                            {'pergunta': 'Em qual país fica Machu Picchu?',
                             'alternativas': ['Chile', 'México', 'Peru'],
                             'correta': 2}],
 'Bandeiras: reconheça as cores': [{'pergunta': '🌍 Qual país tem uma bandeira branca com um '
                                                'círculo vermelho central?',
                                    'alternativas': ['🇨🇦 Canadá', '🇯🇵 Japão', '🇦🇷 Argentina'],
                                    'correta': 1},
                                   {'pergunta': '🌍 Qual país tem uma folha de bordo na bandeira?',
                                    'alternativas': ['🇨🇦 Canadá', '🇧🇷 Brasil', '🇫🇷 França'],
                                    'correta': 0},
                                   {'pergunta': '🌍 Qual país tem estrelas e listras vermelhas e '
                                                'brancas na bandeira?',
                                    'alternativas': ['🇵🇹 Portugal',
                                                     '🇮🇹 Itália',
                                                     '🇺🇸 Estados Unidos'],
                                    'correta': 2}],
 'Espaço: além da Terra': [{'pergunta': '🚀 Qual destes é o satélite natural da Terra?',
                            'alternativas': ['🌙 Lua', '☀️ Sol', '🪐 Saturno'],
                            'correta': 0},
                           {'pergunta': '🚀 Qual destes é uma estrela?',
                            'alternativas': ['🌍 Terra', '☀️ Sol', '🌙 Lua'],
                            'correta': 1},
                           {'pergunta': '🚀 Qual planeta é famoso por seus grandes anéis?',
                            'alternativas': ['🔴 Marte', '🌍 Terra', '🪐 Saturno'],
                            'correta': 2}],
 'Natureza: água e ar': [{'pergunta': 'Como se chama a passagem da água líquida para vapor?',
                          'alternativas': ['Congelamento', 'Evaporação', 'Fusão'],
                          'correta': 1},
                         {'pergunta': 'Como se chama a água que cai das nuvens em gotas?',
                          'alternativas': ['Chuva', 'Neve', 'Granizo'],
                          'correta': 0},
                         {'pergunta': 'Qual fenômeno forma um arco de cores com luz solar e gotas '
                                      'de água?',
                          'alternativas': ['Terremoto', 'Eclipse', 'Arco-íris'],
                          'correta': 2}],
 'Escola: ciências básicas': [{'pergunta': 'Quantas pernas tem um inseto adulto?',
                               'alternativas': ['Quatro', 'Seis', 'Oito'],
                               'correta': 1},
                              {'pergunta': 'Qual gás é liberado na fotossíntese das plantas?',
                               'alternativas': ['Oxigênio', 'Hélio', 'Metano'],
                               'correta': 0},
                              {'pergunta': 'Qual material é atraído por um ímã comum?',
                               'alternativas': ['Madeira', 'Vidro', 'Ferro'],
                               'correta': 2}],
 'Tecnologia: termos comuns': [{'pergunta': 'O que significa tirar uma captura de tela?',
                                'alternativas': ['Apagar um aplicativo',
                                                 'Salvar uma imagem da tela',
                                                 'Desligar o celular'],
                                'correta': 1},
                               {'pergunta': 'Qual destes é um navegador de internet?',
                                'alternativas': ['Google Chrome', 'Calculadora', 'Gravador de voz'],
                                'correta': 0},
                               {'pergunta': 'Qual recurso permite conectar fones sem fio '
                                            'compatíveis ao celular?',
                                'alternativas': ['Modo avião', 'Lanterna', 'Bluetooth'],
                                'correta': 2}],
 'Cinema: personagens famosos': [{'pergunta': 'Qual personagem é um ogro verde?',
                                  'alternativas': ['Buzz Lightyear', 'Shrek', 'Aladdin'],
                                  'correta': 1},
                                 {'pergunta': 'Qual personagem perde um sapatinho de cristal?',
                                  'alternativas': ['Cinderela', 'Moana', 'Mulan'],
                                  'correta': 0},
                                 {'pergunta': 'Qual personagem é um boneco de madeira cujo nariz '
                                              'cresce ao mentir?',
                                  'alternativas': ['Dumbo', 'Peter Pan', 'Pinóquio'],
                                  'correta': 2}],
 'Desenhos: infância': [{'pergunta': 'Qual personagem mora em um abacaxi no fundo do mar?',
                         'alternativas': ['Pica-Pau', 'Bob Esponja', 'Scooby-Doo'],
                         'correta': 1},
                        {'pergunta': 'Qual personagem é um coelho famoso por gostar de cenouras?',
                         'alternativas': ['Pernalonga', 'Pateta', 'Garfield'],
                         'correta': 0},
                        {'pergunta': 'Qual personagem é um gato laranja apaixonado por lasanha?',
                         'alternativas': ['Snoopy', 'Pluto', 'Garfield'],
                         'correta': 2}],
 'Música: instrumentos': [{'pergunta': '🎵 Qual instrumento tem teclas pretas e brancas?',
                           'alternativas': ['🎹 Piano', '🥁 Tambor', '🎺 Trompete'],
                           'correta': 0},
                          {'pergunta': '🎵 Qual destes é um instrumento de cordas?',
                           'alternativas': ['🥁 Bateria', '🎸 Violão', '🎺 Trompete'],
                           'correta': 1},
                          {'pergunta': '🎵 Qual destes é um instrumento de sopro?',
                           'alternativas': ['🎻 Violino', '🥁 Tambor', '🎺 Trompete'],
                           'correta': 2}],
 'Esportes: além do futebol': [{'pergunta': '🏅 Em qual esporte se usa uma raquete para rebater uma '
                                            'bola sobre a rede?',
                                'alternativas': ['🏀 Basquete', '🎾 Tênis', '🏊 Natação'],
                                'correta': 1},
                               {'pergunta': '🏅 Em qual esporte a cesta é o alvo?',
                                'alternativas': ['🏀 Basquete', '⚽ Futebol', '🏐 Vôlei'],
                                'correta': 0},
                               {'pergunta': '🏅 Qual esporte tem provas de crawl e borboleta?',
                                'alternativas': ['🥊 Boxe', '🎾 Tênis', '🏊 Natação'],
                                'correta': 2}]}

LEGENDAS = {'Futebol: apelidos famosos': 'Futebol: apelidos famosos! 🧠 Você consegue acertar as 3 perguntas? '
                              'Comente quantas acertou e desafie um amigo!\n'
                              '\n'
                              '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Relacionamento: combinados': 'Relacionamento: combinados! 🧠 Você consegue acertar as 3 '
                               'perguntas? Comente quantas acertou e desafie um amigo!\n'
                               '\n'
                               '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Amizade: quem é você no grupo?': 'Amizade: quem é você no grupo?! 🧠 Você consegue acertar as 3 '
                                   'perguntas? Comente quantas acertou e desafie um amigo!\n'
                                   '\n'
                                   '#JuhQuiz #Quiz #Desafio #PerguntasERespostas '
                                   '#ConhecimentosGerais',
 'Frutas: por dentro e por fora': 'Frutas: por dentro e por fora! 🧠 Você consegue acertar as 3 '
                                  'perguntas? Comente quantas acertou e desafie um amigo!\n'
                                  '\n'
                                  '#JuhQuiz #Quiz #Desafio #PerguntasERespostas '
                                  '#ConhecimentosGerais',
 'Animais: habilidades incríveis': 'Animais: habilidades incríveis! 🧠 Você consegue acertar as 3 '
                                   'perguntas? Comente quantas acertou e desafie um amigo!\n'
                                   '\n'
                                   '#JuhQuiz #Quiz #Desafio #PerguntasERespostas '
                                   '#ConhecimentosGerais',
 'Pets: curiosidades': 'Pets: curiosidades! 🧠 Você consegue acertar as 3 perguntas? Comente '
                       'quantas acertou e desafie um amigo!\n'
                       '\n'
                       '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Culinária brasileira': 'Culinária brasileira! 🧠 Você consegue acertar as 3 perguntas? Comente '
                         'quantas acertou e desafie um amigo!\n'
                         '\n'
                         '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Doces: adivinhe o ingrediente': 'Doces: adivinhe o ingrediente! 🧠 Você consegue acertar as 3 '
                                  'perguntas? Comente quantas acertou e desafie um amigo!\n'
                                  '\n'
                                  '#JuhQuiz #Quiz #Desafio #PerguntasERespostas '
                                  '#ConhecimentosGerais',
 'Bebidas e sabores': 'Bebidas e sabores! 🧠 Você consegue acertar as 3 perguntas? Comente quantas '
                      'acertou e desafie um amigo!\n'
                      '\n'
                      '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Objetos de casa': 'Objetos de casa! 🧠 Você consegue acertar as 3 perguntas? Comente quantas '
                    'acertou e desafie um amigo!\n'
                    '\n'
                    '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Português: palavras parecidas': 'Português: palavras parecidas! 🧠 Você consegue acertar as 3 '
                                  'perguntas? Comente quantas acertou e desafie um amigo!\n'
                                  '\n'
                                  '#JuhQuiz #Quiz #Desafio #PerguntasERespostas '
                                  '#ConhecimentosGerais',
 'Português: acerte a escrita': 'Português: acerte a escrita! 🧠 Você consegue acertar as 3 '
                                'perguntas? Comente quantas acertou e desafie um amigo!\n'
                                '\n'
                                '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Inglês: palavras do dia a dia': 'Inglês: palavras do dia a dia! 🧠 Você consegue acertar as 3 '
                                  'perguntas? Comente quantas acertou e desafie um amigo!\n'
                                  '\n'
                                  '#JuhQuiz #Quiz #Desafio #PerguntasERespostas '
                                  '#ConhecimentosGerais',
 'Espanhol: palavras básicas': 'Espanhol: palavras básicas! 🧠 Você consegue acertar as 3 '
                               'perguntas? Comente quantas acertou e desafie um amigo!\n'
                               '\n'
                               '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Gírias: você entende?': 'Gírias: você entende?! 🧠 Você consegue acertar as 3 perguntas? Comente '
                          'quantas acertou e desafie um amigo!\n'
                          '\n'
                          '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Ditados: complete': 'Ditados: complete! 🧠 Você consegue acertar as 3 perguntas? Comente quantas '
                      'acertou e desafie um amigo!\n'
                      '\n'
                      '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Adivinhas: objetos': 'Adivinhas: objetos! 🧠 Você consegue acertar as 3 perguntas? Comente '
                       'quantas acertou e desafie um amigo!\n'
                       '\n'
                       '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Lógica: pense rápido': 'Lógica: pense rápido! 🧠 Você consegue acertar as 3 perguntas? Comente '
                         'quantas acertou e desafie um amigo!\n'
                         '\n'
                         '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Matemática do cotidiano': 'Matemática do cotidiano! 🧠 Você consegue acertar as 3 perguntas? '
                            'Comente quantas acertou e desafie um amigo!\n'
                            '\n'
                            '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Brasil: capitais': 'Brasil: capitais! 🧠 Você consegue acertar as 3 perguntas? Comente quantas '
                     'acertou e desafie um amigo!\n'
                     '\n'
                     '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Mundo: lugares famosos': 'Mundo: lugares famosos! 🧠 Você consegue acertar as 3 perguntas? '
                           'Comente quantas acertou e desafie um amigo!\n'
                           '\n'
                           '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Bandeiras: reconheça as cores': 'Bandeiras: reconheça as cores! 🧠 Você consegue acertar as 3 '
                                  'perguntas? Comente quantas acertou e desafie um amigo!\n'
                                  '\n'
                                  '#JuhQuiz #Quiz #Desafio #PerguntasERespostas '
                                  '#ConhecimentosGerais',
 'Espaço: além da Terra': 'Espaço: além da Terra! 🧠 Você consegue acertar as 3 perguntas? Comente '
                          'quantas acertou e desafie um amigo!\n'
                          '\n'
                          '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Natureza: água e ar': 'Natureza: água e ar! 🧠 Você consegue acertar as 3 perguntas? Comente '
                        'quantas acertou e desafie um amigo!\n'
                        '\n'
                        '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Escola: ciências básicas': 'Escola: ciências básicas! 🧠 Você consegue acertar as 3 perguntas? '
                             'Comente quantas acertou e desafie um amigo!\n'
                             '\n'
                             '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Tecnologia: termos comuns': 'Tecnologia: termos comuns! 🧠 Você consegue acertar as 3 perguntas? '
                              'Comente quantas acertou e desafie um amigo!\n'
                              '\n'
                              '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Cinema: personagens famosos': 'Cinema: personagens famosos! 🧠 Você consegue acertar as 3 '
                                'perguntas? Comente quantas acertou e desafie um amigo!\n'
                                '\n'
                                '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Desenhos: infância': 'Desenhos: infância! 🧠 Você consegue acertar as 3 perguntas? Comente '
                       'quantas acertou e desafie um amigo!\n'
                       '\n'
                       '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Música: instrumentos': 'Música: instrumentos! 🧠 Você consegue acertar as 3 perguntas? Comente '
                         'quantas acertou e desafie um amigo!\n'
                         '\n'
                         '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais',
 'Esportes: além do futebol': 'Esportes: além do futebol! 🧠 Você consegue acertar as 3 perguntas? '
                              'Comente quantas acertou e desafie um amigo!\n'
                              '\n'
                              '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #ConhecimentosGerais'}
