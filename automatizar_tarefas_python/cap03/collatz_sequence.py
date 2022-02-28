# Collatz Sequence
# Digite um número inteiro e ele será reduzido a 1
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    number = int(input('Enter number: '))

    while number != 1:
        number = collatz(number)
        print(number)
        
except ValueError:
    print('Error: Enter integers only!')


    
