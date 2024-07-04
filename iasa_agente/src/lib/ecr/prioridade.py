from .comport_comp import ComportComp

"""
A classe Prioridade tem herança da classe ComportComp e é composta
por um conjunto de comportamentos com diferentes prioridades.
Nesta classe as respostas são selecionadas de acordo com uma prioridade
associada que varia ao longo da execução.
Tal como na classe Hierarquia esta também não tem um construtor, pelo que
quando é criada uma nova instância é chamado o construtor do seu parente
o ComportComp.
"""
class Prioridade(ComportComp):
    """
    Este método é responsável por receber todas as accoes a realizar
    e selecionar e devolver a accao que contém a maior prioridade associada.
    Esta seleção é conseguida através do método max() que fornecendo
    os argumentos adequados para esta situação nos devolve a accao com maior
    prioridade da lista de accoes fornecida.
    """
    def seleccionar_accao(self, accoes):
        return max(accoes, key=lambda accao: accao.prioridade)
        