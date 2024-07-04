class Trajecto:
    """
    Esta classe recebe uma solução e guarda em três atributos as localidades do
    trajeto, a dimensao do trajecto e o custo do trajeto.
    """
    def __init__(self, solucao):
        self.__localidades = []
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.__getitem__(self.__dimensao - 1).custo
        for i in range(self.__dimensao):
            no = solucao.__getitem__(i)
            self.__localidades.append(no.estado.localidade)
            
    """
    Este método mostra na consola a lista de localidades da trajeto,
    a dimensao do trajeto e o seu custo
    """
    def mostrar(self):
        print('Solução: ' + str(self.__localidades))
        print('Dimensão: ' + str(self.__dimensao))
        print('Custo: ' + str(self.__custo))