from estado_blocos import EstadoBlocos
from operador_pilha import OperadorPilha
import copy

"""
Esta classe herda da classe OperadorPilha e representa uma transição onde 
irá ser retirado um bloco das duas últimas pilhas e colocado na primeira.
"""
class OperadorEmpilhar(OperadorPilha):
    """
    Este método é responsável por receber um estado e retornar um novo estado
    sendo esta o resultado da aplicação deste operador sobre o estado recebido.
    Para isso é primeiramente criada uma copia da configuração do estado recebido
    através do método deepcopy da biblioteca copy, de seguida é verificado se a
    pilha em questão contém algum bloco, se não tiver é retornado um estado igual
    ao recebido, no entanto se a condição se verificar é então adicinado ao indíce
    0 da primeira pilha o primeiro bloco da pilha em questão e é depois removido
    dessa mesma pilha.
    """
    def aplicar(self, estado):
        nova_configuracao = copy.deepcopy(estado.configuracao)
        if len(nova_configuracao[self._pilha]) > 0:
            nova_configuracao[0].insert(0, nova_configuracao[self._pilha][0])
            nova_configuracao[self._pilha].remove(nova_configuracao[self._pilha][0])
        return EstadoBlocos(nova_configuracao)
        
    """
    O método repr serve para definir o que queremos que apareça na consola
    quando damos print a um objeto desta classe.
    """
    def __repr__(self):
        return "Empilhar(%s)" % self._pilha