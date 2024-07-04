from abc import abstractmethod
from mod.operador import Operador

"""
A classe OperdadorTransferir herda da classe Operador e representa
uma transição de estado, sendo essa transição no âmbito do problema
proposto do deposito. Para este respetivo problema uma transição 
tem como atributo o volume que será depois adicionado ou retirado
ao estado em que é aplicado. A esta transição está também associado
um custo, neste caso o custo é dado por o quadrado do volume transferido.
"""
class OperadorTransferir(Operador):
    """
    No construtor desta classe é recebido o volume da transição e
    de seguida é guardado como um atributo protegido.
    """
    def __init__(self, volume):
        self._volume = volume
    
    @abstractmethod
    def aplicar(self, estado):
        """
        Aplicar operador ao estado
        """
    
    """
    Este método retorna o custo da transição, sendo este o quadrado do
    volume transferido.
    """
    def custo(self, estado, estado_suc):
        return abs(estado_suc.volume - estado.volume) ** 2
        
    