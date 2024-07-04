from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    @abstractmethod
    def S(self):
        """
        Método abstrato que irá retornar o conjunto de estados do mundo
        """
        
    @abstractmethod
    def A(self, s):
        """
        Método abstrato que retorna o conjunto de ações possíveis no estado recebido
        como argumento
        """
        
    @abstractmethod
    def T(self, s, a, sn):
        """
        Método abstrato que retorna a probabilidade de transição do estado recebido s para sn 
        através da ação recebida a.
        """
        
    @abstractmethod
    def R(self, s, a, sn):
        """
        Método abstrato que retorna o retorno esperado na transição de s para sn através de a.
        """
        
    @abstractmethod
    def suc(self, s, a):
        """
        Método abstrato que retorna uma lista que contém os estados sucessores obtidos
        através da aplicação da ação no estado recebiodo.
        """