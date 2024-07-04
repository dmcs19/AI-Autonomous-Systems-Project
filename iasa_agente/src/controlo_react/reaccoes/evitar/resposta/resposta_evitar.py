from random import choice
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae import Direccao

"""
A classe RespostaEvitar representa a resposta a diferentes estímulos, 
esta classe  herda da classe RespostaMover que por sua vez herda da
classe Resposta, isto significa que a classe tem um atributo do tipo
Accao que será depois retornada no método activar e que servirá para
saber que accao deverá ser tomada perante o estímulo recebido.
"""
class RespostaEvitar(RespostaMover):
    """
    O construtor desta classe recebe a direção inicial e chama o super
    construtor da classe Resposta e fornece essa direcao recebida, caso
    não seja passada nenhuma direção a direcao enviada para o super
    construtor é Direccao.ESTE por defeito.
    Para além disto é criada e armazenada uma lista privada que contém 
    todas as direções possíveis sendo estas NORTE, SUL, ESTE e OESTE.
    """
    def __init__(self, dir_inicial=Direccao.ESTE):
        super().__init__(dir_inicial)
        self.__direccoes = [Direccao.NORTE, Direccao.SUL, Direccao.ESTE, Direccao.OESTE]
        
    """
    O método activar é responsável por receber e percepao e a intensidade 
    e com isto decidir que ação tomar.
    Para fazer com que isso aconteça é necessário verificar vários fatores.
    Primeiramente é verificado se existe contacto com o obstáculo através
    da do método contacto_obst() da classe percepcao que quando passada a
    direccao da accao é retornado um booleano que revela se existe contacto
    com o obstáculo ou não. Se este contacto existir inicialmente é chamado 
    o método privado alterar_direccao() que quando passada uma percepcao
    retorna uma direccao livre a tomar, a negação deste valor é depois atribuído à 
    variavel contacto_obst.
    De seguida é verificado se esse método retornou uma direccao livre ou não.
    Caso a direcao tenha sido alterada para uma direccao livre ou não exista 
    contacto com o obstáculo é chamado através do super o método activar() da 
    classe Resposta e passada a percepcao e a intensidade.
    """
    def activar(self, percepcao, intensidade):
        contacto_obst = percepcao.contacto_obst(self._accao.direccao)
        
        if contacto_obst:
            contacto_obst = not self.__alterar_direccao(percepcao)
                
        if not contacto_obst: 
            return super().activar(percepcao, intensidade)
    
    """
    Este método apenas é chamado se existir contacto com o obstáculo e tem
    como objetivo alterar a direccao da accao da resposta.
    Para isso é chamado o método privado direccao_livre() que retorna uma
    direccao livre. Se esse método retornar uma direccao entramos no if
    e a direccao da accao é atualizada sendo depois retornada ao método 
    que chamou este método.
    """
    def __alterar_direccao(self, percepcao):
        direccao_livre = self.__direccao_livre(percepcao)
        if direccao_livre:
            self._accao.direccao = direccao_livre
            return self._accao.direccao
            
    """
    O método privado direccao_livre() é resposável por verificar se existem 
    direccoes livres e retornar uma dessar direccoes aleatóriamente, para isso
    o método recebe a percepcao de modo a verificar se a direccao esta livre ou
    não.
    Para isto é criada uma lista composta por qualquer elemento do atributo 
    privado direccoes que não se encontre em contacto com o obstáculo.
    Depois desta seleção de direccoes livres é verificada se a lista criada 
    não está vazia, se não estiver vazia é usado o método choice() na lista
    direccoes_livres para que seja selecionada uma direccao dessa lista 
    aleatóriamente sendo depois retornada.
    """
    def __direccao_livre(self, percepcao):
        direccoes_livres = [direccao for direccao in self.__direccoes if not percepcao.contacto_obst(direccao)]
        if direccoes_livres :
            return choice(direccoes_livres)