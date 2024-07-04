from abc import ABC, abstractmethod

"""
Esta classe é abstrata e servirá para representar determinadas heurísticas.
"""
class Heuristica(ABC):
    @abstractmethod
    def h(self, estado):
        """
        método abstrato que irá retornar uma estimativa do percurso
        desde o nó com o estado recebido até ao nó objetivo.
        """