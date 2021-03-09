# crie um programa que leia vários números inteiros pelo teclado.
# o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
# no final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

num = soma = cont = 0
while num != 999:
    num = int(input('Digite um número [Digite 999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))
