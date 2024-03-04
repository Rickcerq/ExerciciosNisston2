class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.valor_total = 0.0

    def calcular_total(self):
        self.valor_total = self.quantidade * self.preco
        return self.valor_total
    
    def mostrar_total(self):
        print('O valor total dos produtos é de ' +str(self.valor_total) + 'R$')

p1 = Produto('Maça' , 2.30, 13)
p1.calcular_total()
p1.mostrar_total()