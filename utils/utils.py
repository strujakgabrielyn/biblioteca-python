class DataUtils:
    @staticmethod
    def calcularDiasAtraso(data_atual, data_devolucao):
        return (data_atual - data_devolucao).days
