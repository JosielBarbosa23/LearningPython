import json

with open ('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)

#Desafio 1: Imprimir o e-mail do usuario de id 2.

print(f'O e-mail do usurário ', data["user"][1]["name"], ' é ', data["user"][1]["email"])

#Desafio 2: Imprimir a city do usuario de id 1.

print(f'A cidade do usuário ', data["user"][0]["name"], ' é ', data["user"][0]["address"]["city"])

#Desafio 3: Imprimir o total do pedido do usuario de id 2.

print(f'O total do pedido do usuário ', data["user"][1]["name"], ' é ', data["user"][1]["orders"][0]["total"])
