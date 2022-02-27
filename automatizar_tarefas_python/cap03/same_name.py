# Variaveis globais e locais com mesmo nome
def spam():
    eggs = 'eggs spam local'
    print(eggs) # exibe 'spam local'

def bacon():
    eggs = 'eggs bacon local'
    print(eggs) # exibe 'bacon local'
    spam()
    print(eggs)# exibe 'bacon local'

eggs = 'eggs global'
bacon()
print(eggs)
