from turtle import Turtle
# Inicializando o turtle
t = Turtle()

def obter_distancia():
    resposta = int(input('Informe a distância que deseja percorrer: '))
    return resposta

def rotacao_turtle(t):
    lado = input('A tartaruga deve rotacionar para direita, esquerda ou não rotacionar? [D, E ou N]')
    if lado == ('D'):
        rotacionar_direita(t)
    elif lado == ('E'):
        rotacionar_esquerda(t)

def rotacionar_direita(t):
    rotacione = int(input('Informe a rotação que deve ocorrer para a direita: '))
    t.right(rotacione)     

def rotacionar_esquerda(t):
    rotacione = int(input('Informe a rotação que deve ocorrer para a esquerda: '))
    t.left(rotacione)  
# Definindo a velocidade
t.speed(1)
print('=================================')
print('Seja bem-vindo ao minigame TURTLE')
print('=================================')
while True:
    direcao = input('Você deseja andar para frente ou para trás? [F/T]')
    if direcao == ('F'):
        distancia = obter_distancia()
        rotacao = rotacao_turtle(t)
        if rotacao == ('N'):
            continue
        t.forward(distancia)
    if direcao == ('T'):
        distancia = obter_distancia()
        rotacao = rotacao_turtle(t)
        if rotacao == ('N'):
           continue
        t.backward(distancia)

    resposta = input('Deseja continuar jogando? [S/N]')
    if resposta == ('S'):
        continue
    elif resposta == ('N'):
        break
