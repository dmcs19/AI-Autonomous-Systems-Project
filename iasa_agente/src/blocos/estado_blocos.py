from mod.estado import Estado

"""
A classe EstadoBlocos herda da classe Estado e representa a configuração
de um estado para o problema dos blocos proposto pelo docente.
"""
class EstadoBlocos(Estado):
    """
    No construtor desta classe é recebida a configuração do estado, isto é
    a configuração dos blocos em cada pilha, esta representação é feita em
    forma de uma lista 2D. Esta configuração recebida é então armazenada
    como um atributo privado.
    Depois disso é obtido o id único do estado através a utilização da função
    hash no tuplo da configuracao com tuplos no seu interior.
    """
    def __init__(self, configuracao):
        self.__configuracao = configuracao
        self.__id_valor = hash(tuple(tuple(pilha) for pilha in configuracao))
        
    """
    Esta propriedade funciona como um getter e retorna o atributo privado
    configuração.
    """
    @property
    def configuracao(self):
        return self.__configuracao
    
    """
    Este método retorna o id único correspondente a este estado, sendo esse
    valor guardado no atributo privado id_valor.
    """
    def id_valor(self):
        return self.__id_valor