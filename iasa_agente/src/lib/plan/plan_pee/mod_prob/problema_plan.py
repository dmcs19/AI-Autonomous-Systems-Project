from mod.problema.problema import Problema

"""
A classe ProblemaPlan herda da classe Problema e representa um
problema em específico.
"""
class ProblemaPlan(Problema):
    """
    O construtor desta classe recebe um modelo_plan e um estado_final.
    Dentro deste método é chamado o construtor da classe Problema através
    do super() e são-lhe passados o estado inicial do modelo recebido e os
    operadores desse mesmo modelo, de seguida é armazenado o estado final
    num atributo privado.
    """
    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final
        
    """
    Método que recebe um estado e verifica se esse mesmo estado corresponde ao
    objetivo, para isso é retornado true se o estado recebido for igual ao estado
    final, caso contrário retorna false.
    """
    def objectivo(self, estado):
        return estado == self.__estado_final