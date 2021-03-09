# melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
# o programa encerra quando ele disser que quer mostrar 0 termos.

n = int(input('Primeiro termo:'))
r = int(input('Razão: '))
cont = 0
termo = n
limite = 10
while cont < limite:
    print('{}'.format(termo), end=' -> ')
    termo += r
    cont += 1
    if cont == limite:
        print('PAUSA')
        limite += int(input('Quantos termos deseja mostrar a mais?'))
print('A progressão foi finalizada com {} termos mostrados'.format(cont))
