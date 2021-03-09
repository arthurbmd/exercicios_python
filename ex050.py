# desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares
# se o valor for impar, desconsidere-o

print('\033[33m=\033[m' * 10)
print('\033[36mCONTADOR\033[m')
print('\033[33m=\033[m' * 10)

s = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um {}º número inteiro:'.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma dos {} valores pares lidos é {}.'.format(cont, s))
