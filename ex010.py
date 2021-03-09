#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#US$1,00 = R$3,27

print('\033[33m-=\033[m' * 13)
print('\033[36mCONVERSOR DE MOEDAS!\033[m')
print('\033[33m-=\033[m' * 13)
r = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = r / 5.50
eu = r / 5.95
li = r / 6.83
print('Com R${}, você pode comprar \033[31mUS${:.2f}\033[m'.format(r, dol))
print('Com R${}, você pode comprar \033[31mE{:.2f}\033[m'.format(r, eu))
print('Com R${}, você pode comprar \033[31mL{:.2f}\033[m'.format(r, li))
