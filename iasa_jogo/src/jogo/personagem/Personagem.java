package jogo.personagem;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;

/*
 * Esta classe representa uma personagem virtual que toma decisóes baseadas
 * na situação em que se encontra. Esta interação é realizada com o ambiente 
 * em que a personagem se encontra, sendo este previamente atribuído à personagem.
 * A classe Personagem tem também um atributo do tipo Controlo, este é
 * usado para que conforme a perceção da personagem e após o seu processamento
 * seja dada uma ação para a personagem realizar.
 * Quando o jogo se inicia a personagem fica numa situação de
 * procura de animais. Quando detecta algum ruído aproxima-se e
 * fica em inspecção da zona, procurando a fonte do ruído.
 * Quando volta a haver silêncio a personagem volta a uma
 * situação de procura de animais. Quando detecta um animal a
 * personagem aproxima-se e fica em observação. Caso o animal
 * continue presente, a personagem observa o animal e fica
 * preparada para o registo, se ocorrer a fuga do animal a
 * personagem fica em inspecção da zona, à procura de uma fonte
 * de ruído. Na situação de registo, se o animal continuar presente
 * fotografa-o, caso ocorra a fuga do animal ou a personagem
 * tenha conseguido uma fotografia do animal, a personagem fica
 * novamente numa situação de procura.
 */
public class Personagem {
    private Ambiente ambiente;
    private Controlo controlo;

    /*
     * No construtos da Personagem é recebido o Ambiente em que esta se
     * encontra sendo depois guardado no atributo ambiente.
     * Depois disto é criado um novo Controlo que é onde ocorrerá o
     * processamento da Personagem.
     */
    public Personagem(Ambiente ambiente) {
        this.ambiente = ambiente;
        controlo = new Controlo();
    }

    /*
     * O método executar tem como objetivo chamar o método percecionar
     * da Personagem e enviar a percepcao obtida para o Controlo
     * para que este a processe retornando assim a Accao que a 
     * Personagem deve fazer, mostrando-a depois na consola
     * através do método actuar().
     */
    public void executar() {
        Percepcao percepcao = percecionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
    }

    /*
     * O método percecionar consistem em retornar a percepção da 
     * Personagem sobre o Ambiente.
     * Para isto o método obtém o Evento que está a ocorrer no 
     * Ambiente no qual a Personagem se encontra e de seguida
     * cria uma nova Percepcao relativamente ao Evento ocorrido.
     */
    public Percepcao percecionar() {
        Evento evento = ambiente.getEvento();
        return new Percepcao(evento);
    }

    /*
     * O método actuar mostra na consola a accao que a Personagem deve fazer
     */
    public void actuar(Accao accao) {
        System.out.println("Accao: " + accao);
    }

}
