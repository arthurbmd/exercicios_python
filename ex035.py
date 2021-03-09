# desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar um triangulo

print('\033[33m=\033[m'*25)
print('\033[36mAnalisador de um triângulo\033[m')
print('\033[33m=\033[m'*25)
a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[32mSuas medidas podem formar um triangulo!\033[m')
else:
    print('\033[31mSuas medidas não podem formar um triagunlo!\033[m')
