from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO

"""
A classe ProcuraLargura herda da classe ProcuraGrafo e representa uma das
vária formas possíveis de realizar a procura de uma solução de um problema.
Neste caso a procura que se pretende realizar é a procura em largura, o que 
significa que a procura decorre explorando primeiro os nós mais antigos (primeiros
a ser gerados), levando à exploração exaustiva de cada nível de procura antes da
exploração de nós a um nível de maior profundidade.
"""
class ProcuraLargura(ProcuraGrafo):
    """
    No construtor desta classe é chamado o super do construtor da classe 
    MecanismoProcura e é lhe fornecida uma nova instância da classe FronteiraFIFO.
    Foi escolhido este tipo de fronteira pois é esta fronteira que permite realizar
    uma pesquisa em largura.
    """
    def __init__(self):
        super().__init__(FronteiraFIFO())