# Juh Quiz — 30 vídeos, 90 perguntas; imagens opcionais.
# correta: 0=A, 1=B, 2=C.
# Nas perguntas com emojis, as três alternativas também têm emojis.
# Use com gerar_quiz.py e requirements.txt atualizados para emojis coloridos.

QUIZZES = {'Futebol: regras e curiosidades': [{'pergunta': '⚽ Quantos jogadores cada equipe tem em campo no '
                                                 'início de uma partida de futebol?',
                                     'alternativas': ['⚽ 9', '⚽ 11', '⚽ 13'],
                                     'correta': 1},
                                    {'pergunta': '🏆 Qual seleção venceu a Copa do Mundo masculina de '
                                                 '2002?',
                                     'alternativas': ['🇧🇷 Brasil', '🇩🇪 Alemanha', '🇦🇷 Argentina'],
                                     'correta': 0},
                                    {'pergunta': 'Qual jogador brasileiro ficou conhecido como Rei do '
                                                 'Futebol?',
                                     'alternativas': ['Romário', 'Ronaldo', 'Pelé'],
                                     'correta': 2}],
 'Relacionamento: diálogo e respeito': [{'pergunta': 'Qual atitude demonstra respeito aos limites do '
                                                     'parceiro?',
                                         'alternativas': ['Insistir até conseguir',
                                                          'Aceitar quando ele diz não',
                                                          'Ignorar o assunto'],
                                         'correta': 1},
                                        {'pergunta': 'Durante uma discussão, qual atitude favorece o '
                                                     'diálogo?',
                                         'alternativas': ['Escutar sem interromper',
                                                          'Gritar mais alto',
                                                          'Fazer ameaças'],
                                         'correta': 0},
                                        {'pergunta': 'Qual atitude respeita a privacidade no '
                                                     'relacionamento?',
                                         'alternativas': ['Exigir todas as senhas',
                                                          'Ler mensagens escondido',
                                                          'Conversar sobre limites'],
                                         'correta': 2}],
 'Primeira vez: consentimento e proteção': [{'pergunta': 'É possível engravidar na primeira relação '
                                                         'vaginal sem contracepção?',
                                             'alternativas': ['Só na segunda vez',
                                                              'Sim, é possível',
                                                              'Nunca'],
                                             'correta': 1},
                                            {'pergunta': 'O consentimento pode ser retirado durante uma '
                                                         'relação?',
                                             'alternativas': ['Sim, a qualquer momento',
                                                              'Não, se já começou',
                                                              'Só no dia seguinte'],
                                             'correta': 0},
                                            {'pergunta': 'Qual método ajuda a prevenir gravidez e '
                                                         'reduzir o risco de ISTs?',
                                             'alternativas': ['Coito interrompido',
                                                              'Tabelinha',
                                                              'Preservativo'],
                                             'correta': 2}],
 'Menstruação: mitos e verdades': [{'pergunta': 'Qual é o primeiro dia do ciclo menstrual?',
                                    'alternativas': ['O dia da ovulação',
                                                     'O primeiro dia da menstruação',
                                                     'O último dia da menstruação'],
                                    'correta': 1},
                                   {'pergunta': 'O ciclo menstrual precisa durar exatamente 28 dias em '
                                                'todas as pessoas?',
                                    'alternativas': ['Não, a duração varia',
                                                     'Sim, sempre',
                                                     'Só no inverno'],
                                    'correta': 0},
                                   {'pergunta': 'A menstruação está relacionada à eliminação de qual '
                                                'tecido?',
                                    'alternativas': ['Tecido dos pulmões',
                                                     'Tecido dos rins',
                                                     'Revestimento do útero'],
                                    'correta': 2}],
 'Frutas: descubra qual é': [{'pergunta': '🍽️ Qual fruta é a base tradicional do guacamole?',
                              'alternativas': ['🥑 Abacate', '🍎 Maçã', '🍇 Uva'],
                              'correta': 0},
                             {'pergunta': '🍽️ Qual fruta tem casca marrom com pelos e polpa geralmente '
                                          'verde?',
                              'alternativas': ['🥭 Manga', '🥝 Kiwi', '🍊 Laranja'],
                              'correta': 1},
                             {'pergunta': '🍽️ Qual alimento é uma uva desidratada?',
                              'alternativas': ['🍑 Damasco seco', '🟣 Ameixa seca', '🍇 Uva-passa'],
                              'correta': 2}],
 'Animais: curiosidades surpreendentes': [{'pergunta': '🐾 Qual animal tem três corações?',
                                           'alternativas': ['🐙 Polvo', '🐢 Tartaruga', '🐊 Crocodilo'],
                                           'correta': 0},
                                          {'pergunta': '🐾 Qual destes mamíferos põe ovos?',
                                           'alternativas': ['🦘 Canguru', '🐾 Ornitorrinco', '🦦 Lontra'],
                                           'correta': 1},
                                          {'pergunta': '🐦 Qual ave consegue voar para trás?',
                                           'alternativas': ['🐦 Avestruz', '🐧 Pinguim', '🐦 Beija-flor'],
                                           'correta': 2}],
 'Corpo humano': [{'pergunta': '🧍 Qual órgão bombeia o sangue pelo corpo?',
                   'alternativas': ['🫀 Coração', '🧍 Estômago', '🫘 Rim'],
                   'correta': 0},
                  {'pergunta': 'Qual é o maior órgão do corpo humano?',
                   'alternativas': ['Fígado', 'Pele', 'Pulmão'],
                   'correta': 1},
                  {'pergunta': 'Quantas câmaras tem o coração humano?',
                   'alternativas': ['Duas', 'Seis', 'Quatro'],
                   'correta': 2}],
 'Gravidez: mitos e verdades': [{'pergunta': 'O tamanho da barriga revela com certeza se o bebê é '
                                             'menino ou menina?',
                                 'alternativas': ['Sim, sempre', 'Não', 'Só no primeiro mês'],
                                 'correta': 1},
                                {'pergunta': 'Um teste de gravidez procura detectar qual hormônio?',
                                 'alternativas': ['hCG', 'Insulina', 'Melatonina'],
                                 'correta': 0},
                                {'pergunta': 'Uma menstruação atrasada, sozinha, confirma gravidez?',
                                 'alternativas': ['Sim, em todos os casos',
                                                  'Só depois dos 30 anos',
                                                  'Não, pode ter outras causas'],
                                 'correta': 2}],
 'Métodos contraceptivos': [{'pergunta': 'A pílula anticoncepcional protege contra ISTs?',
                             'alternativas': ['Sim, todas', 'Não', 'Só contra HIV'],
                             'correta': 1},
                            {'pergunta': 'DIU significa o quê?',
                             'alternativas': ['Dispositivo intrauterino',
                                              'Dose interna única',
                                              'Diagnóstico individual urinário'],
                             'correta': 0},
                            {'pergunta': 'A contracepção de emergência substitui o preservativo na '
                                         'prevenção de ISTs?',
                             'alternativas': ['Sim, totalmente', 'Só no primeiro uso', 'Não'],
                             'correta': 2}],
 'Beijo e atração: curiosidades': [{'pergunta': 'Antes de beijar alguém, qual atitude respeita o '
                                                'consentimento?',
                                    'alternativas': ['Insistir sem perguntar',
                                                     'Confirmar se a pessoa quer',
                                                     'Beijar de surpresa sempre'],
                                    'correta': 1},
                                   {'pergunta': 'Um encontro cria obrigação de beijar?',
                                    'alternativas': ['Não', 'Sim, se foi pago', 'Sim, se houve elogio'],
                                    'correta': 0},
                                   {'pergunta': 'O que significa atração recíproca?',
                                    'alternativas': ['Só uma pessoa tem interesse',
                                                     'Todos sentem a mesma coisa',
                                                     'O interesse é mútuo'],
                                    'correta': 2}],
 'Amizade: situações do cotidiano': [{'pergunta': 'Um amigo pede para não divulgar uma informação '
                                                  'pessoal. Qual atitude respeita isso?',
                                      'alternativas': ['Manter a privacidade',
                                                       'Publicar sem o nome',
                                                       'Contar ao grupo'],
                                      'correta': 0},
                                     {'pergunta': 'Qual atitude demonstra escuta quando um amigo '
                                                  'desabafa?',
                                      'alternativas': ['Mudar de assunto',
                                                       'Ouvir com atenção',
                                                       'Rir do problema'],
                                      'correta': 1},
                                     {'pergunta': 'Um amigo recusa um convite. Qual resposta respeita a '
                                                  'decisão?',
                                      'alternativas': ['Fazer chantagem',
                                                       'Cobrar uma explicação sempre',
                                                       'Aceitar a recusa'],
                                      'correta': 2}],
 'Emoções e sentimentos': [{'pergunta': 'Qual palavra descreve tentar compreender o que outra pessoa '
                                        'sente?',
                            'alternativas': ['Empatia', 'Competição', 'Indiferença'],
                            'correta': 0},
                           {'pergunta': 'É possível sentir alegria e tristeza ao mesmo tempo?',
                            'alternativas': ['Nunca', 'Sim', 'Só em sonhos'],
                            'correta': 1},
                           {'pergunta': 'Qual frase expressa um sentimento sem acusar outra pessoa?',
                            'alternativas': ['Você estraga tudo',
                                             'Você nunca presta atenção',
                                             'Eu me senti triste'],
                            'correta': 2}],
 'Alimentos e culinária': [{'pergunta': 'O acarajé é especialmente associado a qual estado?',
                            'alternativas': ['Bahia', 'Paraná', 'Goiás'],
                            'correta': 0},
                           {'pergunta': '🍽️ Qual ingrediente costuma ser a base da tapioca?',
                            'alternativas': ['🌾 Trigo', '🌱 Mandioca', '🍚 Arroz'],
                            'correta': 1},
                           {'pergunta': 'O pão de queijo é especialmente associado a qual estado?',
                            'alternativas': ['Amazonas', 'Pernambuco', 'Minas Gerais'],
                            'correta': 2}],
 'Doces e sobremesas': [{'pergunta': '🍫 Qual ingrediente dá o sabor tradicional de chocolate ao '
                                     'brigadeiro?',
                         'alternativas': ['🍫 Chocolate ou cacau', '☕ Café', '🌿 Canela'],
                         'correta': 0},
                        {'pergunta': 'Qual doce brasileiro é tradicionalmente feito com amendoim?',
                         'alternativas': ['Quindim', 'Paçoca', 'Manjar'],
                         'correta': 1},
                        {'pergunta': 'O nome Romeu e Julieta costuma indicar qual combinação?',
                         'alternativas': ['Banana e chocolate', 'Morango e creme', 'Queijo e goiabada'],
                         'correta': 2}],
 'Filmes famosos': [{'pergunta': '🎬 Woody é personagem de qual animação?',
                     'alternativas': ['🤠 Toy Story', '🚗 Carros', '🐠 Procurando Nemo'],
                     'correta': 0},
                    {'pergunta': 'Simba aparece em qual filme?',
                     'alternativas': ['Tarzan', 'O Rei Leão', 'Aladdin'],
                     'correta': 1},
                    {'pergunta': 'Em qual escola de magia Harry Potter estuda?',
                     'alternativas': ['Nárnia', 'Nevermore', 'Hogwarts'],
                     'correta': 2}],
 'Séries e personagens': [{'pergunta': 'Em Friends, qual personagem é chef de cozinha?',
                           'alternativas': ['Monica', 'Rachel', 'Phoebe'],
                           'correta': 0},
                          {'pergunta': 'Em Stranger Things, qual personagem tem poderes telecinéticos?',
                           'alternativas': ['Dustin', 'Eleven', 'Steve'],
                           'correta': 1},
                          {'pergunta': 'Em Breaking Bad, Walter White era professor de qual disciplina?',
                           'alternativas': ['História', 'Geografia', 'Química'],
                           'correta': 2}],
 'Novelas brasileiras': [{'pergunta': 'Carminha é uma personagem de qual novela?',
                          'alternativas': ['Avenida Brasil', 'O Clone', 'Cheias de Charme'],
                          'correta': 0},
                         {'pergunta': 'Jade e Lucas são personagens de qual novela?',
                          'alternativas': ['Pantanal', 'O Clone', 'Rebelde'],
                          'correta': 1},
                         {'pergunta': 'Maria da Paz é a protagonista de qual novela?',
                          'alternativas': ['A Favorita', 'Senhora do Destino', 'A Dona do Pedaço'],
                          'correta': 2}],
 'Música brasileira': [{'pergunta': 'Quem ficou conhecido como Rei do Baião?',
                        'alternativas': ['Luiz Gonzaga', 'Tim Maia', 'Gilberto Gil'],
                        'correta': 0},
                       {'pergunta': 'Qual cantora ficou conhecida como Rainha do Rock Brasileiro?',
                        'alternativas': ['Gal Costa', 'Rita Lee', 'Alcione'],
                        'correta': 1},
                       {'pergunta': '🎵 Qual destes instrumentos é muito associado ao samba?',
                        'alternativas': ['🎻 Violino', '🎶 Harpa', '🥁 Pandeiro'],
                        'correta': 2}],
 'Complete a letra: cantigas populares': [{'pergunta': 'Complete a cantiga: Ciranda, cirandinha, vamos '
                                                       'todos...',
                                           'alternativas': ['Cirandar', 'Cozinhar', 'Estudar'],
                                           'correta': 0},
                                          {'pergunta': 'Complete a cantiga: Se esta rua, se esta rua '
                                                       'fosse...',
                                           'alternativas': ['Nova', 'Minha', 'Longa'],
                                           'correta': 1},
                                          {'pergunta': 'Complete a cantiga: O cravo brigou com a...',
                                           'alternativas': ['Violeta', 'Margarida', 'Rosa'],
                                           'correta': 2}],
 'Gírias nordestinas': [{'pergunta': 'Na expressão nordestina, uma pessoa arretada pode ser alguém...',
                         'alternativas': ['Muito bom ou admirável', 'Sempre distraído', 'Sem coragem'],
                         'correta': 0},
                        {'pergunta': 'Em uma expressão comum, cabra da peste pode significar alguém...',
                         'alternativas': ['Sonolento', 'Valente ou corajoso', 'Sempre gripado'],
                         'correta': 1},
                        {'pergunta': 'Qual expressão nordestina pode indicar surpresa?',
                         'alternativas': ['Merci', 'Hello', 'Oxente'],
                         'correta': 2}],
 'Complete o ditado popular': [{'pergunta': 'Água mole em pedra dura...',
                                'alternativas': ['Tanto bate até que fura',
                                                 'Nunca encontra saída',
                                                 'Vira água de chuva'],
                                'correta': 0},
                               {'pergunta': 'Quem não tem cão...',
                                'alternativas': ['Compra um cavalo',
                                                 'Caça com gato',
                                                 'Fica sem passeio'],
                                'correta': 1},
                               {'pergunta': 'Antes tarde...',
                                'alternativas': ['Do que chegar cedo', 'Do que esperar', 'Do que nunca'],
                                'correta': 2}],
 'Português: qual é o correto?': [{'pergunta': 'Qual é o plural de cidadão?',
                                   'alternativas': ['Cidadãos', 'Cidadões', 'Cidadães'],
                                   'correta': 0},
                                  {'pergunta': 'Qual palavra indica uma ação?',
                                   'alternativas': ['Bonito', 'Correr', 'Mesa'],
                                   'correta': 1},
                                  {'pergunta': 'Qual é o antônimo de quente?',
                                   'alternativas': ['Grande', 'Alto', 'Frio'],
                                   'correta': 2}],
 'Inglês do dia a dia': [{'pergunta': '🌎 Como se diz maçã em inglês?',
                          'alternativas': ['🍎 Apple', '🍊 Orange', '🍇 Grape'],
                          'correta': 0},
                         {'pergunta': '📚 O que significa book em português?',
                          'alternativas': ['🪑 Mesa', '📖 Livro', '🖊️ Caneta'],
                          'correta': 1},
                         {'pergunta': 'Como se diz obrigado em inglês?',
                          'alternativas': ['Good night', 'See you', 'Thank you'],
                          'correta': 2}],
 'Geografia do Brasil': [{'pergunta': 'Qual é a capital do Brasil?',
                          'alternativas': ['Brasília', 'São Paulo', 'Rio de Janeiro'],
                          'correta': 0},
                         {'pergunta': '🗺️ Em qual região fica a Paraíba?',
                          'alternativas': ['🧭 Sul', '🧭 Nordeste', '🧭 Centro-Oeste'],
                          'correta': 1},
                         {'pergunta': 'Qual oceano banha o litoral brasileiro?',
                          'alternativas': ['Pacífico', 'Índico', 'Atlântico'],
                          'correta': 2}],
 'Bandeiras e países': [{'pergunta': '🏳️ Qual país tem uma bandeira branca com um círculo vermelho?',
                         'alternativas': ['🇯🇵 Japão', '🇨🇦 Canadá', '🇲🇽 México'],
                         'correta': 0},
                        {'pergunta': 'Qual símbolo aparece na bandeira do Canadá?',
                         'alternativas': ['Uma águia', 'Uma folha de bordo', 'Uma lua'],
                         'correta': 1},
                        {'pergunta': 'Qual país tem uma bandeira nacional que não é retangular?',
                         'alternativas': ['Butão', 'Japão', 'Nepal'],
                         'correta': 2}],
 'Espaço e planetas': [{'pergunta': '🪐 Qual planeta é conhecido como Planeta Vermelho?',
                        'alternativas': ['🪐 Marte', '🪐 Vênus', '🪐 Netuno'],
                        'correta': 0},
                       {'pergunta': '🪐 Qual é o maior planeta do Sistema Solar?',
                        'alternativas': ['🌍 Terra', '🪐 Júpiter', '🪐 Saturno'],
                        'correta': 1},
                       {'pergunta': '⭐ Qual é a estrela mais próxima da Terra?',
                        'alternativas': ['⭐ Sirius', '⭐ Vega', '☀️ Sol'],
                        'correta': 2}],
 'Tecnologia e celular': [{'pergunta': 'Para que serve o modo avião no celular?',
                           'alternativas': ['Desativar comunicações sem fio, conforme a configuração',
                                            'Carregar mais rápido sempre',
                                            'Aumentar o armazenamento'],
                           'correta': 0},
                          {'pergunta': '📱 O que é uma cópia de segurança dos arquivos?',
                           'alternativas': ['📩 Spam', '💾 Backup', '📶 Bluetooth'],
                           'correta': 1},
                          {'pergunta': 'Qual cuidado ajuda a proteger uma conta?',
                           'alternativas': ['Divulgar a senha',
                                            'Reutilizar senhas em tudo',
                                            'Ativar autenticação em duas etapas'],
                           'correta': 2}],
 'Desafios de lógica': [{'pergunta': 'Se você ultrapassa quem está em segundo lugar, em que posição '
                                     'fica?',
                         'alternativas': ['Em segundo', 'Em primeiro', 'Em terceiro'],
                         'correta': 0},
                        {'pergunta': 'Dois pais e dois filhos são apenas três pessoas. Quem podem ser?',
                         'alternativas': ['Três irmãos', 'Avô, pai e filho', 'Dois primos e um amigo'],
                         'correta': 1},
                        {'pergunta': 'Quanto é a metade de 50?',
                         'alternativas': ['15', '20', '25'],
                         'correta': 2}],
 'O que é, o que é?': [{'pergunta': '🤔 Tem dentes, mas não morde. Qual opção se encaixa?',
                        'alternativas': ['🪮 Pente', '⚽ Bola', '🥤 Copo'],
                        'correta': 0},
                       {'pergunta': 'Quanto mais se tira, maior fica. O que é?',
                        'alternativas': ['Árvore', 'Buraco', 'Sombra'],
                        'correta': 1},
                       {'pergunta': '🤔 Tem folhas, mas não é árvore. O que é?',
                        'alternativas': ['🪨 Pedra', '👟 Sapato', '📖 Livro'],
                        'correta': 2}],
 'História e invenções': [{'pergunta': 'Quem desenvolveu a prensa de tipos móveis na Europa no século '
                                       'XV?',
                           'alternativas': ['Johannes Gutenberg', 'Isaac Newton', 'Charles Darwin'],
                           'correta': 0},
                          {'pergunta': '🔎 Qual invenção permite observar objetos distantes no céu?',
                           'alternativas': ['🔬 Microscópio', '🔭 Telescópio', '🌡️ Termômetro'],
                           'correta': 1},
                          {'pergunta': '🧭 Qual instrumento ajudou navegadores a identificar os pontos '
                                       'cardeais?',
                           'alternativas': ['⚖️ Balança', '⌛ Ampulheta', '🧭 Bússola'],
                           'correta': 2}]}

