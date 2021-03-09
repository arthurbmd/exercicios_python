# crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
print('\033[33m=\033[m' * 10)
print('\033[36mCONTADOR\033[m')
print('\033[33m=\033[m' * 10)

print('\033[31mUsando o IF, consumimos mais do processador\033[m')
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')

print('\n\033[32mComeçando no número que já sabemos e pulando, consumimos menos processamento')
for c in range(2, 51, 2):
    print(c, end=' ')
print('Acabou!')