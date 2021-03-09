# faça um programa que tenha uma função chamada contador(), que receba tres parametros: inicio, fim e passo e realize a
# contagem. Seu programa tem que realizar tres contagens atraves da função criada: a de 1 até 10 de 1 em 1 b)de 10 até 0,
# de 2 em 2, C) uma contagem personalizada.


def contador(inic, fim, passo):
    if passo == 0:
        passo = 1
    else:
        passo = abs(passo)
    print('-=' * 30)
    print(f'Contagem de {inic} até {fim} de {passo} em {passo}')
    if inic < fim:
        for c in range(inic, fim + 1, passo):
            print(c, end=' ')
            sleep(0.5)
    else:
        for c in range(inic, fim - 1, passo * (-1)):
            print(c, end=' ')
            sleep(0.5)
    print('\nFim!')


from time import sleep

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio:  '))
f = int(input('Fim:     '))
p = int(input('Passo:   '))

contador(i, f, p)
