#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('\033[33m-=\033[m' * 20)
print('\033[36mLOCADORA DE CARRO JOCA AUTOMOVEIS\033[m')
print('\033[33m-=\033[m' * 20)

dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quiilometros o carro rodou? '))
p = dia * 60 + km * 0.15
print('O total a pagar é de \033[31mR${:.2f}\033[m'.format(p))
