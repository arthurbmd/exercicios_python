# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

jogador = {}
gols = []
time = []
while True:
    gols.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'SsNn':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp in 'Nn':
        break
print('-=' * 20)
print('Cod.'.ljust(3), end=' ')
for i in jogador.keys():
    print(f'{i:<15}'.capitalize(), end='')
print()
print('-' * 40)
for c, j in enumerate(time):
    print(f'{c:<4}', end=' ')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    elif opc >= len(time):
        print('ERRO! Escolha um código válido.')
    else:
        print('-' * 40)
        print(f' -- LEVANTAMENTO DO JOGADOR {time[opc]["nome"]}:')
        for i, v in enumerate(time[opc]['gols'], 1):
            print(f'    No jogo {i}, fez {v} gols.')
        print(f'Total de {time[opc]["total"]} gols.')
    print('-' * 40)
print('FINALIZANDO...')
print('<<VOLTE SEMPRE!>>')
