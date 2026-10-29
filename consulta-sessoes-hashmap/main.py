
import json

# Tabela Hash (HashMap)
sessoes = {}

# 1. Ler o arquivo e armazenar as sessões
with open("telephony_sessions.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        numero, dados = linha.strip().split(";", 1)

        sessao = json.loads(dados)

        # Adiciona na tabela Hash
        sessoes[numero] = sessao

print(f"Total de sessões carregadas: {len(sessoes)}")


# 2. Pesquisar sessões pelo número de celular
while True:
    print("\n Consulta de Sessoes")
    print("1 - Pesquisar celular")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = input("\nDigite o número do celular: ").strip()

        # Busca na tabela Hash
        sessao = sessoes.get(numero)

        if sessao is not None:
            print("\n Sessao Encontrada")
            print(f"Celular: {numero}")

            for campo, valor in sessao.items():
                print(f"{campo}: {valor}")
        else:
            print("\nCelular não encontrado!")

    elif opcao == "0":
        print("\nEncerrando programa...")
        break

    else:
        print("\nOpção inválida!")
