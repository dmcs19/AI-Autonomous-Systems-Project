package maqest;

import java.util.HashMap;
import java.util.Map;

/*
 * A classe Estado representa um estado possível para a Máquina
 * de estados, este Estados tem dois atributos, sendo estes um nome
 * e um mapa de transições que vai ser preenchido por todas as
 * Transições disponíveis para este mesmo Estado.
 */
public class Estado<EV, AC> {
    private String nome;
    private Map<EV, Transicao<EV, AC>> transicoes;

    /*
     * O construtor recebe uma String que contém o nome do Estado,
     * guarda esse nome e cria um novo HashMap que vai conter
     * todas as Transições possíveis para o Estado a ser criado.
     */
    public Estado(String nome) {
        this.nome = nome;
        transicoes = new HashMap<EV, Transicao<EV, AC>>();
    }

    /*
     * O método retorna o nome do estado.
     */
    public String getNome() {
        return this.nome;
    }

    /*
     * Este método retorna a Transição associada ao EV recebido.
     */
    public Transicao<EV, AC> processar(EV evento) {
        return transicoes.get(evento);
    }

    /*
     * Este método chama o método seguinte pois o seu objetivo é o mesmo
     * porém este método é usado quando não é fornecido uma AC, por isso
     * este método chama o método em baixo e passa a AC como null.
     */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /*
     * Este método é responsável por adicionar ao mapa transições uma nova
     * Transição relacionada a um EV, o Estado seguinte e a AC a tomar
     * são recebidas pelo método e com estes valores é criada a Transição 
     * que de seguida é adicionada ao mapa.  
     */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor, AC accao) {
        transicoes.put(evento, new Transicao<EV, AC>(estadoSucessor, accao));
        return this;
    }
}
