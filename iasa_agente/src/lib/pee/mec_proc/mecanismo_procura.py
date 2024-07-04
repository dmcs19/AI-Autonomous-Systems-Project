from abc import ABC, abstractmethod

from .solucao import Solucao
from .no import No

"""
A classe MecanismoProcura é abstrata e é responsável por realizar a exploração 
de opções possíveis para encontrar uma solução através de simulação prospetiva,
tendo por base uma representação interna do problema.
"""
class MecanismoProcura(ABC):
    """
    O construtor desta classe guarda a fronteira recebida e inicializa
    duas variáveis privadas a 0, sendo estas o número de nós processados
    e o número máximo de nós mantidos em memória.
    """
    def __init__(self, fronteira):
        self._fronteira = fronteira
        
        self.__nos_processados = 0
        self.__max_nos_memoria = 0
    
    """
    Este método inicia a fronteira.
    """
    def _iniciar_memoria(self):
        self._fronteira.iniciar()
    
    @abstractmethod
    def _memorizar(self, no):
        """
        método abstrato que servirá para memorizar um nó de acordo com o tipo de
        procura.
        """
    
    """
    Neste método é recebido um problema e tem como objetivo encontrar uma solução
    para este mesmo problema. Para executar a procura desta solução é usada uma
    fronteira de exploração para memorizar e gerir nós explorados.
    Primeiramente é chamado o método protected iniciar_memoria() que chama o 
    método iniciar() da fronteira que faz com que a fronteira fique com uma lista
    vazia para armazenar os nós. Depois disso é criado um nó inicial fornecendo-lhe
    o estado inicial do problema para o seu construtor.
    Após a inicialização da fronteira e do nó é chamado o método abstrato memorizar()
    desta classe passando-lhe o nó criado com o objetivo de memorizar o nó na 
    fronteira de acordo com o tipo de procura.
    De seguida é criado um ciclo while que irá percorrer enquanto a fronteira
    não estiver vazia, dentro desse ciclo while é removido o primeiro nó da
    fronteira e posteriormente guardado numa variável, se esse nó corresponder
    ao nó objetivo então é retornado o percurso, ou seja a Solução, caso isso
    não se verifique iremos percorrer todos os nós sucessores obtidos através 
    do método expandir() e de seguida memorizar esses nós para serem analisados
    posteriormente de forma igual ao seu antecessor.
    A cada iteração do ciclo while o número de nós processados aumenta em 1 e 
    é verificado se este objeto é da instância ProcuraLargura ou ProcuraCustoUnif,
    se for de alguma destas é verificado se o número de nós atualmente na fronteira
    e nos explorados ultrapassou o seu máximo, se sim esse valor máximo é alterado,
    caso não seja destas instâncias então é verificado se o número de nós atualmente
    em fronteira ultrapassou o seu máximo, se sim esse valor máximo é alterado.
    """
    def procurar(self, problema):
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not self._fronteira.vazia:
            self.__nos_processados += 1
            if hasattr(self, '_explorados'):
                self.__max_nos_memoria = max(self.__max_nos_memoria, len(self._fronteira._nos) + len(self._explorados))
            else:
                self.__max_nos_memoria = max(self.__max_nos_memoria, len(self._fronteira._nos))
            no = self._fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            else:
                for no_sucessor in self._expandir(problema, no):
                    self._memorizar(no_sucessor)
            
            
    """
    Para este método são recebidos o problema em questão e o nó que se quer 
    expandir. No final podem ser devolvidos vários nós devido à utilização do 
    yield que permite pausar a execução da função e resumir a função a partir
    do mesmo sítio onde tínhamos ficado anteriormente.
    Para isto funcionar corretamente primeiramente iremos percorrer todos os
    operados fornecidos pelo problema, de seguida geramos o estado sucessor
    aplicando o operador ao estado atual através do método aplicar(), depois 
    realizamos uma verificação para ver se o estado_sucessor existe e é válido,
    se isto acontecer é então criado e devolvido uma nova instância da classe Nó
    através do yield.
    """
    def _expandir(self, problema, no):
        for operador in problema.operadores:
            estado_sucessor = operador.aplicar(no.estado)
            if estado_sucessor:
                yield No(estado_sucessor, operador, no)
        
    """
    Retorna o número de nós processados.
    """
    def complexidade_temporal(self):
        return 'Complexidade Temporal: ' + str(self.__nos_processados)
    
    """
    Retorna o número máximo de nós mantidos em memória.
    """
    def complexidade_espacial(self):
        return 'Complexidade Espacial: ' + str(self.__max_nos_memoria)