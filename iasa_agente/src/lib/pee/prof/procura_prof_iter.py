from .procura_prof_lim import ProcuraProfLim

"""
A classe ProcuraProfIter herda da classe ProcuraProfLim e representa um
mecanismo de procura em profundidade iterativa.
"""
class ProcuraProfIter(ProcuraProfLim):
    """
    O método procurar irá realizar uma procura em profundidade iterativa, isto é,
    serão feitas várias procuras em profundidade limitada de forma iterativa, ou 
    seja, são realizadas procuras em profundidade limitada com uma profundidade 
    máxima inicial de 1 onde esta profundidade máxima irá ter um incremento de 1
    no final de cada tentativa.
    Para isto é atualizada a profundidade máxima a cada iteração do ciclo e 
    procura-se a solução através do método procurar do super.
    Se for encontrada uma solução essa é retornada, senão passa para a próxima 
    iteração.
    Se chegarmos ao final e não tiver sido encontrada uma solução é retornado
    None.
    """
    def procurar(self, problema, inc_prof=1, limit_prof=100):
        for profundidade in range(0, limit_prof + 1, inc_prof):
            self.prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao