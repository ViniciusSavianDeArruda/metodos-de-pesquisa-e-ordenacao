package PesquisaLib;

import java.text.Normalizer;
import java.util.Locale;

public class Normalizador {

    public static String normalizar(String texto) {
        if (texto == null) {
            return "";
        }

        String resultado = texto.trim()
                .replaceAll("\\s+", " ")
                .toLowerCase(Locale.ROOT);

        resultado = Normalizer.normalize(
                resultado, Normalizer.Form.NFD);

        return resultado.replaceAll("\\p{M}+", "");
    }
}