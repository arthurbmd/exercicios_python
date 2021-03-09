# Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
# o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos vai pagar.
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o emprestimo será negado
print('\033[33m=\033[m' * 22)
print('\033[36mMEU PYTHON, MINHA VIDA\033[m')
print('\033[33m=\033[m' * 22)

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos deseja pagar? '))
prestacao = casa / (anos * 12)
print('Para pagar um imóvel de \033[34mR${:.2f}\033[m em \033[34m{}\033[m anos'
      ' a prestação será de \033[32mR${:.2f}\033[m'.format(casa, anos, prestacao))
if prestacao <= (salario * 0.3):
    print('\033[32mO empréstimo poderá ser CONCEDIDO!\033[m')
else:
    print('\033[31mO empréstimo será NEGADO!\033[m')
