# escreva um programa que leia o número inteiro qualquer e mostre na tela os n primeiros elementos
# de uma sequencia de fibonacci.
# 0-1-1-2-3-5-8

print('Gerador de elementos da uma Sequencia de Fibonacci')
n = int(input('Digite quantos elementos você quer ver: '))
cont = 2
a = 0
b = 1
print('{} -> {} -> '. format(a, b), end='')
while cont < n:
    soma = a + b
    print('{}'.format(soma), end=' -> ')
    a, b = b, soma
    cont += 1
print('Fim')
