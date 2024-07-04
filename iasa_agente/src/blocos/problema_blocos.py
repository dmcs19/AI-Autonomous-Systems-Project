from lib.mod.problema.problema import Problema
from estado_blocos import EstadoBlocos
from operador_desempilhar import OperadorDesempilhar
from operador_empilhar import OperadorEmpilhar
"""
Esta classe herda da classe Problema e representa um problema em
específico, neste caso é o problema dos blocos apresentado pelo
docente.
"""
class ProblemaBlocos(Problema):
    """
    No construtor desta classe são recebidos com argumentos as configurações
    inicial e final para este problema.
    É chamado o construtor da classe Problema através do super() e é-lhe passado
    um objeto da classe EstadoBlocos inicializado com a configuração inicial e 
    uma lista de todos os operadores deste problema, sendos estes o empilhar e 
    desempilhar para as pilhas 1 e 2.
    De seguida é armazenada a configuração final como um atributo privado que
    irá servir para o método objectivo.
    """
    def __init__(self, config_inicial, config_final):
        super().__init__(EstadoBlocos(config_inicial), [OperadorEmpilhar(1), OperadorEmpilhar(2), OperadorDesempilhar(1), OperadorDesempilhar(2)])
        self.__config_final = config_final
        
    """
    O método objectivo retorna true se o estado recebido tiver uma
    configuração igual à configuração final passada no construtor 
    desta classe.
    """
    def objectivo(self, estado):
        return self.__config_final == estado.configuracao