# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele

print('\033[33m-\033[m' * 30)
print('\033[1;36mVamos analisar uma palavra?\033[m')
print('\033[33m-\033[m' * 30)
n = input('Digite algo: ')
print('\033[;31m', type(n), '\033[m')
print('Só tem espaços?', '\033[31m', n.isspace(), '\033[m')
print('É um número?', '\033[31m', n.isnumeric(), '\033[m')
print('É alfabético?', '\033[31m', n.isalpha(), '\033[m')
print('É alfanúmerico?', '\033[31m', n.isalnum(), '\033[m')
print('Contém só letras maiusculas? ', '\033[31m', n.isupper(), '\033[m')
print('Contém só letras minusculas?', '\033[31m', n.islower(), '\033[m')
print('Está capitalizado?', '\033[31m', n.istitle(), '\033[m')
