# Escreva um programa que leia dois números inteiros e compare-os, mostrando ta tela uma mensagem:
# o primeiro valor é o maior, o segundo valor é o maior, não existe valor maior, os dois são iguais

print('\033[33m=\033[m' * 30)
print('\033[36mDESMITIFICANDO A MATEMÁTICA\033[m')
print('\033[33m=\033[m' * 30)
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[32mPRIMEIRO\033[m número é o maior!')
elif n2 > n1:
    print('O \033[32mSEGUNDO\033[m é o maior!')
else:
    print('Os dois números são \033[32mIGUAIS\033[m!')
