# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas

print('\033[33m-=\033[m' * 10)
print('\033[34mBEM VINDO!!!\033[m')
print('\033[33m-=\033[m' * 10)

nome = input('Qual é o seu nome? ')
print('Olá, \033[34m{}\033[m! Prazer em te conhecer!'.format(nome))
