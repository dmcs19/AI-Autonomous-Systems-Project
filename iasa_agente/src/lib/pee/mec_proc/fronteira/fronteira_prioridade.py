from .fronteira import Fronteira

from heapq import heappush, heappop

"""
A classe FronteiraPrioridade herda da classe Fronteira onde os nós seram organizados
de acordo com a sua prioridade.
"""
class FronteiraPrioridade(Fronteira):
    """
    O construtor desta classe chama o construtor da classe Fronteira através 
    do super para que esta fronteira seja iniciada e de seguida
    armazena o argumento avaliador num atributo privado.
    """
    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador
    
    """
    Este método tem como objetivo inserir o nó recebido na fronteira de acordo
    com a prioridade deste nó.
    Para isto primeiramente é obtida a prioridade do nó através do método
    prioridade() da interface Avaliador.
    De seguida será introduzido um tuplo que contém a prioridade e o nó na
    lista de nós da fronteira através do método heappush
    """
    def inserir(self, no):
        prioridade = self.__avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))
    
    """
    Este método servirá para remover um nó da lista de nós que tem a maior prioridade.
    Primeiro é removido um tuplo através do método heappop onde é atribuido ao
    ao primeiro elemento do tuplo uma variável incógnita e à segunda uma variável
    no, de seguida é retornada a variável no.
    """
    def remover(self):
        _, no = heappop(self._nos)
        return no