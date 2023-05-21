class Computador:
    sistema_operacional = 'Windows 10'
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def dados_computador(self):
        print(f'O computador é da marca {self.marca} com memória ram de {self.memoria_ram} e uma placa de vídeo {self.placa_de_video} e sistema operacional {self.sistema_operacional}.')
    
    @classmethod
    def configuracao_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de vídeo de baixo nível')
    
    @classmethod
    def configuracao_gamer(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de vídeo de alto nível')
    
computador1 = Computador.configuracao_escritorio('8gb')
computador1.dados_computador()
computador2 = Computador.configuracao_gamer('16gb')
computador2.dados_computador()
