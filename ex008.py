#Escreva um programa que leia um valor  em metros e converta em centimetros e milimetros

print('\033[33m-=\033[m'*10)
print('\033[36mCONVERSOR DE MEDIDAS\033[m')
print('\033[33m-=\033[m'*10)
m = float(input('Digite uma medida em metros: '))
dm = m * 10
cm = m * 100
mm = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
print('A medida {} m corresponde a: \n\033[35m{}\033[m km \n\033[35m{}\033[m hm \n\033[35m{}\033[m dam '
      '\n\033[35m{:.0f}\033[m dm \n\033[35m{:.0f}\033[m cm \n\033[35m{:.0f}\033[m mm'.format(m, km, hm, dam, dm, cm, mm))
