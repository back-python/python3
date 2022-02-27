# Escopos locais não podem usar variáveis de outros escopos locais
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

print('X'*20)
# Variáveis globais podem ser lidas a partir de um escopo local
def spam():
    print(eggs)

eggs = 42
spam()
print(eggs)




