from ecr.estimulo import Estimulo
from sae import Elemento

"""
Esta classe implementa a interface Estímulo e é responsável por
detetar o estímulo alvo na percepcao.
"""
class EstimuloAlvo(Estimulo):
    """
    O construtor desta classe é inicializada com a direccao e com a gama,
    sendo estes dois atributos guardados como privados.
    O gama tem um valor de 0.9 por omissão pois o seu valor tem de 
    estar entre 0 e 1.
    """
    def __init__(self, direccao, gama=0.9):
        self.__direccao = direccao
        self.__gama = gama
        
    """
    Este método recebe a percepcao, que servirá para saber o elemento e
    a distância. Para isso pesquisa-se no atributo per_dir da percepcao
    que é um dicionário que contém a direccao e um tuplo com o elemento
    a distancia e a posição. Ao pesquisar pelo atributo privado direccao
    nesse dicionário são retornados os valores das 3 variáveis anteriormente
    referidas, no entanto apenas precisamos do elemento e da distancio
    pelo que guardamos o valor da posicao numa variável descartável.
    Após a atribuição dos valores a estas variáveis é retornada a intensidade,
    sendo esta a função exponencial inversa da distância se o elemento 
    previamente obtido seja do tipo ALVO, caso contrário é retornado o
    valor 0.
    Esta intensidade vai ser depois usada na classe AproximarDir.
    """
    def detectar(self, percepcao):
        elem, dist, _ = percepcao.per_dir[self.__direccao]
        return self.__gama ** dist if elem == Elemento.ALVO else 0