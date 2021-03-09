# refaça o desafio 009, mostrando a tabuada de um número que o usuario escolher,
# só que agora utilizando um laço for

print('\033[33m-\033[m' * 10)
print('\033[36mTABUANDO\033[m')
print('\033[33m-\033[m' * 10)
n = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n*c)))
