class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.perimetro = 0.0

    def calcular_perimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.lado3
        return self.perimetro
    
    def mostrar_perimetro(self):
        print('O valor do perimetro dos triangulos é de ' +str(self.perimetro))

triangulo1 = Triangulo(5, 5, 20)
triangulo1.calcular_perimetro()
triangulo1.mostrar_perimetro()