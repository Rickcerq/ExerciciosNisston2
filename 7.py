class Carro:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def detalhes(self):
        print('O ' +str(self.modelo) + ' da ' +str(self.marca) + ' é um carro do ano de ' +str(self.ano))

carro1 = Carro('HB20', 'Hyundai', 2012)
carro1.detalhes()