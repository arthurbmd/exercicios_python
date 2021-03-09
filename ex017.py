# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
# calcule e mostre o comprimento da hipotenusa

from math import hypot, sqrt

print('\033[33m-=\033[m' * 15)
print('\033[36DESMITIFICANDO A MATEMÁTICA\033[m')
print('\033[33m-=\033[m' * 15)

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(ca, co)
print('\n\033[31mUSANDO A FUNÇAO HYPOT\033[m')
print('\033[32mO comprimento da hipotenusa é {:.2f}\033[m'.format(hi))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('\n\033[31mUSANDO O PRINCIPIO MATEMÁTICO\033[m')
print('\033[32mO comprimento da hipotenusa é {:.2f}\033[m'.format(hi))
hi = sqrt((co ** 2) + (ca ** 2))
print('\n\033[31mUSANDO A FUNÇÃO SQRT\033[m')
print('\033[32mO comprimento da hipotenusa é {:.2f}\033[m'.format(hi))
