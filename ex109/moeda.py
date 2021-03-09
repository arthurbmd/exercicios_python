def metade(val=0, formatar=False, m='R$'):
    res = val / 2
    return res if not formatar else moeda(res, m)


def dobro(val=0, formatar=False, m='R$'):
    res = val * 2
    return res if not formatar else moeda(res, m)


def aumentar(val=0, quant=0, formatar=False, m='R$'):
    res = val + (val * quant / 100)
    return res if not formatar else moeda(res, m)


def diminuir(val=0, quant=0, formatar=False, m='R$'):
    res = val - (val * quant / 100)
    return res if not formatar else moeda(res, m)


def moeda(valor=0, moeda='R$'):
    res = f'{moeda}{valor:>.2f}'.replace('.', ',')
    return res