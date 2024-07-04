package jogo.ambiente;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
 * A classe Ambiente neste caso em concreto representa um espaço selvagem
 * onde existem vários animais. Vai existir também uma personagem que
 * tenta tirar fotografias dos animais no entanto essa personagem vai
 * ter que reagir ao Eventos que ocorrem no Ambiente onde se encontra.
 * A escolha do próximo Evento a acontecer no Ambiente é responsabilidade
 * do utilizador, esta escolha é feita através da consola e teram que ser
 * utilzadas letras referentes aos Eventos para que estes sejam selecionados.
 */
public class Ambiente {
    private Evento evento;
    private Map<String, Evento> eventos;
    private Scanner sc = new Scanner(System.in);

    /*
     * No construtor do Ambiente é criado um HashMap com
     * as Strings que podem ser introduzidas pelo utilizador e
     * os Eventos correspondestes às mesmas.
     * É através deste HashMap que o método gerarEvento()
     * encontra o próximo Evento a ocorrer no Ambiente.
     */
    public Ambiente() {
        eventos = new HashMap<String, Evento>();

        eventos.put("s", Evento.SILENCIO);
        eventos.put("r", Evento.RUIDO);
        eventos.put("a", Evento.ANIMAL);
        eventos.put("f", Evento.FUGA);
        eventos.put("o", Evento.FOTOGRAFIA);
        eventos.put("t", Evento.TERMINAR);
    }

    /*
     * Este método retorna o evento do Ambiente.
     */
    public Evento getEvento() {
        return this.evento;
    }

    /*
     * Este método atualiza o Evento do Ambiente utilizando o método
     * gerarEvento() e de seguida mostra-o na consola através do
     * método mostrar().
     */
    public void evoluir() {
        evento = gerarEvento();
        mostrar();
    }

    /*
     * O método gerarEvento() é responsável por pedir ao utilizador
     * o próximo Evento a ocorrer no Ambiente. Para isto acontecer
     * o utilizador tem que na consola uma letra que tenha sido
     * atribuída a um Evento previamente e de seguida esse mesmo
     * Evento é retornado para que seja depois atualizado.
     */
    private Evento gerarEvento() {
        System.out.println("\nEvento? ");
        String comando = sc.next();
        return eventos.get(comando);
    }

    /*
     * Este método mostra na consola o evento que está a
     * ocorrer no Ambiente.
     */
    private void mostrar() {
        System.out.println("Evento: " + this.evento);
    }
}
