# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "m" ou "F'. caso esteja errado
# peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()
while sexo not in 'MF':
    print('Dados inválidos.', end=' ')
    sexo = str(input('Por favor, informe sexo: [M/F]: ')).strip().upper()
print('O sexo {} foi registrado.'.format(sexo))
