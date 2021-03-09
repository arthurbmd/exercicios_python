# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa, mostre:
# a media de idade do grupo, qual é o nome do homem mais velho. quantas mulheres tem menos de 20 anos

soma = 0
velho = 0
homemvelho = ''
cont = 0
for c in range(1, 5):
    print('---{}ªPESSOA----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    if sexo not in 'Mm' and sexo not in 'Ff':
        print('Opção inválida! Tente novamente')
        exit()
    soma += idade
    if sexo in 'Mm' and idade > velho:
        homemvelho = nome
        velho = idade
    if sexo in 'Ff' and idade < 20:
        cont += 1
media = soma / 4
print('A média de idade é {} anos'.format(media))
print('O nome do homem mais velho tem {} anos e se chama {}.'.format(velho, homemvelho))
print('E temos {} mulheres com menos de 20 anos.'.format(cont))
