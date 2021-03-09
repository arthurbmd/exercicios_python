def leiadinheiro(msg):
    while True:
        din = str(input(msg)).strip().replace(',', '.').replace('R$', '')
        try:
            float(din)
            break
        except:
            print(f'\033[31mERRO! \"{din}\" é um valor inválido.\033[m')
    return float(din)
