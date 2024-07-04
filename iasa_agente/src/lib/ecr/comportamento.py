from abc import ABC, abstractmethod

class Comportamento(ABC):
    """
    Interface comportamento representa qualquer tipo de comportanto, quer seja
    ele simples ou complexo.
    """

    @abstractmethod
    def activar(self, percepcao):
        """
        Este método abstrato servirá para obter uma ação com base na
        percepção recebida.
        """