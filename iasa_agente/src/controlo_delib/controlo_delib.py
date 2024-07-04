from sae import Controlo
from .modelo.modelo_mundo import ModeloMundo
from .mec_delib import MecDelib

class ControloDelib(Controlo):
    """
    O construtor desta classe recebe como argumento um planeador e guarda-o como
    um atributo privado. De seguida é criada e armazenada uma nova instância da
    classe ModeloMundo que é posteriormente enviada como argumento da instância
    criada da classe MecDelib. Para além disso são inicializados 2 atributos privados
    sendo estes os objetivos e o plano, ambos os atributos são inicializados a None.
    """
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__objectivos = None
        self.__plano = None
    
    """
    Método que recebe uma percepcao e produz uma accao.
    Este método assimila a percepcao e de seguida verifica se é necessário 
    reconsiderar, se não for necessário é chamado de imediato o método executar
    se for necessário é deliberado e planeado antes de executar.
    """
    def processar(self, percepcao):
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        self.__mostrar()
        accao = self.__executar()
        return accao
    
    """
    ESte método atualiza o modelo do mundo através do método actualizar passando-lhe
    a percepcao recebida como argumento.
    """
    def __assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)
    
    """
    Este método retorna true se for necessário reconsiderar. É necessário reconsiderar
    se o modelo_mundo tiver sido alterado ou se o plano não existir.
    """
    def __reconsiderar(self):
        return self.__modelo_mundo.alterado or not self.__plano
    
    """
    Este método atualiza os objetivos com o que o mecanismo de deliberação produzir.
    """
    def __deliberar(self):
        self.__objectivos = self.__mec_delib.deliberar()
    
    """
    Método que atualiza o plano através do método planear da classe Planeador
    fornecendo-lhe o modelo_mundo e os objetivos.
    """
    def __planear(self):
        if self.__objectivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        else:
            self.__plano = None
    
    """
    Este método é responsável por obter a accao do plano.
    """
    def __executar(self):
        if self.__plano:
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            if operador:
                return operador.accao
    
    """
    Este método mostra o modelo_mundo e o plano.
    """
    def __mostrar(self):
        self.vista.limpar()
        self.__modelo_mundo.mostrar(self.vista)
        if self.__plano:
            self.__plano.mostrar(self.vista)