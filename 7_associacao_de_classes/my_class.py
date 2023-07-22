from typing import Type 

class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def acender(self):
        print('Acendendo {}'.format(self.__comodo))
    
    def apagar(self):
        print('Apagando {}'.format(self.__comodo))

class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('Fui dormir...')

# chamada direta do metodo acender
interruptor_quarto = Interruptor('quarto')
interruptor_quarto.acender()

# associacao da classe Pessoa com Interruptor a partir dos seus objetos
lhama = Pessoa()
lhama.acender_luz(interruptor_quarto)
lhama.apagar_luz(interruptor_quarto)
lhama.dormir()
