from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher
from ecr.hierarquia import Hierarquia
from ecr.prioridade import Prioridade
from sae import Simulador

"""
É criada uma variável comportamento que vai corresponder a uma Hierarquia
onde é passada uma lista de comportamentos, neste caso a lista é composta
apenas por um Comportamento, sendo este Explorar.
Depois disso é criada uma variável controlo que é inicializada com uma
nova instância da classe ControloReact onde lhe é passado o comportamento
composto (Hierarquia) previamente criado.
"""
#comportamento = Hierarquia([Explorar()])
comportamento = Recolher()
controlo = ControloReact(comportamento)


Simulador(1, controlo).executar()