LEGENDAS = {'Futebol: regras e curiosidades': 'Futebol: regras e curiosidades: você acerta as 3 perguntas? Teste '
                                   'seus conhecimentos, comente quantas acertou e desafie alguém!\n'
                                   '\n'
                                   '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Futebol',
 'Relacionamento: diálogo e respeito': 'Relacionamento: diálogo e respeito: você acerta as 3 perguntas? '
                                       'Teste seus conhecimentos, comente quantas acertou e desafie '
                                       'alguém!\n'
                                       '\n'
                                       '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Relacionamento',
 'Primeira vez: consentimento e proteção': 'Primeira vez: consentimento e proteção: você acerta as 3 '
                                           'perguntas? Teste seus conhecimentos, comente quantas '
                                           'acertou e desafie alguém! Conteúdo educativo sobre saúde '
                                           'sexual e reprodutiva.\n'
                                           '\n'
                                           '#JuhQuiz #Quiz #Desafio #PerguntasERespostas '
                                           '#EducacaoSexual',
 'Menstruação: mitos e verdades': 'Menstruação: mitos e verdades: você acerta as 3 perguntas? Teste '
                                  'seus conhecimentos, comente quantas acertou e desafie alguém! '
                                  'Conteúdo educativo sobre saúde sexual e reprodutiva.\n'
                                  '\n'
                                  '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Menstruacao',
 'Frutas: descubra qual é': 'Frutas: descubra qual é: você acerta as 3 perguntas? Teste seus '
                            'conhecimentos, comente quantas acertou e desafie alguém!\n'
                            '\n'
                            '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Frutas',
 'Animais: curiosidades surpreendentes': 'Animais: curiosidades surpreendentes: você acerta as 3 '
                                         'perguntas? Teste seus conhecimentos, comente quantas acertou '
                                         'e desafie alguém!\n'
                                         '\n'
                                         '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Animais',
 'Corpo humano': 'Corpo humano: você acerta as 3 perguntas? Teste seus conhecimentos, comente quantas '
                 'acertou e desafie alguém!\n'
                 '\n'
                 '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #CorpoHumano',
 'Gravidez: mitos e verdades': 'Gravidez: mitos e verdades: você acerta as 3 perguntas? Teste seus '
                               'conhecimentos, comente quantas acertou e desafie alguém! Conteúdo '
                               'educativo sobre saúde sexual e reprodutiva.\n'
                               '\n'
                               '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Gravidez',
 'Métodos contraceptivos': 'Métodos contraceptivos: você acerta as 3 perguntas? Teste seus '
                           'conhecimentos, comente quantas acertou e desafie alguém! Conteúdo educativo '
                           'sobre saúde sexual e reprodutiva.\n'
                           '\n'
                           '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Contracepcao',
 'Beijo e atração: curiosidades': 'Beijo e atração: curiosidades: você acerta as 3 perguntas? Teste '
                                  'seus conhecimentos, comente quantas acertou e desafie alguém!\n'
                                  '\n'
                                  '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Consentimento',
 'Amizade: situações do cotidiano': 'Amizade: situações do cotidiano: você acerta as 3 perguntas? Teste '
                                    'seus conhecimentos, comente quantas acertou e desafie alguém!\n'
                                    '\n'
                                    '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Amizade',
 'Emoções e sentimentos': 'Emoções e sentimentos: você acerta as 3 perguntas? Teste seus conhecimentos, '
                          'comente quantas acertou e desafie alguém!\n'
                          '\n'
                          '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Emocoes',
 'Alimentos e culinária': 'Alimentos e culinária: você acerta as 3 perguntas? Teste seus conhecimentos, '
                          'comente quantas acertou e desafie alguém!\n'
                          '\n'
                          '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Culinaria',
 'Doces e sobremesas': 'Doces e sobremesas: você acerta as 3 perguntas? Teste seus conhecimentos, '
                       'comente quantas acertou e desafie alguém!\n'
                       '\n'
                       '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Doces',
 'Filmes famosos': 'Filmes famosos: você acerta as 3 perguntas? Teste seus conhecimentos, comente '
                   'quantas acertou e desafie alguém!\n'
                   '\n'
                   '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Cinema',
 'Séries e personagens': 'Séries e personagens: você acerta as 3 perguntas? Teste seus conhecimentos, '
                         'comente quantas acertou e desafie alguém!\n'
                         '\n'
                         '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Series',
 'Novelas brasileiras': 'Novelas brasileiras: você acerta as 3 perguntas? Teste seus conhecimentos, '
                        'comente quantas acertou e desafie alguém!\n'
                        '\n'
                        '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Novelas',
 'Música brasileira': 'Música brasileira: você acerta as 3 perguntas? Teste seus conhecimentos, comente '
                      'quantas acertou e desafie alguém!\n'
                      '\n'
                      '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #MusicaBrasileira',
 'Complete a letra: cantigas populares': 'Complete a letra: cantigas populares: você acerta as 3 '
                                         'perguntas? Teste seus conhecimentos, comente quantas acertou '
                                         'e desafie alguém!\n'
                                         '\n'
                                         '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Cantigas',
 'Gírias nordestinas': 'Gírias nordestinas: você acerta as 3 perguntas? Teste seus conhecimentos, '
                       'comente quantas acertou e desafie alguém!\n'
                       '\n'
                       '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Nordeste',
 'Complete o ditado popular': 'Complete o ditado popular: você acerta as 3 perguntas? Teste seus '
                              'conhecimentos, comente quantas acertou e desafie alguém!\n'
                              '\n'
                              '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #DitadosPopulares',
 'Português: qual é o correto?': 'Português: qual é o correto?: você acerta as 3 perguntas? Teste seus '
                                 'conhecimentos, comente quantas acertou e desafie alguém!\n'
                                 '\n'
                                 '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Portugues',
 'Inglês do dia a dia': 'Inglês do dia a dia: você acerta as 3 perguntas? Teste seus conhecimentos, '
                        'comente quantas acertou e desafie alguém!\n'
                        '\n'
                        '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Ingles',
 'Geografia do Brasil': 'Geografia do Brasil: você acerta as 3 perguntas? Teste seus conhecimentos, '
                        'comente quantas acertou e desafie alguém!\n'
                        '\n'
                        '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Geografia',
 'Bandeiras e países': 'Bandeiras e países: você acerta as 3 perguntas? Teste seus conhecimentos, '
                       'comente quantas acertou e desafie alguém!\n'
                       '\n'
                       '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Paises',
 'Espaço e planetas': 'Espaço e planetas: você acerta as 3 perguntas? Teste seus conhecimentos, comente '
                      'quantas acertou e desafie alguém!\n'
                      '\n'
                      '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Espaco',
 'Tecnologia e celular': 'Tecnologia e celular: você acerta as 3 perguntas? Teste seus conhecimentos, '
                         'comente quantas acertou e desafie alguém!\n'
                         '\n'
                         '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Tecnologia',
 'Desafios de lógica': 'Desafios de lógica: você acerta as 3 perguntas? Teste seus conhecimentos, '
                       'comente quantas acertou e desafie alguém!\n'
                       '\n'
                       '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Logica',
 'O que é, o que é?': 'O que é, o que é?: você acerta as 3 perguntas? Teste seus conhecimentos, comente '
                      'quantas acertou e desafie alguém!\n'
                      '\n'
                      '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Adivinhas',
 'História e invenções': 'História e invenções: você acerta as 3 perguntas? Teste seus conhecimentos, '
                         'comente quantas acertou e desafie alguém!\n'
                         '\n'
                         '#JuhQuiz #Quiz #Desafio #PerguntasERespostas #Historia'}

FONTES_SAUDE = {'Primeira vez: consentimento e proteção': ['https://www.forumhealthcentre.nhs.uk/your-health/young-people-s-health',
                                            'https://www.who.int/news-room/questions-and-answers/item/condoms'],
 'Menstruação: mitos e verdades': ['https://www.nhs.uk/conditions/periods/fertility-in-the-menstrual-cycle/',
                                   'https://www.nhs.uk/conditions/periods/period-problems/'],
 'Gravidez: mitos e verdades': ['https://www.nhs.uk/pregnancy/trying-for-a-baby/doing-a-pregnancy-test/'],
 'Métodos contraceptivos': ['https://www.who.int/news-room/questions-and-answers/item/condoms',
                            'https://www.who.int/news-room/fact-sheets/detail/emergency-contraception']}
