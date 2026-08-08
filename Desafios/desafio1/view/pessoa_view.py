class PessoaView:

    def mostrar_menu(self):

        print("\nMENU ")
        print("1. Carregar arquivo")
        print("2. Mostrar dados carregados")
        print("3. Fim")

        return input("Escolha uma opção: ")

    def mostrar_pessoas(self, pessoas):

        print("\nDADOS CARREGADOS")

        if not pessoas:
            print("Nenhum dado carregado.")
            return

        for pessoa in pessoas:
            print(pessoa)

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
