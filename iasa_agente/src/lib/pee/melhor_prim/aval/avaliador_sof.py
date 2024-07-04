from .avaliador_heur import AvaliadorHeur

"""
Esta classe herda da classe AvaliadorHeur e representa a forma de 
avaliar a prioridade de um determinado nó, para isto esta classe 
contém um método prioridade que retorna a estimativa do custo
do percurso até ao nó através de uma função heuristica.
A heurista é escolhida através do método definir_heurista
da classe AvaliadorHeur.
"""
class AvaliadorSof(AvaliadorHeur):
    """
    Este método retorna a estimativa do custo do no até ao objetivo.
    """
    def prioridade(self, no):
        return self._heuristica.h(no.estado)