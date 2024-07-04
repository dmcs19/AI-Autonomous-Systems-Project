"""
A classe Reaccao representa um comportamento simples, isto
é, não contém nenhum conjunto de comportamentos no seu interior.
Esta reação é composta por um estímulo e por uma resposta.
"""
class Reaccao:
    """
    O construtor desta classe inicializa o estímulo e a resposta desta
    reação como atributos privados.
    """
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta
    
    """
    O método activar() é responsável por numa fase inicial obter a intensidade
    do estímulo recebido e de seguida verifica se a intensidade é maior que 0,
    se for é chamado então o método activar() da classe resposta que retornará
    a ação a ter, esta ação será depois retornada por este método.
    """
    def activar(self, percepcao):
        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0:
            accao = self.__resposta.activar(percepcao, intensidade)
            return accao

