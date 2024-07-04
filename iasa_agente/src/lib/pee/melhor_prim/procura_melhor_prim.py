from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.mec_proc.fronteira.fronteira_prioridade import FronteiraPrioridade

"""
Esta classe herda da classe ProcuraGrafo e representa um mecanismo de procura que
procura os melhores nós primeiro.
"""
class ProcuraMelhorPrim(ProcuraGrafo):
    """
    O construtor desta classe chama o construtor do seu super (MecanismoProcura)
    e passa-lhe como argumento uma nova intância da classe FronteiraPrioridade que
    por sua vez é-lhe passada um avaliador.
    De seguida esse avaliador é armazenado numa variável protegida.
    """
    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador
    
    """
    O método manter vai verificar se o nó recebido ainda não se encontra
    nos explorados ou se o custo do nó é menor que o custo do nó com o 
    mesmo estado que se encontra nos explorados.
    """   
    def _manter(self, no):
        return super()._manter(no) or no < self._explorados[no.estado]