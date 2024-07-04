from abc import ABC, abstractmethod

class Estimulo(ABC):

    """
    Interface estímulo de um comportamento 
    """

    @abstractmethod
    def detectar(self, percepcao):
        """
        Detectar estimulo numa percepção
        @param percepcao: percepção a processar
        @return: intensidade do estímulo
        """