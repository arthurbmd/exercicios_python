# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# para salários superiores a R$1.250,00, calcule um aumento de 10% para os inferiores ou iguais, o aumento é de 15%

print('\033[33m-=\033[m' * 15)
print('\033[36mASSALARIANDO\033[m')
print('\033[33m-=\033[m' * 15)
salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15
print('\033[35mO funcionário que antes tinha um salario de \033[30mR${:.2f}\033[35m,'
      ' passará a receber \033[32mR${:.2f}\033[m'.format(salario, aumento))
