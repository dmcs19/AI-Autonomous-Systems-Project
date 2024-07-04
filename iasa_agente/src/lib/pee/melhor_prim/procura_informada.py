from .procura_melhor_prim import ProcuraMelhorPrim

"""
Esta classe herda da classe ProcuraMelhorPrim e representa todas
as procuras informadas. As procuras informadas tiram partido de
conhecimento do domínio do problema para ordenar a fronteira de
exploração.
"""
class ProcuraInformada(ProcuraMelhorPrim):
    """
    Neste método é definida a heuristica no avaliador e de seguida é
    chamado o método procurar da classe ProcuraMelhorPrimeiro através
    do super.
    """
    def procurar(self, problema, heuristica):
        self._heuristica = heuristica
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)