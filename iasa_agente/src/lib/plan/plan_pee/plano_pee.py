from ..plano import Plano

class PlanoPEE(Plano):
    """
    O construtor desta classe recebe e armazena uma solucao como um atributo
    privado.
    """
    def __init__(self, solucao):
        self.__solucao = solucao
    
    """
    Este método recebe um estado e retorna a accao a fazer no estado recebido,
    atualizando o atributo privado solucao.
    """
    def obter_accao(self, estado):
        """
        if self.__solucao.dimensao > 1:
            no = self.__solucao[0]
            if estado == no.estado:
                self.__solucao.remover()
                no = self.__solucao[0]
                return no.operador
        """
            
        if self.__solucao.dimensao > 1:
            if estado == self.__solucao[0].estado:
                operador = self.__solucao[1].operador
                self.__solucao.remover()
                return operador
    
    """
    Método que usa o método mostrar_solucao() da instância vista recebida passando-lhe
    a solucao obtida no construtor para que seja possível visualizar a solução de PEE.
    """
    def mostrar(self, vista):
        vista.mostrar_solucao(self.__solucao)