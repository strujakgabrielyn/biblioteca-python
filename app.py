from flask import Flask, request, jsonify
from entities.biblioteca import Biblioteca
from entities.livro import Livro
from entities.cliente import Cliente
from entities.emprestimo import Emprestimo
from entities.bibliotecario import Bibliotecario

app = Flask(__name__)

bibliotecario = ("João", 12345)
# Crie uma instância da Biblioteca
biblioteca = Biblioteca(bibliotecario)

# Rota raiz
@app.route('/')
def index():
    return "API da Biblioteca"

# Rotas da API
@app.route('/api/livros', methods=['GET'])
def get_livros():
    livros = biblioteca.listar_livros()
    return jsonify(livros)

@app.route('/api/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livro = Livro(novo_livro['titulo'], novo_livro['autor'], novo_livro['editora'], novo_livro['ano'])
    biblioteca.adicionar_livro(livro)
    return jsonify({'message': 'Livro adicionado com sucesso'})

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    clientes = biblioteca.listar_clientes()
    return jsonify(clientes)

@app.route('/api/clientes', methods=['POST'])
def adicionar_cliente():
    novo_cliente = Cliente(request.json['nome'], request.json['email'])
    biblioteca.adicionar_cliente(novo_cliente)
    return jsonify({'message': 'Cliente adicionado com sucesso'})

@app.route('/api/emprestimos', methods=['GET'])
def get_emprestimos():
    emprestimos = biblioteca.listar_emprestimos()
    return jsonify(emprestimos)

@app.route('/api/emprestimos', methods=['POST'])
def realizar_emprestimo():
    id_livro = request.json['id_livro']
    id_cliente = request.json['id_cliente']
    resultado = biblioteca.realizar_emprestimo(id_livro, id_cliente)
    if resultado == 'livro_emprestado':
        return jsonify({'message': 'Livro já está emprestado'})
    elif resultado == 'cliente_inadimplente':
        return jsonify({'message': 'Cliente inadimplente. Não é possível fazer o empréstimo'})
    else:
        return jsonify({'message': 'Empréstimo realizado com sucesso'})

@app.route('/api/emprestimos', methods=['PUT'])
def realizar_devolucao():
    id_livro = request.json['id_livro']
    id_cliente = request.json['id_cliente']
    resultado = biblioteca.realizar_devolucao(id_livro, id_cliente)
    if resultado == 'devolucao_atrasada':
        return jsonify({'message': 'Devolução em atraso'})
    elif resultado == 'emprestimo_nao_encontrado':
        return jsonify({'message': 'Empréstimo não encontrado'})
    else:
        return jsonify({'message': 'Devolução realizada com sucesso'})

# Executar o servidor Flask
if __name__ == '__main__':
    app.run()
