from controller.encurtador import Encurtador
from model.tabela_hash import TabelaHash
from utilidades.validador_url import ValidadorUrl


class Menu:

    def __init__(self):

        self.meus_links = TabelaHash()

    def executar(self):

        while True:

            print("\n Encurtador de Links")
            print("1 - Gerar link encurtado")
            print("2 - Testar local")
            print("3 - Limpar")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.gerar_link()

            elif opcao == "2":
                self.testar_local()

            elif opcao == "3":
                print("Operação finalizada. Você pode continuar.")

            elif opcao == "0":
                print("Encerrando programa...")
                break

            else:
                print("Opção inválida!")

    def gerar_link(self):

        url = input("\nInforme o link original: ")

        if not ValidadorUrl.is_link_valido(url):
            print("Verifique o link informado!")
            return

        link_encurtado = Encurtador.encurtar(
            url,
            self.meus_links
        )

        print("\nLink encurtado:")
        print(link_encurtado)

    def testar_local(self):

        url = input("\nInforme o link encurtado: ")

        if url.strip() == "":
            print("Informe um link!")
            return

        url_original = Encurtador.buscar_link_encurtado(
            url,
            self.meus_links
        )

        print("\nResultado:")
        print(url_original)