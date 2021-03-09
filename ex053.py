# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona.

frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
print('O inverso de {} é {}'.format(frase, frase[::-1]))
print('\n\033[31mUSANDO A MANEIRA ENXUTA COM INVERSÃO DE STRING\033[m')
if frase == frase[::-1]:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')

print('\n\033[31mUSANDO O COMANDO FOR\033[m')
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
if frase == inverso:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')
