import random

secret_number = random.randint(1, 20)

print('guess the number in the range 1 and 10')
for i in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < 1 or guess > 20:
        print('Warning! Number out of range!')
        continue
    
    if guess > secret_number:
        print('Your guess is to high!')
    elif guess < secret_number:
        print('Your guess is to low')
    else:
        print('Good job! Your gussed my number in {} guesses!'.format(i))
        break

if guess != secret_number: 
    print('Nope. The number I was thinking of was {}.'.format(str(secret_number)))

print('--END--')
