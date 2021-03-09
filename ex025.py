#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

print('\033[33m-=\033[m' * 15)
print('\033[36mANALISADOR DE NOMES\033[m')
print('\033[33m-=\033[m' * 15)
print('\n\033[32mVOCÊ TEM SILVA NO SEU NOME?\033[m\n')
nome = str(input('Digite seu nome completo: ')).strip()
print('\033[35mSeu nome tem Silva? \033[30m{}\033[m'.format('silva' in nome.lower()))
