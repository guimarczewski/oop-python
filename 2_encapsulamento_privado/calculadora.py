class Calculadora:

    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicionar(num1, num2)
        elif op == '-':
            return self.__subtrair(num1, num2)
        else:
            print('Operação inválida')

    def __adicionar(self, num1, num2):
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2

calculadora = Calculadora()
resultado_ad = calculadora.calcular('+', 3, 2)
print(resultado_ad)
resultado_sub = calculadora.calcular('-', 10, 4)
print(resultado_sub)
resultado_acesso_direto = calculadora.__adicionar(10, 4)
print(resultado_acesso_direto)