# Crie um programa que leia dois números e mostre a soma entre eles

print('\033[33m-=\033[m' * 15)
print('\033[36mVamos somar dois números!!!\033[m')
print('\033[33m-=\033[m' * 15)
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 + n2
print('A soma entre \033[30m{}\033[m e \033[30m{}\033[m é igual a \033[34m{}\033[m!'.format(n1, n2, s))
