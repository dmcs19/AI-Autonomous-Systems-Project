from pee.melhor_prim.aval.heuristica import Heuristica

"""
A classe HeuristicaManhattan herda da classe Heuristica e representa
um tipo de heuristica em específico.
"""
class HeuristicaManhattan(Heuristica):
    """
    No construtor desta clase é recebido e armazenado como um atributo privado
    o estado final.
    """
    def __init__(self, estado_final):
        self.__estado_final = estado_final
    
    """
    Este método é responsável por retornar uma estimativa do custo desde o estado recebido
    até ao estado objetivo, sendo este processo feito através da distância de manhattan.
    """
    def h(self, estado):
        return abs(estado.posicao[0] - self.__estado_final.posicao[0]) + abs(estado.posicao[1] - self.__estado_final.posicao[1])