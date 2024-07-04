class Acoes:
    """
    O construtor desta classe recebe a solucao e o mecanismo de procura e guarda-os
    como atributos privados. É também inicializada uma lista privada com o nome operacoes
    que ira armazenar todos os operadores usados na solução. Depois é obtida a dimensão da
    solução e o seu custo sendo estes valores também armazenados como atributos privados.
    Por fim é feito um ciclo for que percorra a solucao no a no e que obtenha e adicione
    todos os operadores usados à lista feita anteriormente.
    """
    def __init__(self, solucao, mec_proc):
        self.__solucao = solucao
        self.__mec_proc = mec_proc
        self.__operacoes = []
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.__getitem__(self.__dimensao - 1).custo
        for i in range(self.__dimensao - 1):
            no_sucessor = solucao.__getitem__(i+1)
            self.__operacoes.append(no_sucessor.operador)
            
    """
    Este método é responsável por mostrar na consola as informações necessárias e 
    pedidas pelo docente de modo a facilitar a compreensão do problema e da respetiva
    solução.
    """
    def mostrar(self):
        print("Solução:")
        print(str(self.__solucao.__getitem__(0).estado.configuracao))
        for i in range(1, self.__dimensao):
            print(str(self.__solucao.__getitem__(i).estado.configuracao) + " " + str(self.__operacoes[i-1]))
        print('Dimensão: ' + str(self.__dimensao - 1))
        print('Custo: ' + str(self.__custo))
        print(self.__mec_proc.complexidade_temporal())
        print(self.__mec_proc.complexidade_espacial())
