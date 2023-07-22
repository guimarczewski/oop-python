class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

# classe Circo fechada para alterações mas aberta para extensoes, no caso as outras classes
# são extensoes da classe circo

class Malabarista:

    def apresentar_show(self):
        print('Malabarista apresentando seu show')

class Palhaco:

    def apresentar_show(self):
        print('Palhaco apresentando seu show')

class Domador:

    def apresentar_show(self):
        print('Domador apresentando seu show')

circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
# gera uma associação de classes