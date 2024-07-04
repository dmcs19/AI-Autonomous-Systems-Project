from .avaliador_heur import AvaliadorHeur

"""
Esta classe herda da classe AvaliadorHeur e será usada para a 
procura A*, esta procura tem como objetivo a minimização do
custo global. Para isto esta classe atribui ao no uma prioridade
resultante do custo acumulado até ao nó mais o custo estimado até
ao objetivo. 
"""
class AvaliadorAA(AvaliadorHeur):
    """
    Este método retorna a soma do custo do nó com a estimativa do custo
    desde o nó até ao nó objetivo.
    """
    def prioridade(self, no):
        return no.custo + self._heuristica.h(no.estado)