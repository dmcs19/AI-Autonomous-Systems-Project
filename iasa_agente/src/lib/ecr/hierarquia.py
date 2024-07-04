from .comport_comp import ComportComp

"""
A classe Hierarquia tem herança da classe ComportComp.
Esta classe é composta por um conjunto de comportamentos que
estão organizados numa hierarquia fixa de supressão.
Esta classe não contém construtor pois quando é criada uma
nova instância é chamado o construtor do seu parente o 
ComportComp.
"""
class Hierarquia(ComportComp):
    """
    Este método é responsável por receber todas as accoes a
    realizar e selecionar e devolver a accao que se encontra
    no nível mais alto da hierarquia.
    """
    def seleccionar_accao(self, accoes):
        return accoes[0]