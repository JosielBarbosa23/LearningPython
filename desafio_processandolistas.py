from itertools import zip_longest
#Desafio 1: Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas, porém a pesquisa foi  encontrada em momentos diferentes. Assim, acabamos com duas listas diferentes, crie uma mensagem que diz o nome e valor do produto.
produtos = ['Monitor', 'Teclado gamer', 'Mouse gamer', 'Mouse pad', 'Gabinete']
precos = ['R$ 1.200,00', 'R$ 350,00', 'R$ 150,00', 'R$ 50,00']

for produto, preco in zip_longest(produtos, precos):
    print(f'Produto: {produto} encontrado no valor {preco}')