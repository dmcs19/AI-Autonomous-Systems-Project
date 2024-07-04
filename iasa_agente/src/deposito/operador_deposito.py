from mod.operador import Operador
from estado_volume import EstadoVolume

"""
A classe OperdadorDeposito herda da classe Operador e representa
uma transição de estado, sendo essa transiçã ono âmbito do problema
proposto do deposito. Para este respetivo problema uma transição 
tem como atributos o volume que será depois adicionado ou retirado
ao estado em que é aplicado. A esta transição está também associado
um custo, neste caso o custo é dado por o quadrado do volume transferido.
"""
class OperadorDeposito(Operador):
    """
    No construtor desta classe é recebido o volume da transição e
    de seguida é guardado como um atributo privado.
    """
    def __init__(self, volume):
        self.__volume = volume
        
    """
    O método aplicar é responsável por receber um estado e aplicar uma 
    transição e retornar depois o estado resultante dessa transição 
    aplicada ao estado recebido. Para isto é apenas feita uma verificação
    que é se ao alterarmos o valor do volume do estado recebido com o valor
    desta transição o seu volume se mantém acima de 0. Caso o valor seja 
    menor que 0 esse mesmo valor é passado para 0, de seguida é retornada
    uma nova instância do EstadoVolume.
    """
    def aplicar(self, estado):
        novo_volume = estado.volume + self.__volume
        if novo_volume < 0:
            novo_volume = 0
        return EstadoVolume(estado.volume + self.__volume)
    
    """
    Este método retorna o custo da transição.
    """
    def custo(self, estado, estado_suc):
        return abs(estado_suc.volume - estado.volume) ** 2
    
    """
    Mostra na consola a informação do operador, dependendo se o volume
    é positivo ou negativo.
    """
    def __repr__(self):
        if self.__volume < 0:
            return "Vazar(" + str(self.__volume*(-1)) + ")"
        return "Encher(" + str(self.__volume) + ")"
