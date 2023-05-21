class Carros:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def dados_carro(self):
        print(f'O veículo da {self.marca} modelo {self.modelo} lançado no ano {self.ano} custa R$ {self.preco}.')

carro1 = Carros('Honda', 'Civic', '2023', 'R$ 80.000,00')
carro1.dados_carro()

