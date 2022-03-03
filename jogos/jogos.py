import adivinhacao
import forca
import jokenpo


def escolhe_jogo():

    print('#####################################')
    print('######## ESCOLHA O SEU JOGO #########')
    print('#####################################')
    print('########## 1. ADIVINHAÇÃO ###########')
    print('############# 2. FORCA ##############')
    print('############ 3. JOKENPO #############')
    print('#####################################')

    jogo = int(input('Digite o valor do jogo desejado - '))

    if (jogo == 1):
        print('Jogando adivinhação ...')
        adivinhacao.jogar()

    if (jogo == 2):
        print('jogando forca ...')
        forca.jogar()

    if (jogo == 3):
        print('Jogando jokenpo ...')
        jokenpo.jogar()

    print('FIM DO JOGO')


if (__name__ == "__main__"):
    escolhe_jogo()
