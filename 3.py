class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print('A area é de ' + str(area))

r1 = Retangulo(120, 60)
r1.calcular_area()