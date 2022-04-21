'''
Este programa permite ao usuario escolher varios arquivos de uma pasta e copiar-los em um
caminho diferente.
'''

import os
import shutil

caminho_original = (r'path')
caminho_novo = (r'path')
extension = '.jpg'
#limpar a pasta destino caso haja algum arquivo nela
for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        if file.endswith(extension):
            os.remove(os.path.join(root, file))

#escolher os arquivos em uma lista
#ex_input: file1,file2,file3
l = str(input('digite os nomes dos arquivos sem extensao: ')).strip().upper()
lista = l.replace(',', ' ').split()
os.chdir(caminho_original)

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        for c in range (0, len(lista)):
            old_path = os.path.join(caminho_original, lista[c] + extension)
            new_path = os.path.join(caminho_novo, '{}'.format(c+1) + extension)
            if file.startswith(lista[c] + extension):
                shutil.copy(old_path, new_path)
