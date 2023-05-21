import os
#Criar listas com 5 frutas, 5 cores e outra com 5 linguages.
frutas =['Manga', 'Maçã', 'Banana', 'Morango', 'Laranja']
cores = ['Verde', 'Vermelho', 'Preto', 'Azul', 'Amarelo']
linguagens = ['Python', 'Java', 'SQL', 'PHP', 'C']

#Desafio 1: Criar um novo arquivo frutas.txt e inserir todas as 5 frutas da lista.

with open ('frutas.txt', 'w', encoding='utf-8', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

#Desafio 2: Imprimir na tela todas as linhas do arquivo frutas.txt.

with open('frutas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)

#Desafio 3: Adicione as cores dentro do arquivo frutas.txt sem apagar os dados das frutas.

with open('frutas.txt','a', encoding='utf-8',newline='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor) 

#Desafio 4: Crie um arquivo 'Top 5 Linguagens.txt' e popule-o de forma que cada linguagem ocupe uma linha.

with open ('top5linguagens.txt', 'w', encoding='utf-8', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)

with open('top5linguagens.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)

#Desafio BÔNUS: Crie vários arquivos vazios usando o laço FOR.
arquivos = ['musica.mp3', 'foto.jph', 'senhas.txt', 'relatorio.pdf']
for arquivo in arquivos:
    with open(arquivo, 'w', encoding='utf-8'):
        pass
