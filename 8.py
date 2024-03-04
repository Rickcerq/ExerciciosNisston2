class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2)/2
        return self.media
    
    def mostrar_media(self):
        print(' A media de ' +str(self.nome) + ' é de ' + str(self.media))

aluno1 = Aluno('Gustavo', 6.5, 8)
aluno1.calcular_media()
aluno1.mostrar_media()