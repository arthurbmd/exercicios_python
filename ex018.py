# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import radians, tan, sin, cos

print('\033[33m-=\033[m' * 15)
print('\033[36mDESMITIFICANDO A MATEMÁTICA\033[m')
print('\033[33m-=\033[m' * 15)

ang = float(input('Digite um ângulo: '))
rad = radians(ang)
print('\033[32mO ângulo de {} tem o SENO de {:.2f}\033[m'.format(ang, sin(rad)))
print('\033[32mO ângulo de {} tem o COSSENO de {:.2f}\033[m'.format(ang, cos(rad)))
print('\033[32mO ângulo de {} tem a TANGENTE de {:.2f}\033[m'.format(ang, tan(rad)))
