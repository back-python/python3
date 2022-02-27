# Tratamento de erros com Python
def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid Value!')
        
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

print('='*20)
# Outro exemplo
# Bacon(1) não será executado, pois quando um erro é encontrado em try ele pula para except
# e continua a execução do código
def bacon(divide_by):
    return 42 / divide_by

try:
    print(bacon(2))
    print(bacon(12))
    print(bacon(0))
    print(bacon(1))
except ZeroDivisionError:
    print('Error: Invalid value!')
