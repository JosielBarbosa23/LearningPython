possui_passaporte = True
passagem_comprada = True
menor_de_idade = False
maior_idade = False

# Viaja apenas se possui passaporte e tiver a passagem comprada e não for menor de idade:
print((possui_passaporte and passagem_comprada) and not menor_de_idade)
# Viaja apenas se possui passaporte ou tiver a passagem comprada e não for menor de idade:
print((possui_passaporte or passagem_comprada) and not menor_de_idade)
# Viaja apenas se não possuir passaporte ou tiver a passagem comprada e não for menor de idade:
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)
# Viaja apenas se não possuir passaporte ou tiver a passagem comprada e não for menor de idade:
print((not possui_passaporte or not passagem_comprada) and menor_de_idade)

if possui_passaporte and maior_idade == True:
    print("Você está apto para viajar.")
else:
    print("Você não está apto para viajar.")