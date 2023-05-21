class Computador:
    sistema_operacional = 'Windows 10'
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    def dados_computador(self):
        print(f'O computador é da marca {self.marca} com memória ram de {self.memoria_ram} e uma placa de vídeo {self.placa_de_video} e sistema operacional {self.sistema_operacional}.')

computador1 = Computador('Asus', '8gb', 'NVIDIA')
computador1.dados_computador()


Computador.sistema_operacional = 'Linux'

computador2 = Computador('Dell', '8gb', 'NVIDIA')
computador2.dados_computador()

