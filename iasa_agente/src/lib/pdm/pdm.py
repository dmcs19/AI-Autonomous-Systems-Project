from .mec_util import MecUtil

class PDM:
    """
    No construtor desta classe é recebido o modelo, a gama e o delta max, é então
    guardado como um atributo privado.
    De seguida e criada um novo objeto da classe MecUtil passando-lhe como argumentos
    o modelo a gama e o delta_max, sendo este objeto guardado depois de um atributo
    privado.
    """
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
    
    """
    Este método recebe como argumento uma Utilidade e tem como objetivo obter a política
    ótima, que determina a selção das ações que maximizam o valor de ação em cada estado.
    """  
    def politica(self, U):
        S, A = self.__modelo.S, self.__modelo.A
        pol = {}
        for s in S():
            if A(s):
                if U[s] != 0:
                    pol[s] = max(A(s), key=lambda a: self.__mec_util.util_accao(s, a, U))
        return pol

    """
    Este método vai calcular a Utilidade, de seguida usa essa utilidade para 
    calcular a política e no final é retornado um tuplo que contém a utilidade
    e a política.
    """
    def resolver(self):
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U, pol
        