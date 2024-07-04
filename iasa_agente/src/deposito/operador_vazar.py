from operador_tranferir import OperadorTransferir
from estado_volume import EstadoVolume

class OperadorVazar(OperadorTransferir):
    """
    O método aplicar é responsável por receber um estado e aplicar uma 
    transição e retornar depois o estado resultante dessa transição 
    aplicada ao estado recebido. Para isto é apenas feita uma verificação
    que é se ao alterarmos o valor do volume do estado recebido com o valor
    desta transição o seu volume se mantém acima de 0. Caso este valor
    seja menor que 0 é retornado uma nova instância de EstadoVolume iniciada
    com o volume a 0.
    """
    def aplicar(self, estado):
        novo_volume = estado.volume - self._volume
        if novo_volume < 0:
            novo_volume = 0
        return EstadoVolume(novo_volume)
    
    """
    Este método mostra na consola a informação do operador.
    """
    def __repr__(self):
        return "Vazar(%s)" % self._volume