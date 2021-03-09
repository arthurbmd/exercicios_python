# crie um programa que leia vários números inteiros pelo teclado, no final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuario se ele
# quer continuar ou não a digitar valores.

maior = cont = soma = 0
menor = float('inf')
resp = 's'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = str(input('Deseja continuar? [S/N]: ')).strip()
    while resp not in 'SsNn':
        resp = str(input('Opção inválida! Deseja continuar? [S/N]: ')).strip()
media = soma / cont
print('Você digitou {} números, a média deles é {}'.format(cont, media))
print('O maior valor digitado foi {} e o menor {}'.format(maior, menor))
