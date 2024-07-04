"""
A classe Resposta representa a resposta geral de
um comportamento.
"""
class Resposta:
    """
    O construtor desta classe apenas inicializa a ação
    recebida como um atributo protected.
    """
    def __init__(self, accao):
        self._accao = accao

    """
    Este método pretende ativar a resposta, para isso
    é definida a prioridade da ação. É recebida a percecao
    a processar e a intensidade do estimulo associado.
    É finalmente retornada a ação a realizar.
    """
    def activar(self, percepcao, intensidade=0):
        self._accao.prioridade = intensidade
        return self._accao