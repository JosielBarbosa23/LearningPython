#Desafio 1: Use a operação adequada (break ou continue) para ao chegar no estilo "Rap", o mesmo não deve ser impresso.
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == ('Rap'):
       continue
    print(estilo)
#Desafio 2: Use a operação adequada (break ou continue) para ao chegar no estilo "Rock" a execução deve ser interrompida.
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == ('Rock'):
        break
    print(estilo)
