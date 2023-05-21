#Desafio: Extraia as cores da lista a seguir e coloque as em uma nova lista. Finalmente imprima a nova lista na tela.
pinturas = [

    ['Pintura Classica', 'Azul', 1857],

    ['Pintura Medieval', 'Vermelha', 1867],

    ['Pintura Moderna', 'Verde', 1897]

]
def cores(pinturas):
    return pinturas[1]

map(cores, pinturas)
lista_de_cores = list(map(cores, pinturas))
print(lista_de_cores)