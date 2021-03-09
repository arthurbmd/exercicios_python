# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas,
# o nome com todas minusculas
# quantas letras ao (todo sem considerar espaços)
# quantas letras tem o primeiro nome

print('\033[33m-=\033[m' * 15)
print('\033[36mANALISADOR DE NOME\033[m')
print('\033[33m-=\033[m' * 15)

nome = str(input('Digite seu nome completo: ')).strip()
print('\033[33mAnalisando seu nome...\033[m')
print('\033[32mSeu nome em maiúsculo é \033[30m{}\033[m'.format(nome.upper()))
print('\033[32mSeu nome em minúsculas é \033[30m{}\033[m'.format(nome.lower()))
print('\033[32mSeu nome tem ao todo tem \033[30m{}\033[32m letras\033[m'.format(len(nome.replace(' ', ''))))
lista = nome.split()
print('\033[32mSeu primeiro nome é \033[30m{} \033[32me tem \033[30m{} \033[32mletras\033[m'.format(lista[0], len(lista[0])))
