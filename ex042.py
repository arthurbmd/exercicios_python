# refaça o desagio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# equilatero todos os lados iguais, isosceles dois lados iguais, escaleno, todos os lados diferentes

print('\033[33m=\033[m' * 30)
print('\033[36mANALISADOR DE TRIÂNGULOS')
print('\033[33m=\033[m' * 30)
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[32mSuas retas PODEM formar um triangulo\033[m', end =' ')
    if a == b == c:
        print('\033[30mEQUILÁTERO!\033[m')
    elif a == b or b == c or a == c:
        print('\033[30mISÓSCELES!\033[m')
    else:
        print('\033[30mESCALENO!\033[m')
else:
    print('\033[31mSuas retas NÃO PODEM formar um triangulo!\033[m')
