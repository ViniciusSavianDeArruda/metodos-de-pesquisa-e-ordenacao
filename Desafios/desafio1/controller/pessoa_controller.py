from model.pessoa import Pessoa


class PessoaController:

    def __init__(self):
        self.pessoas = []

    def carregar_arquivo(self):
        self.pessoas.clear()

        try:
            with open("data/dados.txt", "r", encoding="utf-8") as arquivo:

                for linha in arquivo:
                    nome = linha.strip()

                    if nome:
                        pessoa = Pessoa(nome)
                        self.pessoas.append(pessoa)

            return True

        except FileNotFoundError:
            return False

    def obter_pessoas(self):
        return self.pessoas
