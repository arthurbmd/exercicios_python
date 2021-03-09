def metade(val=0, formatar=False, m='R$'):
    """
    Calcula a metade do valor informado.
    :param val: (opcional) valor a ser calculado.
    :param formatar: (opcional) formata o valor em formato de moeda.
    :param m: simbolo da moeda corrente.
    :return: retorna a metade valor informado
    """
    res = val / 2
    return res if not formatar else moeda(res, m)


def dobro(val=0, formatar=False, m='R$'):
    """
    Calcula o dobro do valor informado.
    :param val: (opcional) valor a ser calculado.
    :param formatar: (opcional) formata o valor em formato de moeda.
    :param m: simbolo da moeda corrente.
    :return: retorna o dobro do valor informado
    """
    res = val * 2
    return res if not formatar else moeda(res, m)


def aumentar(val=0, taxa=0, formatar=False, m='R$'):
    """
    Calcula o aumento de um valor atraves de uma taxa.
    :param val: (opcional) valor a ser calculado.
    :param taxa: (opcional) taxa a ser aumentada no valor informado.
    :param formatar: (opcional) formata o valor formatado em moeda.
    :param m: (opcional) moeda corrente.
    :return: retorna o valor aumentado na taxa informada.
    """
    res = val + (val * taxa / 100)
    return res if not formatar else moeda(res, m)


def diminuir(val=0, taxa=0, formatar=False, m='R$'):
    """
    Calcula a redução de um valor atraves de uma taxa.
    :param val: (opcional) valor a ser calculado.
    :param taxa: (opcional) taxa a ser aumentada no valor informado.
    :param formatar: (opcional) formata o valor formatado em moeda.
    :param m: (opcional) moeda corrente.
    :return: retorna o valor aumentado na taxa informada.
    """
    res = val - (val * taxa / 100)
    return res if not formatar else moeda(res, m)


def moeda(valor=0, moeda='R$'):
    """
    Formata o valor informado em formatação de moeda.
    :param valor: (opcional) valor a ser formatado
    :param moeda: (opcional) simbolo da moeda
    :return: retorna uma string com a formatação em moeda.
    """
    res = f'{moeda}{valor:>7.2f}'.replace('.', ',')
    return res


def resumo(val=0, aum=10, dim=5):
    """
    Printa na tela um resumo com aumento, redução, dobro e metade do valor informado.
    :param val: (opcional) Valor a ser calculado.
    :param aum: (opcional) Taxa de aumento
    :param dim: (opcional) Taxa de redução
    """
    print('-' * 32)
    print('RESUMO DO VALOR'.center(32))
    print('-' * 32)
    print('Preço analisado:'.ljust(20), moeda(val).rjust(10))
    print('Dobro do preço:'.ljust(20), dobro(val, True).rjust(10))
    print('Metade do preço:'.ljust(20), metade(val, True).rjust(10))
    print(f'{aum}% de aumento:'.ljust(20), aumentar(val, aum, True).rjust(10))
    print(f'{dim}% de redução:'.ljust(20), diminuir(val, dim, True).rjust(10))
    print('-' * 32)
