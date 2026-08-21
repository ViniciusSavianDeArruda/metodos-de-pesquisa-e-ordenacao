package app;

import app.controller.ProcessoController;
import app.model.ProcessoService;
import app.view.ProcessoView;

public class Main {

    public static void main(String[] args) {

        ProcessoService service = new ProcessoService();
        ProcessoView view = new ProcessoView();

        ProcessoController controller =
                new ProcessoController(service, view);

        controller.iniciarSistema();
    }
}
