class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Olá ' +str(self.nome) + '!')

p1 = pessoa('Henrique', 18)
p1.falar()