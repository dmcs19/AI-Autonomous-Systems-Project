from lib.mod.problema.problema import Problema
from estado_volume import EstadoVolume
from operador_encher import OperadorEncher
from operador_vazar import OperadorVazar
from operador_deposito import OperadorDeposito

"""
Esta classe herda da classe Problema e representa um problema especifico,
neste caso o problema foi dado pelo docente.
"""
class ProblemaDeposito(Problema):
    """
    O construtor desta classe recebe o volume inicial e o
    volume final, é chamado o construtor da classe Problema e são passados
    os operadores criados e uma nova instância da classe EstadoVolume inicializada
    com o volume inicial recebido. De seguida é armazenado o valor do 
    volume final pretendido como um atributo privado.
    Existem duas linhas que realizam a mesma coisa porém na primeira foram usados
    dois operadores diferentes para encher e vazar o deposito, sendo estes operadores
    da autoria do professor. Na segunda linha foram usados 4 operadores do mesmo tipo
    que suportam tanto o ato de encher como o de vazar, sendo este atribuido através
    do valor recebido quando o operador é instânciado, este operador foi da minha
    autoria.
    """
    def __init__(self, vol_inicial, vol_final):
        super().__init__(EstadoVolume(vol_inicial), [OperadorEncher(2),OperadorEncher(3),OperadorVazar(2),OperadorVazar(3)])
        # super().__init__(EstadoVolume(vol_inicial), [OperadorDeposito(2),OperadorDeposito(3),OperadorDeposito(-2),OperadorDeposito(-3)])
        self.__vol_final = vol_final
        
    """
    O método objectivo recebe um estado e verifica se esse estado corresponde
    ao estado objetivo do problema, esta verificação é feita através do volume.
    """
    def objectivo(self, estado):
        return estado.volume == self.__vol_final