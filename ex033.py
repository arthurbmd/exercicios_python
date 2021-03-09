# faça um programa que leia tres números e mostre qual é o maior e qual é o menor

print('\033[33m-=\033[m' * 15)
print('\033[36mDESMITIFICANDO A MATEMÁTICA\033[m')
print('\033[33m-=\033[m' * 15)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
print('\n\033[31mUSANDO O IF\033[m')
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('\033[32mO menor valor digitado é \033[30m{}\033[m'.format(menor))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('\033[32mO maior valor digitado é \033[30m{}\033[m'.format(maior))

print('\033[35m=\033[m' * 20)

print('\n\033[31mUSANDO O ELIF\033[m')
if n1 > n2 and n1 > n3:
    print('\033[32mO maior número digitado foi \033[30m{}\033m'.format(n1))
elif n2 > n3:
    print('\033[32mO maior número digitado foi \033[30m{}\033[m'.format(n2))
else:
    print('\033[32mO maior número digitado foi \033[30m{}\033[m'.format(n3))
if n1 < n2 and n1 < n3:
    print('\033[32mO menor número digitado foi \033[30m{}\033[m'.format(n1))
elif n2 < n3:
    print('\033[32mO menor número digitado foi \033[30m{}\033[m'.format(n2))
else:
    print('\033[32mO menor número digitado foi \033[30m{}\033[m'.format(n3))

print('\033[35m=\033[m' * 20)

print('\n\033[31mUSANDO O MÉTODO MAX E MIN\033[m')
print('\033[32mO maior valor digitado é \033[30m{}\033[m'.format(max(n1, n2, n3)))
print('\033[32mO menor valor digitado é \033[30m{}\033[m'.format(min(n1, n2, n3)))
