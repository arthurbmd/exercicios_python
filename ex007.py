#desenvolva um programa  que leia as duas notas de um aluno, calcule e mostre sua média

print('\033[33m-=\033[m' * 20)
print('\033[34mVamos calcular a média do aluno\033[m')
print('\033[33m-=\033[m' * 20)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2
print('A média entre \033[30m{:.1f}\033[m e \033[30m{:.1f}\033[m é igual a \033[31m{:.1f}\033[m'.format(n1, n2, m))
