import random


def jogar():

    print('######################################')
    print('######## JOGO DA ADIVINHAÇÃO #########')
    print('######################################')
    print('############ DIFICULDADE #############')
    print('######### 1. ENCHER LINGUIÇA #########')
    print('############ 2. ADIVINHÃO ############')
    print('############ 3. MÃE DINÁ #############')
    print('######################################')

    nivel = int(input('Digite o nível desejado - '))

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    if nivel == 1:
        tentativas = 13
    if nivel == 2:
        tentativas = 7
    if nivel == 3:
        tentativas = 4

    while (tentativas != 0):
        print('Você possui {} tentativas'.format(tentativas))
        chute = int(input('Digite um palpite entre 1 e 100 - '))

        if chute > 100 or chute < 1:
            print('Número inválido')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print('VOCÊ ACERTOU! PARABÉNS!\n')
            pontos += 50 * nivel
            ganhou = True
            break

        else:
            print('VOCÊ ERROU!')
            tentativas -= 1

            pontos_perdidos = abs(chute - numero_secreto)

            pontos -= pontos_perdidos * tentativas

            if maior:
                print('Seu chute foi MAIOR do que o número secreto!\n')
            else:
                print('Seu chute foi MENOR do que o número secreto!\n')

    if tentativas == 0:
        print('VOCÊ PERDEU! O número secreto era {}!'.format(numero_secreto))

    if pontos < 0:
        pontos = 0
    elif pontos > 1000:
        pontos = 1000
        print('COM ESSA PONTUAÇÃO VOCÊ PODIA JOGAR NA MEGA :D')

    print('Sua pontuaçao final foi: ', pontos)
    print('FIM DO JOGO!')


if(__name__ == "__main__"):
    jogar()
