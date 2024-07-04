from .fronteira import Fronteira

"""
Esta classe herda da classe Fronteira e será usada para efetuar procuras em 
profundidade. Isto acontece pois os primeiros nós a serem explorados são os
últimos a serem adicionados à fronteira, daí o nome LIFO (last in first out).
"""
class FronteiraLIFO(Fronteira):
    """
    O método inserir desta classe insere o nó recebido no início da lista
    para que estes sejam os primeiros a serem explorados e assim cumprir uma 
    procura em profundidade.
    """
    def inserir(self, no):
        self._nos.insert(0, no)