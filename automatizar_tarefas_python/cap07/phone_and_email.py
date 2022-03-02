#! /usr/bin/python3
# phone_and_email = Encontra números de telefone e de e-mail no clipboard

# Importando módulos
import re, pyperclip

# Copiando clipboard para a variável 
clipboard = pyperclip.paste()

# Encontrando telefone
phone_regex = re.compile(r'(0?\d{2}|\(0?\d{2}\))?\s?(\d{5}-?\d{4})')
find_phone = phone_regex.findall(clipboard)

# Encontrando email
email_regex = re.compile(r'\w+@\w+.\w+')
find_email = email_regex.findall(clipboard)

# Resultados
if find_phone:
    print('Telefones encontrados'.center(30, '='))
    for phone in find_phone:
        print(' '.join(phone))
else:
    print('Não foi encontrado nenhum telefone!')

if find_email:
    print('Email encontrados'.center(30, '='))
    for email in find_email:
        print(email)
else:
   print('Não foi encontrado nenhuma e-mail!')
