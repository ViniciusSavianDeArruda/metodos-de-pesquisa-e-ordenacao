package PesquisaView;

import PesquisaView.model.NomesModel;
import PesquisaView.view.NomesView;
import PesquisaView.controller.NomesController;

public class Main {

    public static void main(String[] args) {

        NomesModel model = new NomesModel();
        NomesView view = new NomesView();

        NomesController controller = new NomesController(model, view);

        view.setLocationRelativeTo(null);
        view.setVisible(true);
    }
}