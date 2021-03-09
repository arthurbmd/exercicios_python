def metade(val=0):
    res = val / 2
    return res


def dobro(val=0):
    res = val * 2
    return res


def aumentar(val=0, quant=0):
    res = val + (val * quant / 100)
    return res


def diminuir(val=0, quant=0):
    res = val - (val * quant / 100)
    return res


def moeda(valor=0, moeda='R$'):
    res = f'{moeda}{valor:>.2f}'.replace('.', ',')
    return res