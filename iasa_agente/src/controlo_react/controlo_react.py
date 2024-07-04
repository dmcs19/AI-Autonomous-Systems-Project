from sae import Controlo

"""
A classe ControloReact tem herança da classe Controlo fornecida pelo docente.
Esta classe tem um argumento do tipo Comportamento, podendo este ser do tipo
simples ou composto.
"""
class ControloReact(Controlo):
    """
    O construtor desta classe recebe um Comportamento e armazena-o como
    um atributo.
    """
    def __init__(self, comportamento):
        self.comportamento = comportamento

    """
    O método processar() recebe uma Percepcao e é responsável por obter a accao
    a realizar, para isso o método chama o método activar() do seu atributo
    comportamento e passa-lhe a percepcao recebida para depois retornar a accao 
    retornada por esse mesmo método.
    """
    def processar(self, percepcao):
        return self.comportamento.activar(percepcao)