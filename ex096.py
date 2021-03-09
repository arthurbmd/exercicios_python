# faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def area(a, b):
    area = a * b
    print(f'A área de um terreno de {a} x {b} é de {area}m².')


print('CONTRE DE TERRENO'.center(30))
print('-' * 30)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
