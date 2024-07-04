import random
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

from sae import Direccao

"""
A classe Explorar representa um comportamento simples e tem a finalidade de 
explorar o ambiente de forma aleatória.
Esta classe implementa a classe Abstrata Comportamento e tem dependências
das classes RespostaMover e Direccao.
"""
class Explorar:
    """
    O método activar primeiramente obtém uma Direccao aleatória através da
    função random no Enum Direccao, de seguida é criada uma instância da
    classe RespostaMover fornecendo-lhe a direccao previamente decidida e
    depois disso é gerada uma Accao correspondente a essa instância da
    RespostaMover através do método activar(), no final é retornada a
    accao obtida por este mesmo método.
    """
    def activar(self, percepcao):
        direccao = random.choice(list(Direccao))
        resposta_mover = RespostaMover(direccao)
        return resposta_mover.activar(percepcao)