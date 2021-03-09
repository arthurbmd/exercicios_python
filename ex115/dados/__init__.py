def linha(tam=40):
    return '-' * tam


def cabeçalho(msg):
    print(linha())
    print(msg.center(len(linha())))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for c, i in enumerate(lista, 1):
        print(f'\033[32m[{c}] - \033[34m{i}\033[m')
    print(linha())
    opc = leiaint('\033[32mDigite sua opção: \033[m')
    return opc


def leiaint(msg=''):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite apenas um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário interrompeu o programa.')
        else:
            break
    return int(n)


def leiafloat(msg):
    while True:
        n = str(input(msg)).strip().replace(',', '.')
        try:
            float(n)
        except Exception as error:
            print(f'\033[31mERRO! Digite um valor real válido!\033[m')
        except KeyboardInterrupt:
            print(f'O usuário interrompeu o programa.')
        else:
            break
    return float(n)
