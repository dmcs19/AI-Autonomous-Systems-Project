from .fronteira import Fronteira

"""
Esta classe herda da classe Fronteira e será usada para efetuar procuras em
largura. Isto acontece pois os ultimos nós a serem explorados seram os mais
recentes na fronteira, daí o nome FIFO (first in first out).
"""
class FronteiraFIFO(Fronteira):
    """
    O método inserir desta classe insere o nó recebido no final da lista através
    do método append(), com isto os nós mais antigos permanecerão no início da
    lista o que faz com que sejam explorados antes dos mais antigos que ficarão
    no final da lista. Desta forma é realizada uma procura em largura.
    """
    def inserir(self, no):
        self._nos.append(no)