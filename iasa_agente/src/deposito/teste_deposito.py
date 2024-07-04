from problema_deposito import ProblemaDeposito
from accoes import Accoes

from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim

VOL_INICIAL = 0
VOL_FINAL = 9

def teste_deposito():
    # mecs_proc = [ProcuraCustoUnif(), ProcuraProfundidade(), ProcuraLargura(), ProcuraProfIter(), ProcuraProfLim()]
    # for mec_proc in mecs_proc:
    mec_proc = ProcuraCustoUnif()
    problema = ProblemaDeposito(VOL_INICIAL, VOL_FINAL)
    solucao = mec_proc.procurar(problema)
    if solucao:
        Accoes(solucao).mostrar()
            
teste_deposito() 

