import os
import datetime

FICHEIRO_DADOS = "minhas_financas.txt"


def add_transacao():
    print("\n ADD TRANSACAO")
    while True:
        tipo = input("Recebimento ou Despesa? (r/d)> ").lower()
        if tipo in ["r", "d"]:
            break
        print("Insira apenas (Recebimento - r) ou (Despesa - d)")

    montante = input("Insira o montante: $ ")
    categoria = input("Insira a categoria: ")
    descricao = input("Insira a descricao: ")
    hoje = datetime.datetime.now().strftime("%Y-%m-%d")
    simbolo = "+" if tipo == "r" else "-"

    # Isto vai abrir o ficheiro no modo append - novos dados serao adicionados no final do ficheiro sem deletar nada
    with open(FICHEIRO_DADOS, "a") as ficheiro:
        ficheiro.write(f"{hoje}|{simbolo}{montante}|{categoria}|{descricao}\n")
    print("Transacao adicionada com sucesso")


def ver_transacoes():
    if not os.path.exists(FICHEIRO_DADOS):
        print("Nenhuma transacao existente")
        return
    print("\n TRANSACOES ")
    print("-" * 45)

    print("DATA          MONTANTE        CATEGORIA             DESCRICAO")
    print("-" * 45)

    with open(FICHEIRO_DADOS, "r") as ficheiro:
        for linha in ficheiro:
            partes = linha.strip().split("|")
            data = partes[0]
            montante = partes[1]
            categoria = partes[2]
            descricao = partes[3]
            print(
                f"{data}     {montante}          {categoria}                 {descricao}")


def ver_resumo():
    if not os.path.exists(FICHEIRO_DADOS):
        print("\nNenhuma Transacao encontrada")
        return

    total_recebimento = 0
    total_despesas = 0

    with open(FICHEIRO_DADOS, "r") as ficheiro:
        for linha in ficheiro:
            partes = linha.strip().split("|")
            montante = partes[1]

            if montante.startswith("+"):
                total_recebimento += float(montante[1:])
            else:
                total_despesas += float(montante[1:])
    saldo = total_recebimento - total_despesas

    print("\n SUMARIO FINANCEIRO")
    print(f"Total Recebimento: ${total_recebimento:.2f}")
    print(f"Total Despesas:    ${total_despesas:.2f}")
    print(f"Saldo:             ${saldo:.2f}")


def principal():
    while True:
        print("\n" + "=" * 30)
        print("REGISTRADOR DE FINANCAS")
        print("=" * 30)
        print("1. Add Transacao")
        print("2. Visualizar Transacoes")
        print("3. Sumario")
        print("4. Sair")

        escolha = input("\n Escolha (1-4)> ")
        if escolha == "1":
            add_transacao()
        elif escolha == "2":
            ver_transacoes()
        elif escolha == "3":
            ver_resumo()
        elif escolha == "4":
            print("Tchau")
            break
        else:
            print("Escolha invalida, por favor escolha opcoes (1-4)")


principal()
