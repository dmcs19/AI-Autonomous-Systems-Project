from sae import Controlo
from sae import Simulador

class ControloTeste(Controlo):
    def processar(self, percepcao):
        print("processar")

controlo = ControloTeste()
Simulador(1, controlo).executar()