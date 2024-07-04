from ..mod_prob.problema_plan_traj import ProblemaPlanTraj

"""
Esta classe servirá para planear um trajeto, gerando uma solução, com base
nos argumentos recebidos no método planear. Permitindo assim mostrar o 
trajeto correspondente a uma solução.
"""
class PlaneadorTrajecto:
    """
    Este método cria uma instância problema da classe ProblemaPlanTraj, de seguida
    é instânciado um mecanismo de procura e depois chamamos o método procurar() 
    do mecanismo de procura utilizado, obtendo assim a respetiva solução sendo
    depois retornada.
    Após termos chegado à solução é então mostrado na consola o nome do mecanismo
    de procura usado na procura pela solução e os recursos usados pelo mecanismo.
    """
    def planear(self, ligacoes, loc_inicial, loc_final, mec_proc):
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        solucao = mec_proc.procurar(problema)
        print('\n')
        print(mec_proc.__class__.__name__)
        print(mec_proc.complexidade_temporal())
        print(mec_proc.complexidade_espacial())
        return solucao