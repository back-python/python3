"""
UnboundLocalError: local variable 'eggs' referenced before assignment
Tentando usar uma variável local, antes de atribuir um valor para ela
"""
def spam():
    print(eggs) # ERRO!
    eggs = 'spam local'

eggs = 'global'
spam()
