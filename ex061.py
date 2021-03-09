# refaça o desafio 051, lendo o primeiro temo e a razão de uma pa,
# mostrando os 10 primeiros termos da progressão usando a estrutura while

num = int(input('Digite um número: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
termo = num
print('A progressão aritmética é:')
while cont < 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    cont += 1
print('Fim')
