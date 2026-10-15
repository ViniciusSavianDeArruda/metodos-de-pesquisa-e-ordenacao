package PesquisaView.controller;

import PesquisaView.model.NomesModel;
import PesquisaView.view.NomesView;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;

public class NomesController {

    private NomesModel model;
    private NomesView view;

    public NomesController(NomesModel model, NomesView view) {
        this.model = model;
        this.view = view;

        view.adicionarAcaoCadastrar(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cadastrar();
            }
        });

        view.adicionarAcaoPesquisa(new DocumentListener() {
            @Override
            public void insertUpdate(DocumentEvent e) {
                pesquisar();
            }

            @Override
            public void removeUpdate(DocumentEvent e) {
                pesquisar();
            }

            @Override
            public void changedUpdate(DocumentEvent e) {
                pesquisar();
            }
        });

        pesquisar();
    }

    private void cadastrar() {
        String nome = view.getNomeDigitado();

        if (model.cadastrarNome(nome)) {
            view.mostrarMensagem("Nome cadastrado com sucesso!");
            view.limparNome();
        } else {
            view.mostrarMensagem("Nome inválido ou já cadastrado!");
        }

        pesquisar();
    }

    private void pesquisar() {
        String prefixo = view.getPrefixoDigitado();

        view.atualizarLista(model.pesquisarNomes(prefixo));
    }
}