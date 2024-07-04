"""
Esta classe servirá para todos os avaliadores que usaram
heuristicas, sendo eles neste caso o avaliador da procura
sofrega e da procura A*.
"""
class AvaliadorHeur:
    """
    Este método servirá para definir a heuristica de determinado
    avaliador, sendo este recebido como argumento e guardado 
    posteriormente como um atributo protegido.
    """
    def definir_heuristica(self, heuristica):
        self._heuristica = heuristica