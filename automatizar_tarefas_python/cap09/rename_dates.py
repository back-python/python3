#! /usr/bin/python3
# rename_date.py - Renomeia arquivos com datas no padrao americano, para o padrão brasileiro

import shutil, os, re

date_us = re.compile(r'^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)?\d\d)(.*?)$')

# Percorre os arquivos do diretório de trabalho com um loop.
for us_file_name in os.listdir('.'):
    mo = date_us.search(us_file_name)

    # Ignora os arquivos que não tenham uma data.
    if mo == None:
        continue

    # Obtém as diferentes partes do nome do arquivo.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Compõe o nome do arquivo em estilo brasileiro.
    br_file_name = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Obtém os paths absolutos completos dos arquivos.
    abs_working_dir = os.path.abspath('.')
    us_file_name = os.path.join(abs_working_dir, us_file_name)
    br_file_name = os.path.join(abs_working_dir, br_file_name)
    
    # Renomeia os arquivos.
    #print('Renaming "%s" to "%s"...' % (us_file_name, br_file_name))

    # remova o caractere de comentário após os testes
    shutil.move(us_file_name, br_file_name)
    
