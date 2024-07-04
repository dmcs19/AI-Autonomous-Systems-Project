from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_aa import ProcuraAA
from heur_blocos import HeurBlocos
from problema_blocos import ProblemaBlocos
from estado_blocos import EstadoBlocos
from acoes import Acoes

"""
Configurações inicial e final das pilhas.
"""
BLOCOS_INICIAL = [[2, 3, 1], [], []]
BLOCOS_FINAL = [[1, 2, 3], [], []]

def teste_blocos():
    # mec_proc = ProcuraCustoUnif()
    mec_proc = ProcuraAA()
    problema = ProblemaBlocos(BLOCOS_INICIAL, BLOCOS_FINAL)
    if isinstance(mec_proc, ProcuraAA):
        heuristica = HeurBlocos(EstadoBlocos(BLOCOS_FINAL))
        solucao = mec_proc.procurar(problema, heuristica)
    else:
        solucao = mec_proc.procurar(problema)
    if solucao:
        Acoes(solucao, mec_proc).mostrar()
        
teste_blocos()
    
"""
ProcuraAA
Solução:
[[2, 3, 1], [], []]
[[3, 1], [2], []] Desempilhar(1)
[[1], [3, 2], []] Desempilhar(1)
[[], [3, 2], [1]] Desempilhar(2)
[[3], [2], [1]] Empilhar(1)
[[2, 3], [], [1]] Empilhar(1)
[[1, 2, 3], [], []] Empilhar(2)
Dimensão: 6
Custo: 8
Complexidade Temporal: 26
Complexidade Espacial: 57

ProcuraCustoUnif
Solução:
[[2, 3, 1], [], []]
[[3, 1], [2], []] Desempilhar(1)
[[1], [3, 2], []] Desempilhar(1)
[[], [3, 2], [1]] Desempilhar(2)
[[3], [2], [1]] Empilhar(1)
[[2, 3], [], [1]] Empilhar(1)
[[1, 2, 3], [], []] Empilhar(2)
Dimensão: 6
Custo: 8
Complexidade Temporal: 42
Complexidade Espacial: 66


Após olharmos e compararmos os dois resultados podemos tirar algumas conclusões.
A primeira é que tanto com a procura A* como com a procura custo uniforme os
resultados obtidos foram os mesmos no que toca à dimensão ao custo e à solução.
Esta igualdade nas soluções já era esperado pois ambos os métodos de procura 
retornam a solução ótima e como tal o resultado é o mesmo. No entanto é possível 
observar que existem diferenças no que toca à complexidade temporal e espacial,
a procura A* consegui encontrar a solução ótima mantendo a complexidade temporal
e espacial mais reduzida do que a procura custo uniforme. Esta maior eficiência
por parte da procura A* já era esperada devido ao facto de como estas procuras 
funcionam.
Dito isto podemos concluir que a procura A* é melhor do que a procura custo 
uniforme pois apesar de o resultado ser o mesmo, esta demora menos tempo a encontrar
solução e consome menos recursos.
"""