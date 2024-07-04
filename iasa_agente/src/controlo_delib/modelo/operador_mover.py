from mod.operador import Operador
from sae import Accao
from mod.agente.estado_agente import EstadoAgente

import math

class OperadorMover(Operador):
    """
    O construtor desta classe recebe e armazena o modelo_mundo como um atributo
    privado, depois é calculado o angulo através do value da direcao recebida.
    Para além disso é criada uma nova instância da classe Accao sendo esta
    inicializada com a direccao recebida como argumento do método, esta accao
    é então guardada como um atributo privado.
    """
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value
        self.__accao = Accao(direccao)
    
    """
    Funciona como um getter e retorna o angulo do operador.
    """
    @property
    def ang(self):
        return self.__ang
    
    """
    Funciona como um getter e retorna a accao.
    """
    @property
    def accao(self):
        return self.__accao
    
    """
    Este método tem como função aplicar o operador ao estado recebido como
    argumento.
    """
    def aplicar(self, estado):
        x, y = estado.posicao
        dx = round(self.accao.passo * math.cos(self.ang))
        dy = round(-self.accao.passo * math.sin(self.ang))
        nova_posicao = x+dx, y+dy
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado
    
    """
    Este método retorna a distância entre a posicao do estado e do estado sucessor
    se esta for maior que 1, caso não seja é retornado o valor 1.
    """
    def custo(self, estado, estado_suc):
        return max(math.dist(estado.posicao, estado_suc.posicao), 1)