from plan_traj.planeador.ligacao import Ligacao
from plan_traj.planeador.planeador_trajecto import PlaneadorTrajecto
from plan_traj.planeador.trajecto import Trajecto

from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim

# Criar a localização inicial e final do trajeto
LOC_INICIAL = 'loc-0'
LOC_FINAL = 'loc-4'

# Criar uma tabela de ligações.
ligacoes = [Ligacao('loc-0', 'loc-1', 5),
            Ligacao('loc-0', 'loc-2', 25),
            Ligacao('loc-1', 'loc-3', 12),
            Ligacao('loc-1', 'loc-6', 5),
            Ligacao('loc-2', 'loc-4', 30),
            Ligacao('loc-3', 'loc-2', 10),
            Ligacao('loc-3', 'loc-5', 5),
            Ligacao('loc-4', 'loc-3', 2),
            Ligacao('loc-5', 'loc-6', 8),
            Ligacao('loc-5', 'loc-4', 10),
            Ligacao('loc-6', 'loc-3', 15)]

"""
Nesta função é instânciado um planeador da classe PlaneadorTrajecto e depois
é obtida uma solução através do método planear da instância planeador.
De seguida é verificada se a solução é válida, se sim é criada uma instância
da classe Trajecto e é chamado o método mostrar.
"""
def teste_plan_traj():
    planeador = PlaneadorTrajecto()
    mecs_proc = [ProcuraCustoUnif(), ProcuraProfundidade(), ProcuraLargura(), ProcuraProfIter(), ProcuraProfLim()]
    for mec_proc in mecs_proc:
        solucao = planeador.planear(ligacoes, LOC_INICIAL, LOC_FINAL, mec_proc)
        if solucao:
            Trajecto(solucao).mostrar()
        
# Chama a função teste_plan_traj()   
teste_plan_traj()


# Resultados

"""
ProcuraCustoUnif
Complexidade Temporal: 11
Complexidade Espacial: 13
Solução: ['loc-0', 'loc-1', 'loc-3', 'loc-5', 'loc-4']
Dimensão: 5
Custo: 32


ProcuraProfundidade
Complexidade Temporal: 3
Complexidade Espacial: 2
Solução: ['loc-0', 'loc-2', 'loc-4']
Dimensão: 3
Custo: 55


ProcuraLargura
Complexidade Temporal: 6
Complexidade Espacial: 10
Solução: ['loc-0', 'loc-2', 'loc-4']
Dimensão: 3
Custo: 55


ProcuraProfIter
Complexidade Temporal: 7
Complexidade Espacial: 2
Solução: ['loc-0', 'loc-2', 'loc-4']
Dimensão: 3
Custo: 55


ProcuraProfLim
Complexidade Temporal: 3
Complexidade Espacial: 2
Solução: ['loc-0', 'loc-2', 'loc-4']
Dimensão: 3
Custo: 55
"""