from entities.livro import Livro

class LivroServico:
    def adicionarLivro(self, biblioteca, livro):
        biblioteca.livros.append(livro)

    def removerLivro(self, biblioteca, livro):
        biblioteca.livros.remove(livro)

    def buscarLivroPorTitulo(self, biblioteca, titulo):
        for livro in biblioteca.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def listarLivrosDisponiveis(self, biblioteca):
        livros_disponiveis = []
        for livro in biblioteca.livros:
            if livro.disponibilidade:
                livros_disponiveis.append(livro)
        return livros_disponiveis