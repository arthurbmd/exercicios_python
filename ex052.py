# faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(num, cont))
if cont == 2:
    print('E por isso, é um número primo!')
else:
    print('E por isso, não é um número primo!')
