from ..planeador import Planeador
from .plano_pdm import PlanoPDM
from .modelo.modelo_pdm_plan import ModeloPDMPlan
from pdm.pdm import PDM

"""
Esta classe herda da classe Planeador e representa um planeador para
um caso específico, PDM neste caso.
"""
class PlaneadorPDM(Planeador):
    """
    No construtor desta classe são recebidos a gama e o delta_max e são guardados
    como atributos privados, estas variaveis tem valores por defeito de 0.85 e 1
    respetivamente.
    """
    def __init__(self, gama=0.85, delta_max=1):
        self.__gama = gama
        self.__delta_max = delta_max
        
    """
    Este método é responsável por receber o modelo e os objetivos e retornar o
    plano seguinte. Para gerar este plano é primeiramente criado um objeto
    da classe ModeloPDMPlan passando-lhe como argumentos o modelo_plan e os
    objectivos, de seguida é criado um objeto da classe PDM sendo-lhe passados
    o modelo_pdm previamente criado e a gama e o delta max recebidos no construtor.
    por fim são calculadas a utilidade e a politica através do método resolver que
    vão ser depois utilizadas na construção do objeto da classe PlanoPDM que irá 
    ser retornado.
    """
    def planear(self, modelo_plan, objectivos):
        modelo_pdm = ModeloPDMPlan(modelo_plan, objectivos)
        pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
        utilidade, politica = pdm.resolver()
        return PlanoPDM(utilidade, politica)