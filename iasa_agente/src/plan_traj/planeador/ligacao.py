from dataclasses import dataclass

"""
Este código representa uma dataclasse com 3 atributos, origem, destino e custo.
"""
@dataclass
class Ligacao:
    origem: str
    destino: str
    custo: int