# crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

print('\033[33m-=\033[m' * 15)
print('\033[36mDESMITIFICANDO A MATEMÁTICA\033[m')
print('\033[33m-=\033[m' * 15)
print('\n\033[35mÉ PAR OU IMPAR?\033[m')
num = int(input('Me diga um número qualquer: '))
if num % 2 == 0:
    print('\033[32mO número {} é par!\033[m'.format(num))
else:
    print('\033[32mO número {} é impar!\033[m'.format(num))
