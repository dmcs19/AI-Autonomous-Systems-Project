from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.simulador import Simulador

# TODO Selecionar a heuristica a partir do teste

controlo = ControloDelib(PlaneadorPEE())
Simulador(4, controlo).executar()



"""
Resultados:


Heurística: Distância de Manhattan
Complexidade Temporal: 202
Complexidade Espacial: 251

Heurística: Distância de Manhattan
Complexidade Temporal: 420
Complexidade Espacial: 251

Heurística: Distância de Manhattan
Complexidade Temporal: 807
Complexidade Espacial: 466



Heurística: Distância Euclidiana
Complexidade Temporal: 230
Complexidade Espacial: 265

Heurística: Distância Euclidiana
Complexidade Temporal: 463
Complexidade Espacial: 265

Heurística: Distância Euclidiana
Complexidade Temporal: 882
Complexidade Espacial: 458


Ao analisarmos os resultados é visível que os resultados das duas
Heurísticas são muito semelhantes, no entanto em todos os resultados
a heuristica de distância de manhattan conseguiu resultados mais 
eficientes, ou seja menores complexidades temporais e espaciais.
Este resultado era o esperado pois enquanto na heuristica de
distancia euclidiana apenas retiramos uma restrição na heuristica
de distancia de manhattan retiramos duas restrições, o que faz com 
que na heuristica de manhattan os resultados da estimativa do custo
do percurso do nó em questão até ao objetivo sejam mais próximas da
realidade, obtendo assim um resultado mais rápido e utilizando menos
memória.

"""