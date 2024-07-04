from ecr.reaccao import Reaccao
from .estimulo.estimulo_alvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

"""
A classe AproximarDir representa um comportamento simples e herda da classe
Reaccao. Esta classe será inicializada com uma variavél do tipo direccao.
"""
class AproximarDir(Reaccao):
    """
    O construtor desta classe chama através do super o construtor da
    classe Reaccao e passa-lhe uma instância do EstimuloAlvo inicializada
    com a direccao recebida neste método e passa-lhe também uma instância
    da classe RespostaMover, também ela inicializada com a direccao recebida
    no construtor desta classe.
    """
    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))