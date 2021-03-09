# faça um programa que leia um número qualquer e mostre o seu fatorial.
#ex 5!= 5x4x3x2x1 = 120

from math import factorial
num = int(input('Digite um número: '))
f = factorial(num)
print('\033[31mUSANDO O FACTORIAL\033[m')
print('O fatorial de {} é {}.'.format(num, f))
print('\n\033[31mUSANDO O WHILE\033[m')
cont = num
fator = 1
print('Calculando {}! = '.format(num), end=' ')
while cont > 0:
    fator *= cont
    print('{} '.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print('{}.'.format(fator))

print('\n\033[31mUSANDO O FOR\033[m')
f = 1
print('Calculando {}! = '.format(num), end='')
for c in range(num, 0, -1):
    f *= c
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
print('{}.'.format(f))
