# escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher
# qual será a base de conversão: 1- binário, 2 - octal, 3 hexadecimal

print('\033[33m=\033[m' * 30)
print('\033[36mCALCULADORA DE BASES NUMÉRICAS\033[m')
print('\033[33m=\033[m' * 30)
numero = int(input('Digite um número inteiro qualquer:'))
print('''\033[35mPara converter em: 
[1] binário 
[2] octal 
[3] hexadecimal\033[m''')
conversao = int(input('Digite uma opção:'))
if conversao == 1:
    print('O número {} em BINÁRIO é \033[32m{}\033m'.format(numero, bin(numero)[2:]))
elif conversao == 2:
    print('O número {} em OCTAL é \033[32m{}\033[m'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('O número {} em HEXADECIMAL é \033[32m{}\033[m'.format(numero, hex(numero)[2:]))
else:
    print('\033[31mERRO! OPÇÃO NÃO ENCONTRADA!\033[m')