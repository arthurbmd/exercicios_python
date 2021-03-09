# Faça um programa que leia o nome completo de uma pessoa, mostrado em seguida o primeiro e o último nome separadamente
# ex: ana maria de souza primeiro = Ana, ultimo = Souza

print('\033[33m-=\033[m' * 15)
print('\033[36mANALISADOR DE NOME\033[m')
print('\033[33m-=\033[m' * 15)
print('\n\033[31mVAMOS VER QUAL O SEU PRIMEIRO E ÚLTIMO NOME?\033[m')
nome = str(input('Digite seu nome completo: ')).split()
print('\n\033[32mMuito prazer em conhecê-lo!\033[m')
print('\033[34mSeu primeiro nome é \033[30m{}\033[m'.format(nome[0]))
print('\033[35mSeu último nome é \033[30m{}\033[m'.format(nome[-1]))
