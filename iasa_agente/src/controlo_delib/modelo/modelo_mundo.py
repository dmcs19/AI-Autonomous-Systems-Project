from mod.agente.estado_agente import EstadoAgente
from .operador_mover import OperadorMover
from sae import Direccao
from plan.modelo.modelo_plan import ModeloPlan

import math

"""
Esta classe tem como objetivo representar todo o modelo do mundo, tudo o que seja
estados, elementos e operadores do mundo estará definido nesta classe.
"""
class ModeloMundo(ModeloPlan):
    """
    No construtor desta classe ocorre a inicialização de todos os atributos,
    todos estes atributos são privados pois não queremos que sejam alterados
    fora desta classe. Primeiramente é inicializado o atributo estado a None,
    de seguida os atributos estados e elementos como uma lista e um dicionário
    vazios respetivamente, é também inicializado o atributo alterado a false e
    os operadores com uma lista que contém instâncias da classe OperadorMover
    sendo estas inicializadas com todas as direções existentes.
    """
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        self.__alterado = False
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
    
    """
    Propriedade que funciona como um getter e que retorna todos os elementos do modelo.
    """
    @property
    def elementos(self):
        return self.__elementos
    
    """
    Propriedade que funciona como um getter e que retorna o atributo privado que
    é true se o modelo tiver sido alterado ou false caso contrário.
    """
    @property
    def alterado(self):
        return self.__alterado
    
    """
    Método que retorna o estado do modelo.
    """
    def obter_estado(self):
        return self.__estado

    """
    Método que retorna todos os estados do modelo.
    """
    def obter_estados(self):
        return self.__estados

    """
    Método que retorna todos os operadores do modelo.
    """
    def obter_operadores(self):
        return self.__operadores
        
    """
    Este método recebe um estado e retorna o elemento no dicionário de elementos
    correspondente à posição do estado recebido.
    """
    def obter_elemento(self, estado):
        return self.elementos.get(estado.posicao)
    
    """
    Retorna a distancia entre o estado do agente e o estado recebido como
    argumento.
    """
    def distancia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)
    
    """
    Neste método é atualizado o atributo estado do modelo com uma nova
    instância da classe EstadoAgente onde lhe é passada a posicao da
    percepcao recebida. De seguida é feita uma verifição que averigua
    se os elementos do modelo atual são diferentes dos elementos da percepcao
    recebida como argumentos, se isto não se verificar o atributo alterado
    é colocado a False o que significa que o modelo não sofreu alterações.
    No entanto se esta condição for verdadeira os elementos do modelo 
    passam a ser iguais aos elementos da percepcao recebida, os estados 
    do modelos passam a ser novas instâncias da classe EstadoAgente onde
    lhes são passadas as posicoes da percepcao recebida e o atributo alterado
    é colocado a True o que significa que o modelo sofreu alterações.
    """
    def actualizar(self, percepcao):
        self.__estado = EstadoAgente(percepcao.posicao)
        if self.elementos != percepcao.elementos:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
            self.__alterado = True
        else:
            self.__alterado = False
        
    """
    O método mostrar recebe uma instância da classe VistaAmb e chama os métodos
    mostrar_alvos_obst e marcar_posicao onde são passados os elementos e a posicao
    do estado do modelo respetivamente.
    O método mostrar_alvos_obst serve para visualizar os alvos e os obstáculos e
    o método marcar_posicao serve para marcar uma determinada posicao.
    """
    def mostrar(self, vista):
        vista.mostrar_alvos_obst(self.elementos)
        vista.marcar_posicao(self.__estado.posicao)