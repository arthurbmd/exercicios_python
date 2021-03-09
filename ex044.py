# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento: a vista, dinheiro/cheque 10% de desconto, a vista no cartão 5% de desconto, em até 2x no cartão normal
# 3x ou mais no cartão 20% de juros

valor = float(input('Preço das compras: R$'))
print('''Digite a forma de pagamento:
[1] À vista no Dinheiro / cheque
[2] À vista no cartão
[3] Parcelado 2x no cartão
[4] Parcelado 3x ou mais no cartão''')
pagamento = int(input('Digite a opção:'))
if pagamento == 1:
    final = valor - (valor * 0.1)
elif pagamento == 2:
    final = valor - (valor * 0.05)
elif pagamento == 3:
    final = valor
    parcela = final / 2
    print('Sua compra será parcelada em 2 vezes de R${:.2f} SEM JUROS')
elif pagamento == 4:
    parcelamento = int(input('Quantas parcelas?'))
    final = valor * 1.2
    parcela = final / parcelamento
    print('Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS.'.format(parcelamento, parcela))
else:
    print('Opção inválida. Tente novamente.')
    exit()
print('Suas compras no valor de R${:.2f} passará a custar R${:.2f}.'.format(valor, final))
