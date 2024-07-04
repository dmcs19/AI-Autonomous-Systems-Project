package jogo.personagem;

import jogo.ambiente.Evento;
import maqest.Estado;
import maqest.MaquinaEstados;

/*
 * A classe Controlo é a classe responsável pelas ações que a
 * Personagem toma, é aqui que com acesso a uma Máquina de Estados
 * criada no construtor são tomadas as decisões.
 * Estas decisões são tomadas pelo método processar() e dependem
 * do atual estado da Máquina de Estados e do Evento ocorrido no
 * Ambiente.
 */
public class Controlo {
    private MaquinaEstados<Evento, Accao> maqEst;

    /*
     * No construtor do da classe Controlo é onde é criada a Máquina
     * de estados usada para processar os eventos ocorridos.
     * Antes de criarmos esta Máquina de estados temos de definir todos
     * os Estados possíveis para a Personagem e de seguida temos que
     * definir todas as transições possíveis e associá-las a cada um dos 
     * estados, fornecendo o Evento, o estado seguinte e a Accao a tomar
     * pela Personagem.
     * Após realizar estes procedimentos vamos então criar uma nova
     * Máquina de estados e fornecer-lhe o estado inicial.
     */
    public Controlo() {
        // Definir estados
        Estado<Evento, Accao> procura = new Estado<>("Procura");
        Estado<Evento, Accao> inspeccao = new Estado<>("Inspecção");
        Estado<Evento, Accao> observacao = new Estado<>("Observação");
        Estado<Evento, Accao> registo = new Estado<>("Registo");

        // Definir transições
        procura
                .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
                .transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR)
                .transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

        inspeccao
                .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
                .transicao(Evento.RUIDO, inspeccao, Accao.PROCURAR)
                .transicao(Evento.SILENCIO, procura);

        observacao
                .transicao(Evento.ANIMAL, registo, Accao.OBSERVAR)
                .transicao(Evento.FUGA, inspeccao);

        registo
                .transicao(Evento.FUGA, procura)
                .transicao(Evento.FOTOGRAFIA, procura)
                .transicao(Evento.ANIMAL, registo, Accao.FOTOGRAFAR);

        maqEst = new MaquinaEstados<Evento, Accao>(procura);
    }

    /*
     * Este método retorna o estado atual da Maquina de Estados
     */
    public Estado<Evento, Accao> getEstado() {
        return maqEst.getEstado();
    }

    /*
     * Este método é o responsável por realizar o processamento
     * da parte da Personagem. Este processamento baseia-se na
     * receção das percepcões da personagem e através dessas percepções
     * devolver à Personagem a ação que deve tomar.
     * Numa fase inicial do método extrai o Evento através da percepção
     * recebida da Personagem, após essa extração é chamado o método
     * processar() mas desta vez relativamente à Máquina de Estados
     * associada a esta classe, este método irá retornar a ação que
     * a Personagem deve tomar. Depois desta decisão é chamado o método
     * mostrar() para informar o utilizador e é retornada a Accao a tomar
     * para a instacia da classe Personagem que chamou este método.
     */
    public Accao processar(Percepcao percepcao) {
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();
        return accao;
    }

    /*
     * O método mostrar escreve na consola o estado em que se encontra
     * a Maquina de Estados.
     */
    private void mostrar() {
        System.out.println("Estado: " + maqEst.getEstado().getNome());
    }

}
