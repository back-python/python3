import adivinhacao
import forca


def escolhe_jogo():

    print('#####################################')
    print('######## ESCOLHA O SEU JOGO #########')
    print('#####################################')
    print('########## 1. ADIVINHAÇÃO ###########')
    print('############# 2. FORCA ##############')
    print('#####################################')

    jogo = int(input('Digite o valor do jogo desejado - '))

    if (jogo == 1):
        print('Jogando adivinhação ...')
        adivinhacao.jogar()

    if (jogo == 2):
        print('jogando forca ...')
        forca.jogar()

    print('FIM DO JOGO')


if (__name__ == "__main__"):
    escolhe_jogo()
