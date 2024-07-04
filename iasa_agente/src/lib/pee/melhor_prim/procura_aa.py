from .procura_informada import ProcuraInformada
from .aval.avaliador_aa import AvaliadorAA

"""
Esta classe herda da classe ProcuraInformada e representa 
um mecanismo de procura A*, isto significa que este mecanismo
pretende a minimização do custo global, sendo este o custo acumulado 
até ao nó + o custo estimado até ao objetivo.
"""
class ProcuraAA(ProcuraInformada):
    """
    O construtor desta classe chama o construtor da classe
    ProcuraInformada através do super e passa-lhe como argumento 
    uma nova instância da classe AvaliadorSof.
    """
    def __init__(self):
        super().__init__(AvaliadorAA())