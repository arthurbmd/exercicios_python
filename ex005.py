#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

print('\033[33m-=\033[m' * 12)
print('\033[36mAntecessor e sucessor\033[m')
print('\033[33m-=\033[m' * 12)
n = int(input('Digite um número: '))
ant = n - 1
suc = n + 1
print('\033[31mUsando variáveis\033[m')
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, ant, suc))
print('\033[31mUsando sem variáveis\033[m')
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n + 1), (n - 1)))
