from random import randint
import sys
from tkinter import *
from tkinter import messagebox

JOKENPO = {
    'PEDRA': 0,
    'PAPEL': 1,
    'TESOURA': 2
}

def pedra():
    escolha_jogador = 'PEDRA'
    jogo(escolha_jogador)

def papel():
    escolha_jogador = 'PAPEL'
    jogo(escolha_jogador)

def tesoura():
    escolha_jogador = 'TESOURA'
    jogo(escolha_jogador)

def jogada_cpu():
    return randint(0,2)

def jogo(escolha_jogador):
    jogador = JOKENPO[escolha_jogador]
    cpu = jogada_cpu()

    print(jogador)
    print(cpu)

    if jogador == cpu:
        mensagem = 'Empatou!'
    elif jogador - cpu == -2 or jogador - cpu == 1:
        mensagem = 'Você venceu!'
    else:
        mensagem = 'Você perdeu!'

    messagebox.showinfo('Resultado', mensagem)
    sys.exit()

def jogar():
    # Interface

    janela = Tk()
    janela.title('JOKENPO') # Título da janela
    janela.geometry('250x350') # Tamanho da janela

    texto_orientacao = Label(janela, text='PEDRA, PAPEL OU TESOURA?') # Label precisa saber de onde ele é, e o que será escrito.
    texto_orientacao.grid(column=0, row=0, padx=20, pady=20)

    botao_pedra = Button(janela, text='PEDRA',padx=22, command=pedra)
    botao_pedra.grid(column=0,padx=10, pady=10, row=1)

    botao_papel = Button(janela, text='PAPEL', padx=22, command=papel)
    botao_papel.grid(column=0, row=2,padx=10, pady=10)

    botao_tesoura = Button(janela, text='TESOURA', command=tesoura)
    botao_tesoura.grid(column=0, row=3, padx=10, pady=10)

    janela.mainloop()

if(__name__ == "__main__"):
    jogar()
