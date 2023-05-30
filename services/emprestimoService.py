import datetime
from entities.emprestimo import Emprestimo

class EmprestimoServico:
    def realizarEmprestimo(self, biblioteca, livro, cliente):
        if livro.disponibilidade:
            emprestimo = Emprestimo(livro, cliente)
            livro.disponibilidade = False
            biblioteca.emprestimos.append(emprestimo)

    def realizarDevolucao(self, biblioteca, livro):
        emprestimos = biblioteca.emprestimos
        for emprestimo in emprestimos:
            if emprestimo.livro == livro and emprestimo.data_devolucao is not None and emprestimo.data_devolucao < datetime.date.today():
                emprestimos.remove(emprestimo)
                break
        livro.disponivel = True



    def buscarEmprestimoPorCliente(self, biblioteca, cliente):
        emprestimos_cliente = []
        for emprestimo in biblioteca.emprestimos:
            if emprestimo.cliente == cliente:
                emprestimos_cliente.append(emprestimo)
        return emprestimos_cliente

    def listarEmprestimosEmAtraso(self, biblioteca):
        emprestimos_atraso = []
        data_atual = datetime.date.today()
        for emprestimo in biblioteca.emprestimos:
            if emprestimo.data_devolucao is None and emprestimo.data_emprestimo < data_atual:
                emprestimos_atraso.append(emprestimo)
        return emprestimos_atraso
