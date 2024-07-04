from .procura_informada import ProcuraInformada
from .aval.avaliador_sof import AvaliadorSof

"""
Esta classe herda da classe ProcuraInformada e representa 
um mecanismo de procura sofrega, isto significa que este mecanismo
pretende a minimização da estimativa de custo para atingir o objetivo
sem ter em conta o custo do percurso explorado, sabemos também que
este mecanismo produz soluções sub-ótimas.
"""
class ProcuraSofrega(ProcuraInformada):
    """
    O construtor desta classe chama o construtor da classe
    ProcuraInformada através do super e passa-lhe como argumento 
    uma nova instância da classe AvaliadorSof.
    """
    def __init__(self):
        super().__init__(AvaliadorSof())