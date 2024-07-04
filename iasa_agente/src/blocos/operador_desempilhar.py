from estado_blocos import EstadoBlocos
from operador_pilha import OperadorPilha
import copy

"""
Esta classe herda da classe OperadorPilha e representa uma transição onde 
irá ser colocado um bloco numa das duas últimas pilhas sendo este retirada
da primeira pilha.
"""
class OperadorDesempilhar(OperadorPilha):
    """
    Este método é responsável por receber um estado e retornar um novo estado
    sendo esta o resultado da aplicação deste operador sobre o estado recebido.
    Para isso é primeiramente criada uma copia da configuração do estado recebido
    através do método deepcopy da biblioteca copy, de seguida é verificado se a
    primeira pilha contém algum bloco, se não tiver é retornado um estado igual
    ao recebido, no entanto se a condição se verificar é então adicinado ao indíce
    0 da pilha em questão o primeiro bloco da primeira pilha e é depois removido
    dessa mesma pilha.
    """
    def aplicar(self, estado):
        nova_configuracao = copy.deepcopy(estado.configuracao)
        if len(nova_configuracao[0]) > 0:
            nova_configuracao[self._pilha].insert(0, nova_configuracao[0][0])
            nova_configuracao[0].remove(nova_configuracao[0][0])
        return EstadoBlocos(nova_configuracao)
        
    """
    O método repr serve para definir o que queremos que apareça na consola
    quando damos print a um objeto desta classe.
    """
    def __repr__(self):
        return "Desempilhar(%s)" % self._pilha