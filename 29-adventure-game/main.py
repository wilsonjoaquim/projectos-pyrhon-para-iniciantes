import time
import random

jogador = {
    "nome": "",
    "vida": 100,
    "ouro": 50,
    "items": []
}

# localizacao do jogo
localizacoes = {
    "cidade": {
        "descricao": "Uma cidade maravilhosa com shoppings e pessoas amigaveis.",
        "opcoes": ["shop", "floresta", "repouso"]
    },
    "floresta": {
        "descricao": "Uma floresta escura com son estranhos",
        "opcoes": ["explorar", "voltar para a cidade", "campo"]
    },
    "shop": {
        "descricao": "Uma loja pequena com varios itens a venda",
        "opcoes": ["comprar vida porcao (20 ouros)", "comprar palavra de socorro(50 ouros)", "voltar a cidade"]
    },
}

# itens com efeitos
itens = {
    "porcao vida": {"vida": 30, "preco": 20},
    "socorro palavra": {"perigo": 10, "preco": 50}
}
# inimigos que podem ser encontrados
inimigos = [
    {"name": "Goblin", "vida": 30, "perigo": 5, "ouro": 15},
    {"name": "Wolf", "vida": 20, "perigo": 7, "ouro": 10},
    {"name": "Bandit", "vida": 40, "perigo": 8, "ouro": 25}
]


def escrever_lento(texto):
    for c in texto:
        print(c, end="", flush=True)
        time.sleep(0.02)


def mostrar_estados():
    print("\n" + "="*40)
    print(
        f"Nome: {jogador['nome']} | Vida: {jogador['vida']} | Ouro: {jogador['ouro']}")

    if jogador["items"]:
        print(f" Itens: {", ".join(jogador["items"])}")
        print("\n" + "="*40)


def cidade():
    escrever_lento("\n Voce esta na cidade.")
    escrever_lento(localizacoes["cidade"]["descricao"])

    while True:
        mostrar_estados()
        print("\nOque gostaria de fazer?")
        print("1. Ir ao Shopping")
        print("2. Entrar na floresta")
        print("3. Repousar dentro (restaura vida por 10 ouros)")
        print("4. Terminar o jogo")

        escolha = input("> ").lower()
        if escolha == "1" or "shop" in escolha:
            shop()
        elif escolha == "2" or "floresta" in escolha:
            floresta()
        elif escolha == "3" or "repouso" in escolha:
            repouso()
        elif escolha == "4" or "sair" in escolha:
            escrever_lento("\nObrigado por jogar, tchau..")
            exit()
        else:
            print("\n Eu nao entendo esta opcao. Por favor tentar novamente")


def shop():
    escrever_lento("\Voce esta no shop.")
    escrever_lento(localizacoes["shop"]["descricao"])

    while True:
        mostrar_estados()
        print("\n O que gostaria de fazer?")
        print("1. Comprar pocao de vida (20 ouros)")
        print("2. Comprar swords (50 ouros)")
        print("3. Retornar a cidade")
        escolha = input("> ").lower()

        if escolha == "1" or "vida" in escolha:
            comprar_item("porcao vida")
        elif escolha == "2" or "socorro palavra" in escolha:
            comprar_item("socorro palavra")
        elif escolha == "3" or "retornar" or "cidade" in escolha:
            escrever_lento("Voce deixa o shop e retorna a cidade")
            return
        else:
            print("\n Eu nao entendo esta opcao. Por favor tentar novamente")


def comprar_item(nome_item):
    item = itens[nome_item]
    if nome_item in jogador["items"] and nome_item != "porcao vida":
        escrever_lento(f"\n Tu ja tem um {nome_item}")
        return

    if jogador["ouro"] >= item["preco"]:
        jogador["ouro" -= item["preco"]]

        if nome_item not in jogador["items"]:
            jogador["items"].append(nome_item)

        if "vida" in item:
            escrever_lento(
                f"\n Voce comprou uma pocao de vida! pode usar para restaurar {itens['porcao vida']} Vida!")
        elif "perigo" in item:
            escrever_lento(
                f"\n Voce comprou um {nome_item}!Isto vai te defender dos inimigos rapidos")
        else:
            print("\nVoce nao tem ouro suficiente para comprar este item")


def floresta():
    escrever_lento("\n Voce entrou na floresta escura...")
    escrever_lento(localizacoes['floresta']["descricao"])

    while True:
        mostrar_estados()
        print("\n O que gostaria de fazer?")
        print("1. Explorar profundo para encontrar tesouro ou inimigos")
        print("2. Retornar a cidade")
        print("3. Montar acampamento (restaura 10 vidas)")
        escolha = input("> ").lower()

        if escolha == "1" or "explorar" in escolha:
            explorar
        elif escolha == "2" or "retornar" or "cidade" in escolha:
            comprar_item("Voce deixa a floresta e retorna a cidade")
        elif escolha == "3" or "campo" in escolha:
            escrever_lento(
                "Voce montou um acampamento para descansar por minutos...")
            jogador["vida"] += min(jogador["vida"] + 10, 100)
            escrever_lento("voce se sente melhor um pouco")
        else:
            print("\n Eu nao entendo esta opcao. Por favor tentar novamente")


