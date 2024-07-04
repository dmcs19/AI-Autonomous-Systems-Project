package jogo.personagem;

import jogo.ambiente.Evento;

/*
 * A classe Percepcao representa a percepcao que a Personagem
 * tem sobre o Ambiente que o rodeia. Sendo esta classe 
 * inicializada com o Evento que ocorre no Ambiente onde a
 * Personagem se encontra.
 */
public class Percepcao {
    private Evento evento;

    /*
     * O construtor da classe Percepcao recebe um Evento
     * e guarda esse valor.
     */
    public Percepcao(Evento evento) {
        this.evento = evento;
    }

    /*
     * O método getEvento() retorna o evento atribuído
     * à classe Percepcao.
     */
    public Evento getEvento() {
        return this.evento;
    }
}
