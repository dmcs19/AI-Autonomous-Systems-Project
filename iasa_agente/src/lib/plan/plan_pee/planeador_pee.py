from ..planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from .mod_prob.heur_dist import HeurDist
from .mod_prob.heuristica_manhattan import HeuristicaManhattan
from .mod_prob.problema_plan import ProblemaPlan
from .plano_pee import PlanoPEE

"""
A classe PlaneadorPEE herda da classe Planeador.
"""
class PlaneadorPEE(Planeador):
    """
    No construtor desta classe é inicializado o mecanismo de procura, neste caso o 
    mecanismo usado é o de ProcuraAA. Este mecanismo é então armazenado como um
    atributo privado.
    """
    def __init__(self):
        self.__mec_pee = ProcuraAA()
    
    """
    Este método é responsável por retornar um plano PEE para o primeiro objetivo da
    lista recebida. Para que isso aconteça é primeiramente feita uma verificação para
    averiguar se o argumento recebido dos objectivos é válido, se isto se verificar 
    seguimos em frente. De seguida vamos à procura de uma solução através do método 
    procurar da classe ProcuraAA, passando-lhe como argumentos um objeto da classe
    ProblemaPlan e a heuristica pretendida.
    Se ao fazermos isso houver uma solução é então retornado um objeto da classe 
    PlanoPEE inicializado com a solução encontrada, já no caso de não haver solução
    não fazemos nada e é retornado None.
    """
    def planear(self, modelo_plan, objectivos):
        if objectivos:
            # solucao = self.__mec_pee.procurar(ProblemaPlan(modelo_plan, objectivos[0]), HeuristicaManhattan(objectivos[0]))
            solucao = self.__mec_pee.procurar(ProblemaPlan(modelo_plan, objectivos[0]), HeurDist(objectivos[0]))
            if solucao:
                print("\nHeurística: Distância Euclidiana")
                print(self.__mec_pee.complexidade_temporal())
                print(self.__mec_pee.complexidade_espacial())
                return PlanoPEE(solucao)
            