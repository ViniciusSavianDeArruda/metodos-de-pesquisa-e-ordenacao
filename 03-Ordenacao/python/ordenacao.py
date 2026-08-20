import random
import time


class Ordenacao:

    @staticmethod
    def bolha(lista):
        comparacoes = 0
        trocas = 0
        troca = True

        while troca:
            troca = False

            for i in range(len(lista) - 1):
                comparacoes += 1

                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]

                    trocas += 1
                    troca = True

        print("--- Bolha ---")
        print("Comparações:", comparacoes)
        print("Trocas:", trocas)


    @staticmethod
    def selecao(lista):
        comparacoes = 0
        trocas = 0

        for i in range(len(lista) - 1):

            menor = i

            for j in range(i + 1, len(lista)):
                comparacoes += 1

                if lista[j] < lista[menor]:
                    menor = j

            if i != menor:
                lista[i], lista[menor] = lista[menor], lista[i]
                trocas += 1

        print("--- Seleção ---")
        print("Comparações:", comparacoes)
        print("Trocas:", trocas)


    @staticmethod
    def insercao(lista):
        comparacoes = 0
        trocas = 0

        for i in range(1, len(lista)):

            valor = lista[i]
            j = i - 1

            while j >= 0:

                comparacoes += 1

                if valor < lista[j]:
                    lista[j + 1] = lista[j]
                    trocas += 1
                    j -= 1
                else:
                    break

            lista[j + 1] = valor
            trocas += 1

        print("--- Inserção ---")
        print("Comparações:", comparacoes)
        print("Trocas:", trocas)


class Util:

    @staticmethod
    def popular_lista(lista, quantidade):

        for i in range(quantidade):
            lista.append(random.randrange(100000))


    @staticmethod
    def exibir_lista(lista):

        for item in lista:
            print(item)


    @staticmethod
    def exibir_tempo(tempo, nome):

        print("Tempo:", nome, "-", tempo * 1000, "ms")


def main():

    quantidade = int(
        input("Quantos números deseja trabalhar? ")
    )

    # Cria a lista original
    lista = []

    Util.popular_lista(lista, quantidade)

    # Cria uma cópia para cada algoritmo
    lista_bolha = lista.copy()
    lista_selecao = lista.copy()
    lista_insercao = lista.copy()
    lista_sort = lista.copy()


    # SORT NATIVO
    inicio = time.perf_counter()

    lista_sort.sort()

    fim = time.perf_counter()

    print("--- Sort nativo ---")
    Util.exibir_tempo(
        fim - inicio,
        "Ordenação"
    )

    print()


    # BOLHA
    inicio = time.perf_counter()

    Ordenacao.bolha(lista_bolha)

    fim = time.perf_counter()

    Util.exibir_tempo(
        fim - inicio,
        "Ordenação"
    )

    print()


    # SELEÇÃO
    inicio = time.perf_counter()

    Ordenacao.selecao(lista_selecao)

    fim = time.perf_counter()

    Util.exibir_tempo(
        fim - inicio,"Ordenação")

    print()


    # INSERÇÃO
    inicio = time.perf_counter()

    Ordenacao.insercao(lista_insercao)

    fim = time.perf_counter()

    Util.exibir_tempo(
        fim - inicio,"Ordenação")

main()
