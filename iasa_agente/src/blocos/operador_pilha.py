from abc import abstractmethod
from mod.operador import Operador

"""
Esta classe herda da classe Operador e representa uma transição de estado, sendo
essa transição no ambito do problema dos blocos proposto pelo docente. Para este 
respetivo problema uma transição tem como atributo a pilha a que o bloco será 
adicionado ou removido. A esta transição está também associado um custo, neste
caso o custo é dado pelo número da pilha que é feita a transição.
"""
class OperadorPilha(Operador):
    """
    No construtor desta classe é recebido a pilha com a qual será feita a transição
    sendo esse valor guardado como um atributo protegido.
    """
    def __init__(self, pilha):
        self._pilha = pilha
        
    @abstractmethod
    def aplicar(self, estado):
        """
        Aplicar o operador ao estado
        """

    """
    Este método retorna o custo da transição, sendo este definido pelo número da pilha
    na qual será feita a transição.
    """  
    def custo(self, estado, estado_suc):
        return self._pilha