from random import randrange

def jogar():

    exibe_menu()

    # O programa pede para repetir a categoria, até que ela seja válida
    cat = False

    # Preenchimento e validação de categoria
    while not cat:
        categoria = input('Digite a categoria desejada: ')

        cat = valida_categoria(categoria)

        if not cat:
            print('Categoria inválida!')

    # A conversão não foi feita antes, por que pra satisfazer a validação do programa
    # é preciso mandar uma string para o validador
    categoria = int(categoria)
    palavra_secreta = busca_palavra(categoria) if categoria > 0 else input('Digite uma palavra: ').upper()

    # iniciando uma váriavel com base no tamanho de outra
    letras_acertadas = ['_' for letra in palavra_secreta]

    ganhou = False
    tentativas = 7

    print(exibe_letras_acertadas(letras_acertadas))

    while not ganhou and tentativas > 0:

        letra = input('Digite uma letra: ').upper().strip()

        if valida_letra(letra):
            # Se acertar, preenche letra
            preenche_letra_acertada(letra, palavra_secreta, letras_acertadas)

            # Tirar tentativa, se errar
            if letra not in palavra_secreta:
                tentativas -= 1
                desenha_forca(tentativas)
                #print(tentativas > 0 and 'Você errou! Ainda possui {} tentativas!'.format(tentativas) or 'Você errou!')
        
        else:
            print('Letra Inválida!')
            continue

        print(exibe_letras_acertadas(letras_acertadas))

        # Se '_' nao existir em letras_acertadas
        ganhou = '_' not in letras_acertadas

    if ganhou == True:
        print(exibe_mensagem_venceu())

    else:
        print(exibe_mensagem_perdeu(palavra_secreta))

def exibe_menu():
     # Menu do jogo
    print('######################################')
    print('########### JOGO DA FORCA ############')
    print('######################################')
    print('############ 1 - FRUTAS ##############')
    print('########## 2 - PROFISSOẼS ############')
    print('############ 3 - CORES ###############')
    print('########### 4 - OBJETOS ##############')
    print('####### 0 - DIGITE UMA PALAVRA #######')
    print('######################################')

def busca_palavra(categoria):
    
    categorias = ('palavras/frutas.txt', 'palavras/profissoes.txt', 'palavras/cores.txt', 'palavras/objetos.txt')
    
    categoria = categorias[categoria - 1]
    
    # Buscando palavras de um arquivo externo
    arquivo = open(categoria, "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    
    palavra = palavras[randrange(0, len(palavras))].upper()
    return palavra

def exibe_letras_acertadas(letras_acertadas):
    return ' '.join(letras_acertadas)

def valida_categoria(cat):
    if cat.isnumeric():
        cat = int(cat)
        if cat >= 0 and cat <= 4:
            return True

    return False

def valida_letra(l):
    return len(l) == 1 and l.isalpha()

def preenche_letra_acertada(letra, palavra_secreta, letras_acertadas):
    for i in range (0, len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letras_acertadas[i] = letra

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def exibe_mensagem_venceu():
    print("Parabéns, você ganhou!")
    print("       ___________")
    print("      '._==_==_=_.'")
    print("      .-\\\:     /-.")
    print("     | (|:.     |) |")
    print("      '-|:.     |-'")
    print("        \\\::.  /")
    print("         '::..'")
    print("           ) (")
    print("         _.' '._")
    print("        '-------'")

def exibe_mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("         _______")
    print("      \"          \"")
    print("    \"              \"")
    print("  //   XX      XX    \/\ ")
    print("  \|  XXXX    XXXX   | /")
    print("   |  XXXX    XXXX   |/")
    print("   \_     XXX      _/")
    print("     |\   XXX    /|")
    print("     ||         ||")
    print("      | * * * * |")
    print("       \  = =  /")
    print("         \"---\"")

if(__name__ == "__main__"):
    jogar()
