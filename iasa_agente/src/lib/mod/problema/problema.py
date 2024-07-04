from abc import ABC, abstractmethod

"""
A classe Problema é uma classe abstrata e serve para representar qualquer tipo
de problema e é constituído por um estado inicial, operadores e por objetivos.
"""
class Problema(ABC):
    """
    No construtor desta classe são recebidos o estado inicial e os operadores
    deste problema e são guardados como atributos privados.
    """
    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores
    
    """
    propriedade que funciona como um getter e retorna o estado inicial deste problema de forma a que seja
    possível verificar este estado fora da classe mas que não seja possível 
    alterá-lo.
    """
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    """
    propriedade que funciona como um getter e retorna todos os operadores deste problema de forma a que
    seja possível obte-los fora desta classe, mas que não seja possível alterá-los.
    """
    @property
    def operadores(self):
        return self.__operadores

    @abstractmethod
    def objectivo(self, estado):
        """
        método abstrato que verifica se o objetivo de determinado problema foi
        atingido com sucesso ou não, retornando true ou false conforme o resultado.
        """
    