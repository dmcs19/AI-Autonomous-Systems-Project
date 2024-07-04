from mod.estado import Estado

class EstadoAgente(Estado):
    """
    O construtor desta classe armazena a posicao como um atributo privado
    e inicializa o atributo privado id_valor.
    """
    def __init__(self, posicao):
        self.__posicao = posicao
        self.__id_valor = hash(posicao)
        
    """
    Funciona como um getter e retorna a posição.
    """
    @property
    def posicao(self):
        return self.__posicao
    
    """
    Método que retorna a identificação única do estado em questão. 
    """
    def id_valor(self):
        return self.__id_valor