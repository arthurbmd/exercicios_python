# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessaria para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
print('\033[33m-=\033[m' * 15)
print('\033[36mLOJA DE PINTURA DO SEU MANUEL\033[m')
print('\033[33m-=\033[m' * 15)

l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
a = l * h
t = a / 2
print('Sua parede tem dimensão de \033[30m{}m x {}m\033[m e sua área é de \033[32m{:.1f}m²\033[m. \n'
      'Para pintá-la, você deverá utilizar \033[32m{} L\033[m de tinta'.format(l, h, a, t))
