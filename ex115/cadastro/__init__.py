from ex115.dados import *


def lerlista(nome):
    try:
        arquivo = open(nome, 'rt')
    except FileNotFoundError:
        criar_arquivo(nome)
        print('Arquivo não encontrado, então foi criado um novo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>15} anos')
    finally:
        arquivo.close()


def cadastronova(arq, nome='<desconhecido>', idade=0):
    if nome == '':
        nome = '<desconhecido>'
    try:
        arquivo = open(arq, 'at')
    except FileNotFoundError:
        criar_arquivo(arq)
        print('Arquivo não encontrado, então foi criado um novo.')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
    finally:
        arquivo.close()


def criar_arquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def arquivo_existe(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
        return True
    except:
        return False