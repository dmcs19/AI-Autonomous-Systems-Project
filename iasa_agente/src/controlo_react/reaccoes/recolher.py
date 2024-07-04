from ecr.hierarquia import Hierarquia
from .aproximar.aproximar_alvo import AproximarAlvo
from .evitar.evitar_obst import EvitarObst
from .explorar.explorar import Explorar

"""
A classe Recolher representa um comportamento composto através da herança da
classe Hierarquia que por sua vez herda da classe ComportComp.
"""
class Recolher(Hierarquia):
    """
    O construtor desta classe é responsável por chamar o super que por sua
    vez inicializa o construtor da classe Hierarquia. Para o super é enviada 
    a hierarquia consoante o nível de competência de cada comportamento,
    sendo o AproximarAlvo o mais alto da hierarquia seguida do EvitarObst 
    e por fim o Explorar que se encontra no nível mais baixo da hierarquia.
    """
    def __init__(self):
        super().__init__([
            AproximarAlvo(),
            EvitarObst(),
            Explorar()
        ])