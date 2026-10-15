package PesquisaView.model;

import PesquisaLib.PesquisaSequencial;
import PesquisaLib.Trie;
import java.util.ArrayList;
import java.util.List;

public class NomesModel {

    private final List<String> nomes = new ArrayList<>();
    private final Trie trie = new Trie();

    public boolean cadastrarNome(String nome) {

        if (nome == null || nome.trim().isEmpty()) {
            return false;
        }

        nome = nome.trim().replaceAll("\\s+", " ");

        if (PesquisaSequencial.existe(nomes, nome)) {
            return false;
        }

        nomes.add(nome);
        trie.inserir(nome);

        return true;
    }

    public List<String> pesquisarNomes(String prefixo) {
        return trie.pesquisar(prefixo);
    }
}