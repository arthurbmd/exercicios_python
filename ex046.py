# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio
# indo de 10 até 0 com uma pausa de 1 segundo entre eles.

from time import sleep
print('\033[33m=\033[m' * 20)
print('\033[36mReveillon Copacabana\033[m')
print('\033[33m=\033[m' * 20)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[32mFeliz ano novo!!!\033[m')
