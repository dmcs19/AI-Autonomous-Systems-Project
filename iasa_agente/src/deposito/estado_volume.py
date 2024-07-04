from mod.estado import Estado

"""
A classe EstadoVolume herda da classe Estado e contém toda
a informação necessária para representar um estado necessário 
para o problema proposto do deposito. Sendo esta informação 
necessária o volume.
"""
class EstadoVolume(Estado):
    """
    O construtor desta classe é responsável por inicializar
    um atributo privado relativo ao volume.
    """
    def __init__(self, volume):
        self.__volume = volume
        self.__id_valor = hash(volume)
        
    """
    A propriedade volume funciona como um getter e retorna 
    o volume do estado.
    """
    @property
    def volume(self):
        return self.__volume
    
    """
    Retorna um identificador único para identificar cada estado,
    neste caso é usado o volume do estado para identificar o mesmo.
    """
    def id_valor(self):
        return self.__id_valor