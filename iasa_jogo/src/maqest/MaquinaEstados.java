package maqest;

/*
 * A classe MaquinaEstados serve para representar circuitos lógicos.
 * Esta classe armazena o Estado de um objeto num determinado momento,
 * podendo este Estado ser alterado através de Transições.
 */
public class MaquinaEstados<EV, AC> {
    private Estado<EV, AC> estado;

    /*
     * No consturtor da classe é recebido e atribuído o primeiro estado
     * desta Máquina de estados.
     */
    public MaquinaEstados(Estado<EV, AC> estado) {
        this.estado = estado;
    }

    /*
     * Este método retorna o estado atual da Máquina de estados.
     */
    public Estado<EV, AC> getEstado() {
        return this.estado;
    }

    /*
     * O método processar() é responsável pelo processamento de um
     * Evento gerando uma ação.
     * Para isto o método obtém a transição a fazer através do EV
     * recebido e se essa Transição não for null o estado da máquina de
     * estados é atualizado e é retornada a AC a tomar.
     */
    public AC processar(EV evento) {
        Transicao<EV, AC> transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        }
        return null;
    }
}
