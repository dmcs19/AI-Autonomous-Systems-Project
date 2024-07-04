from sae import Elemento

"""
Esta classe tem como objetivo gerar um conjunto de objetivos.
"""
class MecDelib:
    """
    O construtor desta classe recebe como argumento um modelo_mundo e 
    guarda-o como um atributo privado.
    """
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
    
    """
    Este método retorna uma lita de objetivos ordenada por distância 
    ao agente. Para isso é percorrida a lista de estados obtida através 
    do método obter_estados() da classe modelo_mundo e é verificado se
    o elemento de cada estado é o alvo. De seguida se a lista criada não 
    estiver vazia é utilizada a função sort que irá ordenar a lista através
    do método distancia da classe modelo_mundo.
    """
    def deliberar(self):
        objetivos = [estado for estado in self.__modelo_mundo.obter_estados()\
            if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        if objetivos:
            objetivos.sort(key=self.__modelo_mundo.distancia)
            return objetivos