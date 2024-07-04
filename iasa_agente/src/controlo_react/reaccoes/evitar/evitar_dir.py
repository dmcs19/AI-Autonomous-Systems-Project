from ecr.reaccao import Reaccao
from .estimulo.estimulo_obst import EstimuloObst

"""
A classe EvitarDir herda da classe Reaccao e representa um comportamento 
simples, esta classe é composta por um estímulo do tipo EstimuloObst, sendo
este inicializado com a direccao recebida e por uma resposta.
"""
class EvitarDir(Reaccao):
    """
    No construtor desta classe são recebidas duas variáveis, a primeira é uma
    direccao e a segunda é uma resposta.
    Dentro do método é chamado o super construtor da classe Reaccao e são 
    passados dois objetos, o primeiro é uma instância do tipo EstimuloObst que
    é inicializada com a direccao recebida quando este construtor é chamado e
    o segundo objeto é uma resposta.
    """
    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObst(direccao), resposta)