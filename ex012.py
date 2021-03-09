#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

print('\033[33m-=\033[m' * 20)
print('\033[36mLOJA DE CONVENIÊNCIA SEU MARRECO\033[m')
print('\033[33m-=\033[m' * 20)
p = float(input('Digite o valor do produto: R$'))
pn = p - p * 0.05
print('O produto que custava \033[30mR${:.2f}\033[m, na promoção, de 5% de desconto, vai custar \033[32mR${:.2f}\033[m'.format(p, pn))
