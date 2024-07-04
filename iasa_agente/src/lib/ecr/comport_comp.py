from abc import abstractmethod

from sae import Accao
from .comportamento import Comportamento

"""
Esta classe implementa a interface Comportamento.
A classe ComportComp representa um comportamento composto, isto
é um comportamento que pode conter outros comportamentos em si,
sejam eles comportamentos simples ou compostos.
"""
class ComportComp(Comportamento):
    """
    O construtor desta classe inicializa os comportamentos deste mesmo
    comportamento através de um atributo privado.
    """
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos

    """
    Neste método o objetivo é pegar em todos os comportamentos e ativar cada
    subcomportamento, depois guardamos todas as accoes dos comportamentos e
    aplicamos o método seleccionar_accao() para a lista de accoes obtidas
    """
    def activar(self, percepcao):
        accoes = []
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            if accao:
                accoes.append(accao)
        if accoes:
            return self.seleccionar_accao(accoes)
    """
    Método abstrato
    """
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """
        Selecionar a Ação
        """