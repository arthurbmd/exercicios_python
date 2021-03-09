# Crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores, 21 anos

from datetime import date
maior = 0
menor = 0
atual = date.today().year
for k in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(k)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo, tivemos {} pessoas maiores de idade. \nE também, {} pessoas menores de idade!'.format(maior, menor))
