package jogo;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;
import jogo.personagem.Personagem;

/*
 * A classe jogo é composta por um ambiente e uma personagem que por sua vez
 * é onde ocorrem todas as interações necessárias para que o jogo evolua.
 * As interações e os resultados das mesmas são mostradas ao utilizador 
 * em modo texto através da consola.
 * As ações da Personagem vão depender do Estado em que se encontram e do
 * Evento ocorrido no Ambiente onde se encontram. No caso do Ambiente
 * os seu Eventos vão ser determinados pelo utilizador através da consola.
 */
public class Jogo {
    private static Ambiente ambiente;
    private static Personagem personagem;

    /*
     * No método main é criado um novo ambiente e uma nova personagem, atribuindo à
     * mesma o ambiamente previamente criado. Após a criações destes dois objetos é
     * chamado o método executar.
     */
    public static void main(String[] args) {
        ambiente = new Ambiente();
        personagem = new Personagem(ambiente);
        executar();
    }

    /*
     * No método executar inicialmente é atribuido ao evento um Evento null que
     * servirá de comparação para verificar quando o jogo acaba.
     * É utilizado um cilco do while para quando o evento que ocorre no ambiente é
     * TERMINAR o programa saia do ciclo terminado assim o jogo.
     * Dentro deste ciclo é chamado o método executar() para a personagem e depois
     * disso é chamado o método evoluir() para o ambiente. Após estes dois métodos
     * terem sido executados a variável evento é atualizada, sendo depois utilizada
     * para verificar se o jogo terminou ou não.
     */
    private static void executar() {
        Evento evento;
        do {
            personagem.executar();

            ambiente.evoluir();
            evento = ambiente.getEvento();
        } while (evento != Evento.TERMINAR);
    }
}
