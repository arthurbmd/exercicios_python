# dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado, crie uma função chamada
# leiadinheiro() que seja capaz de funcionar como a função input() mas com uma validação de dados para aceitar apenas
# valores que sejam monetários.


from ex112.utilidadescev import moeda, dados

p = dados.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)