def explorar():
    escrever_lento("\n Tua aventura profunda dentro da floresta...")
    time.sleep(1)

    # 60% de chance no inimigo
    encontrador = random.choices(
        ["inimigo", "tesouro", "nada"], [60, 30, 10])[0]
    if encontrador == "inimigo":
        encontrador_inimigo()
    elif encontrador == "tesouro":
        encontrador_tesouro()
    else:
        escrever_lento(
            "\n Voce explorou um pouco mas nao encontrou nada interessante")


def encontrador_inimigo():
    inimigo = random.choice(inimigos)
    inimigo_vida = inimigo["vida"]

    escrever_lento(f"\n Voce encontrou um {inimigo['name']}!")
    while inimigo_vida > 0 and jogador["vida"] > 0:
        mostrar_estados()
        print("\nO que voce vai fazer?")
        print("1. X Atacar")
        print("2. Usar porcao de vida")
        print("1. Correr")

        escolha = input("> ").lower()
        if escolha == "1" or "atacar" in escolha:
            jogador_perigo = 5
            if "sword" in jogador["items"]:
                jogador_perigo += itens["socorro palavra"]["perigo"]
            inimigo_vida -= jogador_perigo
            escrever_lento(
                f"\n Voce ataca o {inimigo['name']} pelo {jogador_perigo} perigo!")

            if inimigo_vida <= 0:
                escrever_lento(f"Voce defendeu o {inimigo['name']}")
                jogador["ouro"] += inimigo['vida']
                escrever_lento(f"Voce encontrou {inimigo['vida']} ouro!")
                return
            jogador['vida'] -= inimigo['perigo']
            escrever_lento(f"\n O Inimigo {inimigo['name']} perigo")

            if jogador["vida"] <= 0:
                jogo_acabou()

        elif escolha == "2" or "porcao" in escolha:
            if "porcao vida" in jogador["items"]:
                jogador["items"].remove("porcao vida")
                jogador['vida'] = min(
                    jogador["vida"] + itens["porcao vida"], 100)
                escrever_lento(
                    f"Voce usou a porcao da vida e restarou {[itens['porcao vida']['vida']]} vida!")

            else:
                escrever_lento("Nao tens nenhuma porcao de vida")
                continue
            jogador["vida"] -= inimigo['perigo']
            escrever_lento(
                f" O inimigo {inimigo['name']} ataca voce por {inimigo['perigo']} perigo!")
            if jogador["vida"] <= 0:
                jogo_acabou()

        elif escolha == "3" or "correr" in escolha:
            if random.random() > 0.5:
                escrever_lento(" Voce conseguiu fugir")
                return
            else:
                escrever_lento(" Voce conseguiu fugir")
                jogador["vida"] -= inimigo["perigo"]
                escrever_lento(
                    f"O {inimigo['name']} atacou voce por {inimigo['perigo']} perigo!")
                if jogador["vida"] <= 0:
                    jogo_acabou()
        else:
            escrever_lento("Nao consigo entender isto, tente novamente!")


def encontrador_tesouro():
    encontro_ouro = random.randint(10, 30)
    jogador["ouro"] += encontro_ouro

    # random.random() 0.0 - 0.99
    if random.random() < 0.2 and "porcao vida" not in jogador["items"]:
        jogador['items'].append("porcao vida")
        escrever_lento("\n Voce encontrou um tesouro escondido")
        escrever_lento(
            f"Dentro estava {encontro_ouro} ouro e uma porcao de vida!")
    else:
        escrever_lento(
            "\n Voce encontrou uma poca pequena com algum ouro dentro")
        escrever_lento(f"\n Voce ganhou {encontro_ouro} ouro!")


def repouso():
    if jogador["ouro"] >= 10:
        jogador["ouro"] -= 10
        jogador["vida"] = 100
        escrever_lento("\n Voce repousa dentro e recupere tua saude.")
        escrever_lento(
            "Isto custou 10 ouros, mas voce se sente totalemente renovado")

    else:
        escrever_lento("\n Voce nao tem suficiente ouro para repousar dentro!")


def jogo_acabou():
    escrever_lento("\n Tua vida baixou para 0!")
    escrever_lento("FIM DO JOGO")
    print(f"\n Estatistica Final: {jogador['ouro']} ouro colectado")

    novamente = input("jogar de novo ? > ")
    if novamente.startswith("s"):
        jogo_comeca()
    else:
        escrever_lento("\nObrigado por jogar e Adeus")
        exit()


def jogo_comeca():
    jogador["vida"] = 100
    jogador["ouro"] = 50
    jogador["items"] = []

    escrever_lento("\n" + "="*50)
    escrever_lento("JOGO DA FLORESTA")
    escrever_lento("\n" + "="*50)
    escrever_lento("BEM VINDO AO JOGO SIMPLES DE AVENTURA")

    jogador["nome"] = input("\n Qual seu nome aventureiro? > ")
    escrever_lento(
        f"\n Bem-Vindo, {jogador['nome']}! Tua aventura comeca numa pequena cidade.")
    cidade()


jogo_comeca()
