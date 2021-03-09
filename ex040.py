# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando no final de acordo
# com a média atingida: media abaixo de 5 reprovado, entre 5 e 6,9 recuperação, media 7 ou acima aprovado

print('\033[33m=\033[m' * 30)
print('\033[36mESCOLHINHA DO GUANABARA\033[m')
print('\033[33m=\033[m' * 30)

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('\033[30mCom as notas {:.1f} e {:.1f}, a média do aluno é {:.1f}.\033[m'.format(n1, n2, media))
if media < 5:
    print('\033[31mO aluno foi REPROVADO!\033[m')
elif 5 <= media < 7:
    print('\033[33mO aluno está de RECUPERAÇÃO!\033[m')
elif media >= 7:
    print('\033[32mO aluno foi APROVADO!\033[m')
