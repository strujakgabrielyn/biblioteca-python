class ClienteServico:
    def adicionarCliente(self, biblioteca, cliente):
        biblioteca.clientes.append(cliente)

    def removerCliente(self, biblioteca, cliente):
        biblioteca.clientes.remove(cliente)

    def buscarClientePorNome(self, biblioteca, nome):
        for cliente in biblioteca.clientes:
            if cliente.nome.lower() == nome.lower():
                return cliente
        return None

    def listarClientes(self, biblioteca):
        return biblioteca.clientes