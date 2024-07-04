from .procura_profundidade import ProcuraProfundidade

"""
A classe ProcuraProfLim herda da classe ProcuraProfundidade e representa um
mecanismo de procura em profundidade limitada.
"""
class ProcuraProfLim(ProcuraProfundidade):
    """
    O construtor desta classe recebe a variável que representa a profundidade
    máxima e armazena-a num atributo público. O valor da profundidade máxima
    tem o valor se 100 por defeito, isto é, se nenhum valor for passado a esta 
    classe a variável toma o valor de 100. Para além disso é chamado o construtor
    da classe ProcuraProfundidade através do super.
    """
    def __init__(self, prof_max=100):
        self.__prof_max = prof_max
        super().__init__()
    
    """
    Esta propriedade servirá como um getter para o atributo prof_max.
    """
    @property
    def prof_max(self):
        return self.__prof_max
    
    """
    Isto serve como um setter onde quando é utilizado o nome do atributo e fornecido
    um valor de seguida, o valor deste atributo é atualizado.
    """
    @prof_max.setter
    def prof_max(self, valor):
        self.__prof_max = valor

    """
    O método expandir é um método protegido e tem o objetivo de expandir o nó 
    recebido se a sua profundidade for inferior à profundidade máxima da procura.
    """
    def _expandir(self, problema, no):
        if no.profundidade < self.prof_max:
            yield from super()._expandir(problema, no)
    
    """
    Este método é também protegido e é responsável por memorizar o nó recebido 
    se este não corresponder a um ciclo.
    """
    def _memorizar(self, no):
        if not self._ciclo(no):
            super()._memorizar(no)
        
    """
    O método protegido ciclo irá verificar os antecessores do nó para ver se existe
    um nó com o mesmo estado do nó recebido.
    Para isso primeiramente é criada uma variável que vai armazenar o nó atual
    e é atribuida a essa variável o nó recebido, depois disso é feito um ciclo
    while que vai correr até ao nó em questão não ter mais antecessor. Dentro desse
    ciclo é atualizada a variável no_atual para o antecessor do nó recebido, caso 
    seja a primeira vez do ciclo, ou então para o antecessor do nó anteriormente 
    visto no ciclo. De seguida é feita uma verificação para ver se o estado do nó
    recebido como argumento do método é igual ao estado do nó em questão no ciclo
    while, se os estados forem iguais então é returnado True. Caso o ciclo while
    chegue ao fim e não tenha sido encontrado nenhum nó com o mesmo estado então 
    é retornado False. 
    """
    def _ciclo(self, no):
        # no_atual = no
        # while no_atual:
        #     no_atual = no_atual.antecessor
        #     if no.estado == no_atual.estado:
        #         return True
        # return False
        
        return no.estado in self.__estados_antecessores(no)
    
    """
    Este método usa um ciclo while para percorrer todos os nós antecessores
    do nó recebido, a cada iteração deste ciclo é usado o yield para fornecer
    à função que chamou este método o estado do nó em questão no ciclo while.
    De seguida é atualizada a variável no_ant para o seu nó antecessor.
    """
    def __estados_antecessores(self, no):
        no_ant = no.antecessor
        while no_ant:
            yield no_ant.estado
            no_ant = no_ant.antecessor