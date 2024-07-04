class MecUtil:
    """
    No construtor desta classe é recebido o modelo, a gama e o delta_max e são
    depois guardados os 3 objetos como atributos privados.
    """
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
        
    """
    Este método tem como objetivo definir o valor da utilidade associado a cada
    estado do problema servindo depois de suporte ao cálculo da política de ação.
    Para calcular este valor é então criado um dicionário com todos os estados do
    modelo e com um valor inicializado a 0.0, de seguida é feito um ciclo while True
    que irá correr até chegar a um break. Dentro desse ciclo a primeira coisa feita é
    uma cópia do dicionário U através do método copy() e a inicialização do delta a 0.
    Depois disso é feito um ciclo for que irá percorrer todos os estados do modelo,
    dentro deste ciclo é então calculada a utilidade do estado em questão para todas
    as ações possíveis do modelo e é selecionada a maior, caso esta operação não retorne
    nenhum resultado este é colocado a 0 através do parametro default da função max.
    Após esse calculo é recalculado o delta através do máximo entre o delta já obtido
    e a diferença absoluta entre a utilidade anteriormente calculada e a utilidade obtida
    antes do cálculo.
    Quando o ciclo for terminar é então feita uma verificação para averiguar se o delta
    é menor que o delta máximo definido no construtor desta classe, se isso se verificar 
    então saímos do ciclo while através do break sendo depois retornado o dicionário que
    contém os estados e a sua utilidade.
    """
    def utilidade(self):
        S, A = self.__modelo.S, self.__modelo.A
        U = {s: 0.0 for s in S()}
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta <= self.__delta_max:
                break
        return U
        
    """
    Este método retorna a utilidade de uma determinada ação, para isso é usada
    uma fórmula dada pelo docente num dos pdf's fornecidos, sendo a soma dos resultados
    do produto da probabilidade de transição com a soma do retorno esperado com o produto
    da gama com a utilidade. 
    """    
    def util_accao(self, s, a, U):
        T, R = self.__modelo.T, self.__modelo.R
        return sum(T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn]) for sn in self.__modelo.suc(s, a))