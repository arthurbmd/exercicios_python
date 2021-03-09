# faça um programa que tenha uma função chamada escreva() que receba um texta qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável ex: excreva ('Olá Mundo') saída -------- \nolá mundo \n-------

def escreva(msg):
    tamanho = len(msg) + 4
    print(f'~' * tamanho)
    print(f'{msg}'.center(tamanho))
    print('~' * tamanho)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CEV')
