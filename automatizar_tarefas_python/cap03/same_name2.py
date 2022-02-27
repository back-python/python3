# Usando uma variável global dentro de uma função
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
