
import random
import datetime
print('=====================')
print('  Empresa DEZOUDOIS  ')
print('=====================')
nome = input('Informe seu nome: ')
idade = int(input('Informe a sua idade: '))
cadastro = datetime.datetime.now()
cartoes = ['R$ 50,00', 'R$ 250,00', 'R$ 120,00']
sorteio = random.choice(cartoes)
aniv = datetime.datetime.strptime(input('Informe a data do seu aniversário: '), '%d/%m/%Y')


print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {cadastro.day}/{cadastro.month}/{cadastro.year} dentro da empresa DEZOUDOIS. \n Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {sorteio}.')
