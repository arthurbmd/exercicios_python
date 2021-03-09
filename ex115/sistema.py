# crie um pequeno sistema modularizado, que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
# os sistema só vai ter 2 opções: cadastrar uma nova pessoas e listar todas as pessoas cadastradas.

from ex115.dados import *
from ex115.cadastro import *
from time import sleep

arq = 'cadastropessoas.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)
while True:
    opc = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if opc == 1:
        lerlista(arq)
    elif opc == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade: ')
        cadastronova(arq, nome, idade)
    elif opc == 3:
        cabeçalho('FINALIZANDO... VOLTE SEMPRE!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1)


