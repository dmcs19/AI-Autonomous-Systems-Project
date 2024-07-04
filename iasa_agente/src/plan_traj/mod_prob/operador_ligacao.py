from mod.operador import Operador
from .estado_localidade import EstadoLocalidade

"""
A classe OperadorLigacao herda da classe Operador, esta classe
contém 3 atributos privados sendo eles o custo, o estado origem e
o estado destino. 
"""
class OperadorLigacao(Operador):
    """
    No construtor desta classe são armazenados os argumentos recebido 
    em atributos privados, sendo que são criadas duas instâncias da
    classe EstadoLocalidade, uma para o estado origem e uma para o
    estado destino sendo depois armazenados como atributos privados.
    """
    def __init__(self, origem, destino, custo):
        self.__estado_origem = EstadoLocalidade(origem)
        self.__estado_destino = EstadoLocalidade(destino)
        self.__custo = custo
        
    """
    O método aplicar recebe um estado e tem como objetivo gerar um novo estado
    e retorna-o, para isto é verificado se o estado recebido corresponde ao 
    estado origem, se isto acontecer é retornado o estado destino, caso isto não
    se verifique então é retornado None.
    """
    def aplicar(self, estado):
        if self.__estado_origem == estado:
            return self.__estado_destino
        return None
    
    """
    Este método retorna o custo do operador em double.
    """
    def custo(self, estado, estado_suc):
        return self.__custo