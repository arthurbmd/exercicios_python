# faça um programa que leia o peso de cinco pessoas, no final, mostre qual foi o maior e o menor peso lidos

maior = 0
menor = float('inf')
pesos = []
for k in range(1, 6):
    peso = float(input('Digite o {}º peso: (Kg) '.format(k)))
    pesos.append(peso)
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso digitado foi {}Kg'.format(maior))
print('O menor peso digitado foi {}Kg'.format(menor))

print('O maior peso digitado foi {}Kg'.format(max(pesos)))
print('O menor peso digitado foi {}Kg'.format(min(pesos)))




