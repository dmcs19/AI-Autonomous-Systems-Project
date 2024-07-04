from .procura_melhor_prim import ProcuraMelhorPrim
from .aval.avaliador_custo_unif import AvaliadorCustoUnif

"""
Esta classe herda da classe ProcuraMelhorPrim e é responsável por realizar
uma procura de nós por menor custo.
"""
class ProcuraCustoUnif(ProcuraMelhorPrim):
    """
    Este construtor chama o construtor através do super e fornece-lhe uma
    nova instância da classe AvaliadorCustoUnif.
    """
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())
        