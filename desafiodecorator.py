from datetime import datetime

def meu_decorator(funcao):
    def horarioatual():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return horarioatual

@meu_decorator
def registrado():
    print('Parabéns, você foi registrado com sucesso.')

registrado()