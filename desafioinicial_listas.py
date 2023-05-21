#Desafio 1: Crie e imprima uma lista dos 3 objetos que você mais usa no dia a dia.

objetos_dia = ['Fone de ouvido', 'Celular', 'Caneta']
print(objetos_dia)

#Desafio 2: Usando apenas uma linha de código, crie uma lista de 10 a 131.

faixanumero = list(range(10, 132))
print(faixanumero)

#Desafio 3: Imprima na tela o resultado da combinação da lista do desafio 1 e 2.

print(objetos_dia + faixanumero)
#Desafio 4: Crie uma matriz que tenha o nome dos 3 objetos que você mais usa, só que agora, dentro de cada item você irá adicionar um valor em reais do objeto e imprima na tela.

precos_indices = [['Fones de ouvido',50], ['Celular',1.400], ['Caderno',50]]
print(precos_indices)
print(precos_indices[1][0])
