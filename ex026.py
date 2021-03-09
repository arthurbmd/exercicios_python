# Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "a"
# em que posição ela aparece a primeira vez
# em que posição ela aparece a ultima vez

print('\033[33m-=\033[m' * 15)
print('\033[36mANALISADOR DE FRASE\033[m')
print('\033[33m-=\033[m' * 15)
print('\n\033[31mVAMOS CONTAR AS LETRAS A?\033[m')
frase = str(input('Digite uma frase: ')).strip()
print('\n\033[32mAnalisando..\033[m')
print('\033[34mA letra A aparece {} vezes na frase\033[m'.format(frase.lower().count('a')))
print('\033[35mA primeira letra A apareceu na posição \033[30m{}\033[m'.format(frase.lower().find('a') + 1))
print('\033[33mA última letra A apareceu na posição \033[30m{}\033[m'.format(frase.lower().rfind('a') + 1))
