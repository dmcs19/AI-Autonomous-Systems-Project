from pee.melhor_prim.aval.heuristica import Heuristica

"""
Esta classe herda da classe Heuristica e representa a heuristica necessária
para realizar a procura A* no que toca ao problema dos blocos proposto pelo
docente.
"""
class HeurBlocos(Heuristica):
    """
    No construtor desta classe é recebido como argumento o estado final e é
    depois guardado como um atributo privado.
    """
    def __init__(self, estado_final):
        self.__estado_final = estado_final
    
    """
    Este método é responsável por retornar uma estimativa do custo desde o nó
    recebido até ao nó final correspondente ao estado final recebido no construtor.
    Neste caso em específico a estimativa do custo é dada pelo número de blocos 
    fora de posição na primeira pilha.
    Para fazer esta verificação primeiro optei por verificar se o estado recebido 
    é igual ao estado objectivo, se sim então é retornado 0 pois os blocos estão
    todos na posição correta. No entanto se isto não se verificar então é inicializada
    uma variável heur com o valor igual ao número de blocos na segunda e terceira pilha,
    isto é feito porque se um bloco se encontra noutra pilha sem ser a primeira então isso
    significa que não está na posição correta.
    De seguida é feito um ciclo for que vai percorrer a primeira pilha do estado recebido,
    cada vez que o bloco do estado recebido for diferente do bloco do estado objectivo
    na mesmo posição então é adicionado 1 à variável heur.
    No final desse ciclo for é retornada a variável heur indicando assim a estimativa
    do custo do percurso.
    """
    def h(self, estado):
        if estado == self.__estado_final:
            return 0
        heur = len(estado.configuracao[1]) + len(estado.configuracao[2])
        for i in range(len(estado.configuracao[0])):
            if estado.configuracao[0][i] != self.__estado_final.configuracao[0][i]:
                heur += 1
        return heur