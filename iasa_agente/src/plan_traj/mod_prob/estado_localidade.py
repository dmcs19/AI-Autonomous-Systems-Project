from mod.estado import Estado

"""
A classe EstadoLocalidade herda da classe Estado e tem um atributo
publico localidade do tipo string com a propriedade read-only.
Para este problema em específico foi escolhida uma localidade apenas
com uma localidade atribuída pois é a única coisa necessária para 
definir um estado.
"""
class EstadoLocalidade(Estado):
    """
    O construtor desta classe armazena a localidade recebida num
    atributo privado.
    """
    def __init__(self, localidade):
        self.__localidade = localidade
        
    """
    Funciona como um getter e retorna a localidade do EstadoLocalidade.
    """
    @property
    def localidade(self):
        return self.__localidade    
    
    """
    Retorna o número inteiro da localidade. Servindo depois para 
    diferenciar cada localidade.
    """
    def id_valor(self):
        return int(self.__localidade[-1])