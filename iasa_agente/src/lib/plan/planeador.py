from abc import ABC, abstractmethod

class Planeador(ABC):
    @abstractmethod
    def planear(self, modelo_plan,  objectivos):
        """
        Método abstrato que irá retornar o plano conforme o modelo_plan e os
        objectivos recebidos.
        """