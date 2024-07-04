"""
A classe Solucao representa um percurso correspondente a uma solução de um
problema. Com esta classe será possível ter acesso indexado e iteração sobre
o percurso e também remover o primeiro nó do percurso.
"""
class Solucao:
    """
    O construtor desta classe apenas recebe o nó final da solução.
    Primeiramente é criado um atributo privado percurso como uma lista vazia
    que servirá para armazenar o caminho de nós desde o nó raiz até ao objetivo.
    De seguida é feito um ciclo while que ocorrer até que o nó em questão não
    tenho nenhum nó antecessor o que significa que chegamos ao nó raiz.
    Enquanto isto não acontece o nó em questão é adicionado ao inicio do percurso
    para que no final o percurso esteja ordenado da forma que nós queremos, sendo
    esta com o nó raiz no primeiro índice e seguindo depois o percurso de forma
    ordenada até chegarmos ao nó objetivo que ocupará o último lugar da lista.
    Após esta adição à lista a variável nó é atualizada para o seu antesucessor,
    desta forma o ciclo seguirá até o nó raiz ser atingido.
    """
    def __init__(self, no_final):
        self.__percurso = []
        no = no_final
        while no:
            self.__percurso.insert(0, no)
            no = no.antecessor
            
    """
    propriedade que funciona como um getter e retorna a dimensão da solução
    através do método len() fornecendo-lhe o percurso que retorna o seu 
    comprimento.
    """
    @property
    def dimensao(self):
        return len(self.__percurso)
    
    """
    Este método faz uma verificação para ver se o percurso existe e não está 
    vazio, se esta condição se realizar é retornado e removido o primeiro
    nó do percurso através do método pop().
    """
    def remover(self):
        if self.__percurso:
            return self.__percurso.pop(0)
    
    """
    este método retorna um iterador de nós da solução, este servirá para suportar
    instruções do tipo for-each.
    """
    def __iter__(self):
        return iter(self.__percurso)
    
    """
    este método retorna um nó da solução obtido através do índice recebido 
    nesta função.
    """
    def __getitem__(self, index):
        return self.__percurso[index]