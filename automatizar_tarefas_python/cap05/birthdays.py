birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()

    if name == '':
        break

    if name in birthdays:
        print('{} is the birthday of {}'.format(birthdays[name], name))
    else:
        print('I do not have birthday information for {}'.format(name))
        print('What is their birthday? (Example: Dec 15)')
        birthdays[name] = input()
        print('Birthday database is updated!')
        
