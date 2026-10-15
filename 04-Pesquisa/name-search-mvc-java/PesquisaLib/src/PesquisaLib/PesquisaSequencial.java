package PesquisaLib;

import java.util.List;

public class PesquisaSequencial {

    public static boolean existe(
            List<String> nomes, String nome) {

        String procurado = Normalizador.normalizar(nome);

        for (String atual : nomes) {
            if (Normalizador.normalizar(atual)
                    .equals(procurado)) {
                return true;
            }
        }

        return false;
    }
}