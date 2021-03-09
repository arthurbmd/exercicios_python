# um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

print('\033[33m-=\033[m' * 15)
print('\033[36mSORTEADOR DE ALUNOS\033[m')
print('\033[33m-=\033[m' * 15)

print('\n\033[32mBEM VINDO, PROFESSOR!\033[m')
alu1 = str(input('Primeiro aluno: ')).strip().capitalize()
alu2 = str(input('Segundo aluno: ')).strip().capitalize()
alu3 = str(input('Terceiro aluno: ')).strip().capitalize()
alu4 = str(input('Quarto aluno: ')).strip().capitalize()
lista = [alu1, alu2, alu3, alu4]
print('\n\033[31mUSANDO VARIAVEL LISTA\033[m')
print('O aluno escolhido foi {}'.format(choice(lista)))
print('\n\033[31mUSANDO LISTA DENTRO DO FORMAT\033[m')
print('O aluno escolhido foi {}'.format(choice([alu1, alu2, alu3, alu4])))
