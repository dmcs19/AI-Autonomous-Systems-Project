from ecr.resposta import Resposta
from sae import Accao


"""
A classe RespostaMover tem herança da classe Resposta e tem dependência da
classe Accao.
"""
class RespostaMover(Resposta):
    """
    O construtor desta classe chama o contrutor do seu parente (Resposta) 
    através do super() fornecendo-lhe uma nova instância da classe a Accao
    inicializada com a direccao recebida pelo construtor.
    """
    def __init__(self, direccao):
        super().__init__(Accao(direccao))