#Escreva um programa que converta uma temperatura em ºC e converta para ºF
print('\033[33m-=\033[m' * 15)
print('\033[36mCONVERSOR DE TEMPERATURAS\033[m')
print('\033[33m-=\033[m' * 15)

c = float(input('Informe a temperatura em ºC: '))
f = c * 9 / 5 + 32
print('\033[32mA temperatura de {:.1f}ºC\033[m \033[31mcorresponde a {:.1f}ºF\033[m'.format(c, f))
