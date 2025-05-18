import requests


def principal():
    print("\n Conversor simples de moedas")
    print(" Obtendo as taxas de câmbio...")

    try:
        resposta = requests.get("https://open.er-api.com/v6/latest/USD")
        taxas = resposta.json()["rates"]
        print("Taxas obtidas com sucesso!")
    except:
        print(" Erro: Não consegui me conectar a API de taxas de câmbio")
        return

    print("\n Populares: USD EUR GBP JPY CAD AUD CNY AOA")
    while True:
        print("\nInsira detalhes> ")
        moeda_origem = input("Código da moeda origem (ex: USD)> ").upper()
        if moeda_origem not in taxas:
            print(f"Código Inválido {moeda_origem}")
            continue
        moeda_destino = input("Código da moeda destino (ex: EUR)>").upper()
        if moeda_destino not in taxas:
            print(f"Código Inválido {moeda_destino}")
            continue

        try:
            montante = float(input(f"Montante em {moeda_origem}> "))
        except:
            print("Por favor insira um numero valido")
            continue
        montante_em_dolar = montante / taxas[moeda_origem]
        resultado = montante_em_dolar * taxas[moeda_destino]
        print(
            f"\n RESULTADO: {montante} {moeda_origem} = {resultado:.2f} {moeda_destino}")
        print(
            f"Taxa: 1 {moeda_origem} = {taxas[moeda_destino]/taxas[moeda_origem]:.2f} {moeda_destino}")
        if not input("\n Converter novamente? (Sim/Nao) > ").lower().startswith("s"):
            print("Tchau...")
            print("Escrito por: Filho do Almada")
            break


print
principal()
