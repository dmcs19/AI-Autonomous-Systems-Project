from ..plano import Plano

"""
Esta classe herda da classe Plano e representa um plano em específico
feito para o PDM, como tal é composto pelos métodos obter_accao() e 
mostar() que são métodos abstratos da classe Plano.
"""
class PlanoPDM(Plano):
    """
    No construtor desta classe são recebidos a utilidade e a politica
    como argumentos e são depois armazenados como atributos privados.
    """
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica
    
    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)
    
    """
    Este método recebe um objeto da classe VistAmb e servirá para mostrar
    os dados necessários para melhor compreensão dos elementos do plano.
    Neste caso é primeiro feita uma verificação para ver se existe política,
    no caso de haver é então mostrada a utilidade através do método mostrar_valor()
    e é mostrada também a política através do método mostrar_politica().
    """
    def mostrar(self, vista):
        if self.__politica:
            vista.mostrar_valor(self.__utilidade)
            vista.mostrar_politica(self.__politica)