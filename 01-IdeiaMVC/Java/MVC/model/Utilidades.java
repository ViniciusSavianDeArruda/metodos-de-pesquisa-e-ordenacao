package MVC.model;

import java.util.List;
import java.util.Random;

public class Utilidades {

    /**
     * Método de classe que popula lista com números aleatórios
     * ou de forma sequencial dentro de uma faixa.
     */
    public static void popularLista(
            List<Integer> lista,
            long quantidadeNumeros,
            int inicio,
            int fim,
            boolean aleatorio) {

        Random gerador = new Random();

        if (aleatorio) {

            for (long i = 0; i < quantidadeNumeros; i++) {
                lista.add(gerador.nextInt(inicio, fim));
            }

        } else {

            for (long i = 0; i < quantidadeNumeros; i++) {
                lista.add((int) (inicio + i));
            }
        }
    }
}
