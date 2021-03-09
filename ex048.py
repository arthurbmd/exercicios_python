# faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e
# que se encontram no intervalo de 1 até 500

print('\033[33m=\033[m' * 10)
print('\033[36mCONTADOR\033[m')
print('\033[33m=\033[m' * 10)
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} números solicitados é {}'.format(cont, s))
