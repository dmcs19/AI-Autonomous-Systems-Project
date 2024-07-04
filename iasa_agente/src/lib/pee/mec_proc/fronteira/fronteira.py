from abc import ABC, abstractmethod

"""
A classe Fronteira é uma classe abstrata e representa uma estrutura de dados
com relação de ordem. Esta classe será herdada por outras classes onde cada uma
dessas classes terá o seu critério de ordenação determinado pela estratégia de 
controlo da procura.
"""
class Fronteira(ABC):
    
    """
    O construtor desta classe apenas chama o método iniciar() desta mesma classe.
    """
    def __init__(self):
        self.iniciar()
    
    """
    Propriedade que funciona como um getter e retorna um boolean indicando assim
    se a lista de nós da fronteira de exploração se encontra vazia ou não, isto
    servirá para perceber em que momento parar de procurar na fronteira.
    """
    @property
    def vazia(self):
        return len(self._nos) == 0
    
    """
    A propriedade dimensao retorna a dimensao da fronteira.
    """
    @property
    def dimensao(self):
        return len(self._nos)
    
    """
    Este método é chamado no construtor desta classe e tem como objetivo
    inicializar o atributo protected nos como uma lista vazia.
    """
    def iniciar(self):
        self._nos = []
    
    @abstractmethod
    def inserir(self, no):
        """
        método abstrato que irá ditar em que posição o nó recebido será colocado
        na lista de nós da fronteira de exploração.
        """
    
    """
    Este método remove e retorna o nó que se encontra na primeira posição da 
    lista da fronteira de exploração através do método pop().
    """
    def remover(self):
        return self._nos.pop(0)