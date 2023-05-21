#Desafio 1: Gerador de nome
def gerador_de_nome (nome = input('Informe seu nome: ')):
    print(f'Seja bem-vindo, {nome}')

gerador_de_nome()

#Desafio 2: Calcule valores

def calculo_valores(preco, qtd):
    print(f'Total: R$ {preco*qtd:.2f}')

calculo_valores(float(input('Informe o preço do produto: ')), float(input('Informe a quantidade: ')))