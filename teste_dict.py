import random

states_capitals = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas',
    'Distrito Federal': 'Brasília'
    }

# Gerar 35 arquivos de provas
#for quiz_num in range(35):
    # Cria os arquivos com as provas e os gabaritos das respostas
    #quiz_file = open('states_capitals_quiz%s.txt' % (quiz_num + 1), 'w')
    #quiz_answer_file = open('states_capitals_answer%s.txt' % (quiz_num + 1), 'w')

    # Escreve o cabeçalho das provas
    #quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    #quiz_file.write(('' * 20) + 'State Capitals Quiz (Form %s)' % (quiz_num + 1))
    #quiz_file.write('\n\n')

    # Embaralha a ordem dos estados
states = list(states_capitals.keys()) # Transforma o dicionário em lista
random.shuffle(states) # Embaralha a lista

# Percorrer os 25 estados, criando uma pergunta para cada
for question_num in range(27):
    #Obtém respostas corretas e incorretas
    correct_answer = states_capitals[states[question_num]] # Busca a resposta correta
    wrong_answers = list(states_capitals.values()) # Buscando todos os valores do dicionario
    del wrong_answers[wrong_answers.index(correct_answer)] # Deletando a resposta correta
    wrong_answers = random.sample(wrong_answers, 3) # Buscando 3 valores aleatórios
    answer_options = wrong_answers + [correct_answer] # Criando as opções da questão
    random.shuffle(answer_options) # Embaralhando as opções

print(answer_options.index(correct_answer))

