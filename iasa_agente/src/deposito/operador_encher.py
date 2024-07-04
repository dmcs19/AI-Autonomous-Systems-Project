from operador_tranferir import OperadorTransferir
from estado_volume import EstadoVolume

class OperadorEncher(OperadorTransferir):
    """
    O método aplicar retorna uma nova instância da classe
    EstadoVolume sendo esta inicializada com o novo volume.
    """
    def aplicar(self, estado):
        novo_volume = estado.volume + self._volume
        return EstadoVolume(novo_volume)
    
    """
    Este método mostra na consola a informação do operador.
    """
    def __repr__(self):
        return "Encher(%s)" % self._volume