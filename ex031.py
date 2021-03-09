# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando
# R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas

print('\033[33m-=\033[m' * 10)
print('\033[36mVIAGEM 0800\033[m')
print('\033[33m-=\033[m' * 10)
print('\n\033[35mVAI VIAJAR?\033[m')
viagem = float(input('Qual a distância em Km da viagem? '))
if viagem <= 200:
    passagem = viagem * 0.5
else:
    passagem = viagem * 0.45
print('\n\033[31mUSANDO CONDICIONAL COMPOSTA\033[m')
print('\033[32mO valor da passagem será de \033[30mR${:.2f} '
      '\033[32mpara a viagem de {} km\033[m'.format(passagem, viagem))
print('\n\033[31mUSANDO CONDICIONAL SIMPLES\033[m')
passagem = viagem * 0.5 if viagem <= 200 else viagem * 0.45
print('\033[32mO valor da passagem será de \033[30mR${:.2f} '
      '\033[32m para a viagem de {} km\033[m'.format(passagem, viagem))
