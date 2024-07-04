from ecr.hierarquia import Hierarquia
from .resposta.resposta_evitar import RespostaEvitar
from .evitar_dir import EvitarDir
from sae import Direccao


"""
A classe EvitarObst representa um comportamento composto e herda
da classe Hierarquia, o que significa que é composta por uma
lista de comportamentos no seu interior de forma hierárquica.
Esta classe tem um atributo privado do tipo RespostaEvitar.
"""
class EvitarObst(Hierarquia):
    """
    No construtor desta classe é inicializado o atributo privado resposta
    com uma nova instância da classe RespostaEvitar.
    Para além disso é chamado o super do construtor da classe Hierarquia em
    que é passada uma lista com comportamentos no seu interior, neste caso
    a lista é composta por 4 objetos da classe EvitarDir onde cada uma 
    destas instâncias são inicializadas com as 4 direções possíveis e com
    o atributo privado resposta previamente criado.
    """
    def __init__(self):
        self.__resposta = RespostaEvitar()
        super().__init__([
            EvitarDir(direccao, self.__resposta)
            for direccao in Direccao
        ])