class Pessoa: # Substantivo

    def __init__(self, name: str, idade: int) -> None: # Verbo
        self.name = name # Substantivo
        self.idade = idade # Substantivo

    def dirigir(self, veiculo: str) -> None: # Verbo
        print('Dirigindo um(a) {}'.format(veiculo))

    def cantar(self) -> None: # Verbo
        print('Lalala')
    
    def apresentar_idade(self) -> int: # Verbo
        return self.idade