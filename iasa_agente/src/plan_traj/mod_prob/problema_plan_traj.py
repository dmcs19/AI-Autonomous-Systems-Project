from mod.problema.problema import Problema
from .estado_localidade import EstadoLocalidade
from .operador_ligacao import OperadorLigacao

"""
A classe ProblemaPlanTraj herda da classe Problema, ou seja representa um problema
em específico e é constituído por um estado inicial, operadores e um objetivo.
"""
class ProblemaPlanTraj(Problema):
    """
    O construtor desta classe chama o super construtor da classe Problema
    e passa-lhe o estado inicial com uma instância da classe EstadoLocalidade
    fornecendo-lhe a localização inicial, é também passado ao super todos os 
    operadores deste problema.
    De seguida é armazenada uma nova instância da classe EstadoLocalidade 
    passando-lhe a localização final como um atributo privado.
    """
    def __init__(self, ligacoes, loc_inicial, loc_final):
        super().__init__(EstadoLocalidade(loc_inicial),
                        [OperadorLigacao(ligacao.origem, ligacao.destino, ligacao.custo) for ligacao in ligacoes])
        self.__estado_final = EstadoLocalidade(loc_final)
    
    """
    Este método retorna true se o estado recebido como argumento 
    corresponder ao objetivo do problema.
    """
    def objectivo(self, estado):
        return estado == self.__estado_final