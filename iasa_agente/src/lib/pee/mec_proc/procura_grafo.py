from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
A classe ProcuraGrafo herda da classe MecanismoProcura e representa uma das várias
formas possíveis de realizar a procura de uma solução de um problema.
Neste caso a procura que se pretende realizar é a procura em grafos com ciclos,
este método de procura utiliza a procura de largura como sua base, por isso esta
classe será chamada pela classe ProcuraLargura. Este método corresponde em fazer 
uma procura em largura mas com a eliminação de nós correspondentes a estados repetidos,
para isto é necessário verificar se um novo nó sucessor corresponde a um estado que 
já foi anteriormente explorado, se isso acontecer, apenas o nó que corresponde ao
percurso com menor custo deve ser mantido, o outro nó correspondente ao mesmo estado,
mas num percurso com maior custo deve ser eliminado.
"""
class ProcuraGrafo(MecanismoProcura):
    """
    Este método é um método protegido e consiste na inicialização da memória através
    do método iniciar_memoria() do super e é depois inicializado um dicionário 
    protegido que servirá para guardar os nós já explorados.
    """
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {}
    
    """
    Este método servirá para memorizar um nó na fronteira. Primeiramente irá ser
    realizada uma verificação através do método manter, se o resultado retornado
    por esse método for false significa que o estado do nó em questão já foi 
    previamente explorado e com isso não deve ser adicionado à fronteira.
    No entanto caso o resultado retornado por esse método seja true significa que
    queremos inserir esse nó na fronteira para que este seja explorado posteriormente,
    para além disso é necessário adicionar o estado desse nó ao dicionário explorados
    para que este estado não volte a ser explorado.
    """
    def _memorizar(self, no):
        if self._manter(no):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)
            
    """
    Este método é um método protegido e irá retorar um booleano, ele retornará
    true se o estado do nó recebido não se encontrar no dicionário explorados,
    o que significa que o nó é para manter, caso contrário será retornado
    false.
    """
    def _manter(self, no):
        return no.estado not in self._explorados