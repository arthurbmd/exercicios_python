# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade: até 9 mirim, até 14 infantil, até 19 junior, até 25 senior, acima master

from datetime import date

print('\033[33m=\033[m' * 40)
print('\033[36mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('\033[33m=\033[m' * 40)
nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('\033[30mO atleta tem {} anos.\033[m'.format(idade))
if idade <= 9:
    print('\033[32mClassificação: MIRIM.\033[m')
elif idade <= 14:
    print('\033[34mClassificação: INFANTIL.\033[m')
elif idade <= 19:
    print('\033[33mClassificação: JúNIOR.\033[m')
elif idade <= 25:
    print('\033[35mClassificação: SÊNIOR.\033[m')
else:
    print('\033[31mClassificação: MASTER.\033[m')
