# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado. a multa vai custar R$7,00 por km acima do limite

print('\033[33m-=\033[m' * 15)
print('\033[36mRADAR ELETRÔNICO\033[m')
print('\033[33m-=\033[m' * 15)
km = float(input('Qual é a velocidade atual do carro? '))
if km > 80:
    multa = (km - 80) * 7
    print('\033[31mVocê foi multado por ultrapassar o limite de 80 Km/h.\033[m '
          '\n\033[35mVocê deverá pagar uma multa de \033[31mR${:.2f}\033[m'.format(multa))
print('\033[32mTenha um bom dia e dirija com segurança!\033[m')
