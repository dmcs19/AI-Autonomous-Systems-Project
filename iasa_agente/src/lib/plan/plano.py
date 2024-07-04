from abc import ABC, abstractmethod

class Plano(ABC):
    @abstractmethod
    def obter_accao(self, estado):
        """
        Método abstrato que retorna o operador para fazer a accao no estado recebido.
        """
        
    @abstractmethod
    def mostrar(self, vista):
        """
        Método abstrato que servirá para mostrar os dados necessários acerca do plano 
        em questão.
        """