from abc import ABC, abstractmethod

class ModeloPlan(ABC):
    @abstractmethod
    def obter_estado(self):
        """
        Método abstrato que irá retornar o estado atual do modelo em questão.
        """
        
    @abstractmethod
    def obter_estados(self):
        """
        Método abstrato que irá retornar os estados do modelo em questão.
        """
        
    @abstractmethod
    def obter_operadores(self):
        """
        Método abstrato que irá retornar os operadores do modelo em questão.
        """