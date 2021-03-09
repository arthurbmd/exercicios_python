#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento
print('\033[33m-=\033[m' * 10)
print('\033[36mASSALARIANDO\033[m')
print('\033[33m-=\033[m' * 10)

s = float(input('Digite o salário do funcionário: R$'))
sn = s + s * 0.15
print('Um funcionário que ganhava um salário de \033[30mR${:.2f}\033[m, '
      '\033[31mcom o aumento de 15%\033[m, \033[32mpassa a receber R${:.2f}\033[m'.format(s, sn))
