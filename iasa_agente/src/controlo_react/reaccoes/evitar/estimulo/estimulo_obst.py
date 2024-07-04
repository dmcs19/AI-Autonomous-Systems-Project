from ecr.estimulo import Estimulo

"""
Esta classe implementa a Interface Estimulo e é responsável por detetar o
estímulo obstaculo e a sua respetiva intensidade
"""
class EstimuloObst(Estimulo):
    """
    No construtor desta classe são recebidas duas variáveis sendo a primeira
    a direccao e a segunda a intensidade, ambos os valores são guardados
    como atributos privados.
    Neste caso a intensidade tem o valor de 1 por omissão.
    """
    def __init__(self, direccao, intensidade=1):
        self.__direccao = direccao
        self.__intensidade = intensidade

    """
    O método detectar recebe uma percepcao e verifica se existe contacto com 
    o obstaculo, caso exista é retornada a sua intensidade, senão é retornado 0.
    """
    def detectar(self, percepcao):
        return self.__intensidade if percepcao.contacto_obst(self.__direccao) else 0