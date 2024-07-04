class No:
        
    def __init__(self, estado, operador=None, antecessor=None):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        
        if antecessor:
            self.__profundidade = self.__antecessor.profundidade + 1
            self.__custo = self.__antecessor.custo + \
                self.__operador.custo(self.__antecessor.estado, self.__estado)
        else:
            self.__profundidade = 0
            self.__custo = 0

        
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador 
        
    @property
    def antecessor(self):
        return self.__antecessor    
    
    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def custo(self):
        return self.__custo
    
    def __lt__(self, no):
        return self.custo < no.custo