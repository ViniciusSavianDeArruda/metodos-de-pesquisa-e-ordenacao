package PesquisaLib;

import java.util.ArrayList;
import java.util.List;

public class Trie {

    private static class No {
        char letra;
        List<No> filhos = new ArrayList<>();
        List<String> nomes = new ArrayList<>();

        No(char letra) {
            this.letra = letra;
        }
    }

    private No raiz = new No(' ');

    public void inserir(String nome) {
        String texto = Normalizador.normalizar(nome);
        No atual = raiz;

        atual.nomes.add(nome);

        for (char letra : texto.toCharArray()) {

            No proximo = buscarFilho(atual, letra);

            if (proximo == null) {
                proximo = new No(letra);
                atual.filhos.add(proximo);
            }

            atual = proximo;
            atual.nomes.add(nome);
        }
    }

    public List<String> pesquisar(String prefixo) {
        String texto = Normalizador.normalizar(prefixo);
        No atual = raiz;

        for (char letra : texto.toCharArray()) {

            atual = buscarFilho(atual, letra);

            if (atual == null) {
                return new ArrayList<>();
            }
        }

        return new ArrayList<>(atual.nomes);
    }

    private No buscarFilho(No atual, char letra) {

        for (No filho : atual.filhos) {
            if (filho.letra == letra) {
                return filho;
            }
        }

        return null;
    }
}