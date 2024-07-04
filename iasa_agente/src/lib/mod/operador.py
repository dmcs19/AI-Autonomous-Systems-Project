from abc import ABC, abstractmethod

"""
A  classe Operador é uma classe abstrata e representa uma transição de estado,
ou seja ao ser aplicado a um estado este gera um novo estado. Ao receber o estado
atual e o estado sucessor é definido um custo de transição de estado.
"""
class Operador(ABC):
    
    """
    Interface operador que representa uma transição de estado.
    """
    
    @abstractmethod
    def aplicar(self, estado):
        """
        método abstrato que quando aplicado a um estado, gera um novo estado,
        sendo este depois retornado.
        """
        
    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        método abstrato que define o custo de transição de estado, sendo esta 
        transição do estado atual para o estado sucessor.
        """