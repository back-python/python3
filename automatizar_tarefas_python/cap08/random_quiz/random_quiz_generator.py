#! /usr/bin/python3
# random_quiz_generator.py - Cria provas individuais juntamente com os gabaritos

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
for quiz_num in range(35):
    # Cria os arquivos com as provas e os gabaritos das respostas
    quiz_file = open('provas/prova_estados_capitaos%s.txt' % (quiz_num + 1), 'w')
    quiz_answer_file = open('gabaritos/gabarito_estados_capitais%s.txt' % (quiz_num + 1), 'w')

    # Escreve o cabeçalho das provas
    quiz_file.write('Nome:\n\nData:\n\nTurma:\n\n')
    quiz_file.write((' ' * 20) + 'Prova sobre os estados e capitais brasileiras (Modelo %s)' % (quiz_num + 1))
    quiz_file.write('\n')

    # Embaralha a ordem dos estados
    states = list(states_capitals.keys()) # Buscando os nomes dos estados do dicionário e armazenando em uma lista
    random.shuffle(states) # Embaralhando a lista com os estados

    # Percorrer os 27 estados, criando uma pergunta para cada
    for question_num in range(27):
        #Obtém respostas corretas e incorretas
        correct_answer = states_capitals[states[question_num]] # A resposta correta
        wrong_answers = list(states_capitals.values()) # Buscando todas as capitais e transformando em lista
        del wrong_answers[wrong_answers.index(correct_answer)] # Deletando a resposta correta da lista
        wrong_answers = random.sample(wrong_answers, 3) # Sorteando 3 respostas da lista
        answer_options = wrong_answers + [correct_answer] # Montando a questão
        random.shuffle(answer_options) # Embaralhando opções

        # Grava a pergunta e as opções de resposta no arquivo da prova
        quiz_file.write('%s. Qual a capital da(o) %s?\n' % (question_num + 1, states[question_num]))
        for i in range(4):
            quiz_file.write(' %s. %s\n' % ('ABCD'[i], answer_options[i]))
        quiz_file.write('\n')

        # Grava o gabarito em um arquivo
        quiz_answer_file.write('%s. %s\n' % (question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))

    quiz_file.close()
    quiz_answer_file.close()
    

    
