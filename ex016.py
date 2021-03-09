# crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: digite um numero: 6.127, o numero 6.127 tem a parte inteira 6.

print('\033[33m-=\033[m' * 15)
print('\033[36mDESMITIFICANDO A MATEMÁTICA\033[m')
print('\033[33m-=\033[m' * 15)
from math import trunc

num = float(input('Digite um número: '))
print('\033[31mUSANDO A FUNÇÃO TRUNC\033[m')
print('\033[32mO valor digitado foi {} e sua parte inteira é {}\033[m'.format(num, trunc(num)))
print('\n\033[31mUSANDO A FUNÇÃO INT\033[m')
print('\033[32mO valor digitado foi {} e sua parte inteira é {}\033[m'.format(num, int(num)))
