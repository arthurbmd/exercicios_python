# desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status:
# de acodo com a tabela abaixo, abaixo de 18.5 abaixo do peso, entre 18,5 e 25, peso ideal, 25 até 30 sobrepeso
# 30 até 40 obesidade, acima de 40 obesidade mórbida
print('\033[33m=\033[m' * 30)
print('\033[36mIMC PELO MINISTÉRIO DA SAÚDE\033[m')
print('\033[33m=\033[m' * 30)

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (M) '))
imc = peso / (altura ** 2)
print('\033[34mSeu IMC é de {:.1f}\033[m'.format(imc))
if imc < 18.5:
    print('\033[33mVocê está na faixa ABAIXO DO PESO!\033[m')
elif imc < 25:
    print('\033[32mPARABÉNS! Você está na faixa de PESO NORMAL!\033[m')
elif imc < 30:
    print('\033[33mVocê está na faixa SOBREPESO!\033[m')
elif imc < 40:
    print('\033[33mVocê está na faixa OBESIDADE!\033[m')
else:
    print('\033[31mCUIDADO! Você está na faixa OBESIDADE MÓRBIDA!\033[m')
