from abc import abstractmethod

"""
A classe Estado é uma classe abstrata que representa toda a informação necessária
para definir uma configuração de um sistema. Cada estado necessita de uma
identificação única. Um conjunto de estados e de transições de estado é dado
por espaço de estados.
"""
class Estado:
    @abstractmethod
    def id_valor(self):
        """
        método abstrato que define a identificação única do estado em função
        da sua informação(valor de estado).
        """
    
    """
    Este método define a identificação única de um objeto.
    """
    def __hash__(self):
        return self.id_valor()
    
    """
    Este método define a relação de igualdade consistente com a definição
    de identificação, representa a operação ==.
    """
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()