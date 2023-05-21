#Desafio: Itere sobre a lista abaixo exibindo o número do índice + nome da frunta. Porém, quando o índice for 3 exiba o 'N° do índica + nome da fruta EM PROMOÇÃO'

frutas = ['Maçã', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas,0):
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÃO')
    else:
        print(indice, fruta)