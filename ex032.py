# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date

print('\033[33m-=\033[m' * 10)
print('\033[36mANALISADOR DE ANOS\033[m')
print('\033[33m-=\033[m' * 10)
print('\n\033[34mO ano que você quer saber é bissexto?\033[m')
ano = int(input('Digite um ano qualquer. Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('\033[32mO ano {} é BISSEXTO\033[m'.format(ano))
else:
    print('\033[31mO ano {} NÃO é bissexto\033[m'.format(ano))
