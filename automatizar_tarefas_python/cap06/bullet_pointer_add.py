#! /usr/bin/python3
# bullet_pointer_add Adicionando marcações, no início das frases

import pyperclip

clipboard = pyperclip.paste().split('\n')
bullet_items = []

for item in clipboard:
    if item.strip():
        bullet_items.append('* ' + item)
    
clipboard = '\n'.join(bullet_items)
pyperclip.copy(clipboard)
