from controller.pessoa_controller import PessoaController
from view.pessoa_view import PessoaView


def main():

    controller = PessoaController()
    view = PessoaView()

    while True:

        opcao = view.mostrar_menu()

        if opcao == "1":

            if controller.carregar_arquivo():
                view.mostrar_mensagem("Arquivo carregado com sucesso!")
            else:
                view.mostrar_mensagem("Erro ao carregar o arquivo.")

        elif opcao == "2":

            pessoas = controller.obter_pessoas()
            view.mostrar_pessoas(pessoas)

        elif opcao == "3":

            view.mostrar_mensagem("Programa encerrado.")
            break

        else:

            view.mostrar_mensagem("Opção inválida.")


if __name__ == "__main__":
    main()
