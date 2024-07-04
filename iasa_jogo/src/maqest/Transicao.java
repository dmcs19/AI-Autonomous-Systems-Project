package maqest;

/*
 * A classe Transição indica uma mudança de Estado e está associado a um
 * EV na classe Estado e é usada para que quando a Máquina de Estados
 * se encontra num determinado estado e ocorre um certo Evento
 * o Estado da Máquina de estados atualiza para o estadoSucessor
 * presente na Transição e a Personagem toma a Accao de definida
 * nesta mesma Transição.
 */
public class Transicao<EV, AC> {
    private Estado<EV, AC> estadoSucessor;
    private AC accao;

    /*
     * No construtor desta classe pretende-se definir o estado sucessor
     * e a accao a tomar para determinada Transição.
     */
    public Transicao(Estado<EV, AC> estadoSucessor, AC accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    /*
     * Este método retorna o Estado Sucessor para quando ocorrer
     * esta Transição.
     */
    public Estado<EV, AC> getEstadoSucessor() {
        return this.estadoSucessor;
    }

    /*
     * Este método retorna a Accao da Transição.
     */
    public AC getAccao() {
        return this.accao;
    }

}
