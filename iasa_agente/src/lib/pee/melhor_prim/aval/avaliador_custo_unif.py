from pee.mec_proc.fronteira.avaliador import Avaliador

"""
Esta classe herda da classe Avaliador e tem um método prioridade que 
retorna a prioridade do nó, nesta caso a prioridade do nó é definida
pelo custo.
"""
class AvaliadorCustoUnif(Avaliador):
    """
    O método prioridade retorna a prioridade do nó recebido, neste caso
    a prioridade do nó é definida pelo custo do mesmo.
    """
    def prioridade(self, no):
        return no.custo