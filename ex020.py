# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('\033[33m-=\033[m' * 15)
print('\033[36mSORTEADOR DE ALUNOS\033[m')
print('\033[33m-=\033[m' * 15)

print('\n\033[32mBEM VINDO, PROFESSOR!\033[m')
n1 = str(input('Primeiro aluno: ')).strip().capitalize()
n2 = str(input('Segundo aluno: ')).strip().capitalize()
n3 = str(input('Terceiro aluno: ')).strip().capitalize()
n4 = str(input('Quarto aluno: ')).strip().capitalize()

lista = [n1, n2, n3, n4]
shuffle(lista)
print('\n\033[34mA ordem de apresentação será {}\033[m'.format(lista))