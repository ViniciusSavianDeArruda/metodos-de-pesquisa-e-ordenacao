from model.tabela_hash import TabelaHash


class Encurtador:

    @staticmethod
    def encurtar(link_original, tabela):

        DOMINIO = "localhost"

        hash_gerado = str(abs(hash(link_original)))

        tabela.links[hash_gerado] = link_original

        return "https://" + DOMINIO + "/" + hash_gerado

    @staticmethod
    def buscar_link_encurtado(link_encurtado, tabela):

        dados_link = link_encurtado.split("/")

        hash_obtido = dados_link[-1]

        resposta = tabela.links.get(hash_obtido)

        if resposta is None:
            resposta = "Link encurtado não encontrado!"

        return resposta