from abc import ABC, abstractmethod

class Avaliador(ABC):
    """
    A classe Avaliador é uma interface com o método prioridade que tem
    como objetivo definir a prioridade de um nó de acordo com determinados
    critérios.
    """
    
    @abstractmethod
    def prioridade(self, no):
        """
        Método abstrato que servirá para retornar a prioridade correspondente
        ao nó recebido de acordo com determinados critérios.
        """