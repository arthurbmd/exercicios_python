# escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# o programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('\033[33m-\033[m' * 30)
print('\033[36mJOGO DA ADIVINHAÇÃO\033[m')
print('\033[33m-\033[m' * 30)

npc = randint(0, 5)
print('\033[35mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
nuser = int(input('Em que número pensei? '))
print('\033[33mPROCESSANDO...\033[m')
sleep(3)
if npc == nuser:
    print('\033[32mPARABÉNS! VocÊ ganhou!\033[m')
else:
    print('\033[31mGANHEI! eu pensei no número {} e não no número {}!\033[m'.format(npc, nuser))
