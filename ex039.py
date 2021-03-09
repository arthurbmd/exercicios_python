# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# se ele vai ainda se alistar ao serviço militar, se é a hora de se alistar, se já passou do tempo do alistamento
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('\033[33m=\033[m' * 20)
print('\033[36mALISTAMENTO MILITAR\033[m')
print('\033[33m=\033[m' * 20)
print('''Informe seu genêro
[1] Masculino
[2] Feminino''')
sexo = int(input('Digite sua opção: '))
if sexo == 1:
    nascimento = int(input('Digite o ano do nascimento: '))
    atual = date.today().year
    idade = atual - nascimento
    prazo = abs(idade - 18)
    ano = nascimento + 18
    print('\033[30mQuem nasceu em {} tem {} em {}.\033[m'.format(nascimento, idade, atual))
    if idade < 18:
        print('\033[32mAinda faltam {} anos para o alistamento.\033[m'.format(prazo))
        print('\033[32mSeu alistamento será em {}.\033[m'.format(ano))
    elif idade > 18:
        print('\033[31mVocê deveria ter se alistado a {} anos.\033[m'.format(prazo))
        print('\033[31mSeu alistamento foi em {}.\033[m'.format(ano))
    elif idade == 18:
        print('\033[33mVocê deve se alistar IMEDIATAMENTE!\033[m')
elif sexo == 2:
    print('\033[35mVocê não precisa se alistar!\033[m')
else:
    print('\033[31mERRO! OPÇÃO INVÁLIDA.\033[m')
