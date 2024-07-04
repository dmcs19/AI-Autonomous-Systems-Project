from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO

"""
A classe ProcuraProfundidade herda da classe MecanismoProcura e representa uma
das várias formas possíveis de realizar a procura de uma solução de um problema.
Neste caso a procura que se pretende realizar é a procura em profundidade, o que
significa que a procura decorre explorando primeiro os nós mamis recentes
(últimos a ser gerados), aumentando por isso a profundidade do ramo corrente de
procura.
"""
class ProcuraProfundidade(MecanismoProcura):
    """
    No construtor desta classe é chamado o super do construtor da classe 
    MecanismoProcura e é lhe fornecida uma nova instância da classe FronteiraLIFO.
    Foi escolhido este tipo de fronteira pois é esta fronteira que permite realizar
    uma pesquisa em profundidade.
    """
    def __init__(self):
        super().__init__(FronteiraLIFO())
        
    """
    Este método tem o objetivo de inserir o nó na fronteira correspondente a este
    mecanismo de procura, para isso é chamado o método inserir() da classe fronteira
    e fornecida a variável nó recibida por este método.
    """
    def _memorizar(self, no):
        self._fronteira.inserir(no)    