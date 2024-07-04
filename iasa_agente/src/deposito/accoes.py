class Accoes:
    """
    O construtor recebe a solução e armazena todos os dados necesssários 
    em atributos privados.
    """
    def __init__(self, solucao):
        self.__solucao = solucao
        self.__operacoes = []
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.__getitem__(self.__dimensao - 1).custo
        for i in range(self.__dimensao - 1):
            no_sucessor = solucao.__getitem__(i+1)
            self.__operacoes.append(no_sucessor.operador)

    """
    O  método mostrar dá print na consola todas as informações necessárias
    para a compreensão do problema e da respetiva solução.
    """
    def mostrar(self):
        print('Volume Inicial: ' + str(self.__solucao.__getitem__(0).estado.volume))
        print('Volume Final: ' + str(self.__solucao.__getitem__(self.__dimensao - 1).estado.volume))
        print('Solução: ' + str(self.__operacoes))
        print('Dimensão: ' + str(self.__dimensao - 1))
        print('Custo: ' + str(self.__custo))