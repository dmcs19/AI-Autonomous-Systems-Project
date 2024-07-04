from ecr.prioridade import Prioridade
from .aproximar_dir import AproximarDir
from sae import Direccao


"""
A classe AproximarAlvo tem uma relação de herança com a Prioridade que por
sua vez tem uma relação de herança com o ComportComp.
O AproximarAlvo representa um comportamento composto que contém 4 comportamentos
simples na sua composição.
"""
class AproximarAlvo(Prioridade):
    """
    O construtor desta classe tem como função criar 4 comportamentos simples,
    sendo estes da classe AproximarDir com 4 direções diferentes.
    Depois estes comportamentos são colocados numa lista e passados para
    o construtor da classe Prioridade.
    """
    def __init__(self):
        aproximardir1 = AproximarDir(Direccao.NORTE)
        aproximardir2 = AproximarDir(Direccao.SUL)
        aproximardir3 = AproximarDir(Direccao.ESTE)
        aproximardir4 = AproximarDir(Direccao.OESTE)
        comportamentos = [aproximardir1, aproximardir2, aproximardir3, aproximardir4]
        super().__init__(comportamentos)