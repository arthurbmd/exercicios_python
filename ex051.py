# Desenvolva um programa que leia o primeiro termo e a razão de uma PA, no final, mostre os 10 primeiros termos
# dessa progressão.

print('\033[33m-=\033[m' * 15)
print('\033[36mDESMITIFICANDO A MATEMÁTICA\033[m')
print('\033[33m-=\033[m' * 15)
print('{}'.format('\033[32m10 TERMOS DA PA\033[m'))
num = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão da progressão:'))
for c in range(num, num + (10 * razao), razao):
    print(c, '-> ', end='')
print('Fim')
