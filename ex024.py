# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

print('\033[33m-=\033[m' * 15)
print('\033[36mANALISADOR DE CIDADES\033[m')
print('\033[33m-=\033[m' * 15)
cidade = str(input('Em que cidade você nasceu?')).strip().lower()
print('\n\033[31mUSANDO FATIAMENTO DE STRING\033[m')
print('santo' in cidade[:5])
print('\n\033[31mUSANDO STARTSWITH\033[m')
print(cidade.startswith('santo'))
print('\n\033[31mUSANDO SPLIT PARA CRIAR UMA LISTA\033[m')
cid = str(input('Em que cidade você nasceu?')).lower().split()
print('santo' in cid[0])
