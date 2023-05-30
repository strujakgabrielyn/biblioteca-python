import datetime

class Emprestimo:
    def __init__(self, livro, cliente):
        self.livro = livro
        self.cliente = cliente
        self.data_emprestimo = datetime.date.today()
        self.data_devolucao = None
