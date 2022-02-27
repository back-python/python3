"""
1. Se uma variável estiver sendo usada no escopo global (ou seja, fora de todas as funções), ela sempre será uma variável global.
2. Se houver uma instrução global para essa variável em uma função, ela será uma variável global.
3. Caso contrário, se a variável for usada em uma instrução de atribuição na função, ela será uma variável local.
4. Porém, se a variável não for usada em uma instrução de atribuição, ela será uma variável global.
"""
# Exemplo de regras
def spam():
    global eggs
    eggs = 'spam' # essa é a variável global

def bacon():
    eggs = 'bacon' # essa é uma variável local

def ham():
    print(eggs) # essa é a variável global

eggs = 42 # essa é a variável global
spam()
print(eggs)
