import datetime

from entities.biblioteca import  Biblioteca
from entities.livro import Livro
from entities.cliente import Cliente
from entities.bibliotecario import Bibliotecario

from services.clienteService import ClienteServico
from services.emprestimoService import EmprestimoServico
from services.livroService import LivroServico

from utils.utils import DataUtils


def main():
    bibliotecario = Bibliotecario("João", 12345)

    biblioteca = Biblioteca(bibliotecario)

    livro_servico = LivroServico()
    cliente_servico = ClienteServico()
    emprestimo_servico = EmprestimoServico()

 
    livro1 = Livro("Livro 1", "Autor 1", "Editora A", 2021)
    livro2 = Livro("Livro 2", "Autor 2", "Editora B", 2022)
    livro3 = Livro("Livro 3", "Autor 3", "Editora C", 2023)
    livro4 = Livro("Livro 4", "Autor 4", "Editora D", 2023)
    livro_servico.adicionarLivro(biblioteca, livro1)
    livro_servico.adicionarLivro(biblioteca, livro2)
    livro_servico.adicionarLivro(biblioteca, livro3)
    livro_servico.adicionarLivro(biblioteca, livro4)

    cliente1 = Cliente("Cliente 1", "Endereço 1", "123456789")
    cliente2 = Cliente("Cliente 2", "Endereço 2", "987654321")
    cliente_servico.adicionarCliente(biblioteca, cliente1)
    cliente_servico.adicionarCliente(biblioteca, cliente2)

    emprestimo_servico.realizarEmprestimo(biblioteca, livro1, cliente1)
    emprestimo_servico.realizarDevolucao(biblioteca, livro1)


    livros_disponiveis = livro_servico.listarLivrosDisponiveis(biblioteca)
    for livro in livros_disponiveis:
        print(f"Livro disponível: {livro.titulo}")


    cliente = cliente_servico.buscarClientePorNome(biblioteca, "Cliente 0")
    if cliente:
        print(f"Cliente encontrado: {cliente.nome}")


    data_atual = datetime.date.today()
    data_devolucao = datetime.date(2023, 5, 28)
    dias_atraso = DataUtils.calcularDiasAtraso(data_atual, data_devolucao)
    print(f"Dias de atraso: {dias_atraso}")

if __name__ == "__main__":
    main()
