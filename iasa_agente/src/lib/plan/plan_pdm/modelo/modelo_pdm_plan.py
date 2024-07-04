from plan.modelo.modelo_plan import ModeloPlan
from pdm.modelo.modelo_pdm import ModeloPDM

"""
Esta classe herda das classes ModeloPlan e ModeloPDM.
"""
class ModeloPDMPlan(ModeloPlan, ModeloPDM):
    """
    No construtor desta classe é recebido o modelo_plan os objetivos e o rmax, tendo este 
    um valor por defeito de 1000. Estes 3 objetos são então guardados como atributos privados.
    Depois é criado um dicionário vazio correspondente as transições e guardado como atributo
    privado. São então percorridos todos os estados e todas as ações do modelo_plan e obtidos
    todos os estados sucessores possíveis, sendo depois adicionado ao dicionario com o tuplo
    com estado e accao como chave.
    """
    def __init__(self, modelo_plan, objectivos, rmax=1000):
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax
        self.__transicoes = {}
        for s in self.S():
            for a in self.obter_operadores():
                # Modelo determinista
                sn = a.aplicar(s)
                if sn:
                    self.__transicoes[(s, a)] = sn
    
    """
    Este método retorna o estado do modelo_plan recebido no construtor.
    """
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
        
    """
    Este método retorna os estados do modelo_plan recebido no construtor.
    """
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    """
    Este método retorna os operadores do modelo_plan recebido no construtor.
    """
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
    
    """
    Este método retorna os estados do modelo_plan recebido no construtor.
    """
    def S(self):
        return self.obter_estados()
    
    """
    Este método retorna os operadores do modelo_plan recebido no construtor.
    """
    def A(self, s):
        return self.obter_operadores()
    
    """
    Este método retorna 1.0 se existir a possibilidade de quando aplicada a ação a ao estado
    s o estado sucessor ser sn, caso contrário é retornado 0.0 pois a transição é impossível.
    """
    def T(self, s, a, sn):
        return 1.0 if sn == self.__transicoes.get((s, a)) else 0.0
        
    """
    Este método retorna a recompensa da transição do estado s para sn através de a.
    Para isto é primeiro calculado o custo da transição e atribuido o inverso desse 
    valor à recompensa. De seguida é verificado se o estado sucessor está nos objetivos
    se sim é então adicinado à recompensa o valor de rmax. No final disto tudo é então 
    retornada a recompensa.
    """
    def R(self, s, a, sn):
        r = -a.custo(s, sn)
        if sn in self.__objectivos:
            r += self.__rmax
        return r
    
    """
    Este método recebe um estado e uma accao e retorna uma lista de estados sucessores que
    são resultado da ação a sobre o estado s. Se não houver estados sucessores é então 
    retornada uma lista vazia.
    """
    def suc(self, s, a):
        sucessores = self.__transicoes.get((s, a))
        return [sucessores] if sucessores and s not in self.__objectivos else []
        