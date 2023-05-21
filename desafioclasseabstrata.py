from abc import ABC, abstractmethod

class Monitor (ABC):
    @abstractmethod
    def aumentar_claridade(self,pontos):
        pass
    @abstractmethod
    def diminuir_claridade(self,pontos):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self,pontos):
        print(f'Aumentando a claridade em {pontos} pontos.')
    def diminuir_claridade(self,pontos):
        print(f'Diminuindo a claridade em {pontos} pontos.')

monitor = MonitorFullHD()
monitor.aumentar_claridade(6)
monitor.diminuir_claridade(8)
