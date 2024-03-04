class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
         area = 3.14 * (self.raio ** 2)
         print ('A area é de ' + str(area))

c1 = Circulo(5)
c1.calcular_area()