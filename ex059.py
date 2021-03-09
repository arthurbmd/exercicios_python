# Crie um programa que leia dois valores e mostre um dados na tela:
# [1] somar, 2 multiplicar, 3 maior, 4 novos números, 5 sair do programa, seu programa deverá realizar
# a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
opcao = 0
while opcao != 5:
    print('''Qual operação deseja fazer:
     [1] Somar
     [2] Multiplicar
     [3] Maior
     [4] Novos números
     [5] Sair do programa''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
        print('=-=' * 10)
    elif opcao == 2:
        multiplicar = n1 * n2
        print('O produto entre {} e {} é igual a {}.'.format(n1, n2, multiplicar))
        print('=-=' * 10)
    elif opcao == 3:
        maior = max(n1, n2)
        print('Entre {} e {} o maior número é {}.'.format(n1, n2, maior))
        print('=-=' * 10)
    elif opcao == 4:
        print('Informe os novos valores.')
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
        print('=-=' * 10)
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('ERRO! Opção inválida.')
        print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')


