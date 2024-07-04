from pee.melhor_prim.aval.heuristica import Heuristica

import math

"""
A classe HeurDist herda da classe Heuristica.
"""
class HeurDist(Heuristica):
    """
    No construtor desta clase é recebido e armazenado como um atributo privado
    o estado final.
    """
    def __init__(self, estado_final):
        self.__estado_final = estado_final
       
    """
    Método que retorna a distância em linha reta do estado recebido até ao estado
    final através da função dist da biblioteca math.
    """ 
    def h(self, estado):
        return math.dist(estado.posicao, self.__estado_final.posicao)
