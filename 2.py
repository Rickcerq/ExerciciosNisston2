class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor

    def detalhes(self):
        print ('O livro ' + str(self.nome) + ' foi escrito por ' + str(self.autor))

livro1 = Livro('O Senhor dos anéis', 'J.R.R Tolkien')
livro1.detalhes()