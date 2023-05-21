import json

dados_usuario = """{
    "name": "John Smith",
    "age": "30",
    "City": "New York",
    "IsStudent": True,
    "gpa": 3.5
}"""

with open ('desafiodois.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados_usuario, arquivo_json)

    

