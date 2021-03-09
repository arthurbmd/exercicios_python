#Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e raiz quadrada

print('\033[33m-=\033[m' * 12)
print('\033[35mProgramando matemática!!!\033[m')
print('\033[33m-=\033[m' * 12)
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {0} é \033[32m{1}\033[m \nO triplo de {0} é \033[32m{2}\033[m '
      '\nE a raiz quadrada de {0} é \033[32m{3:.2f}\033[m'.format(n, d, t, r))
