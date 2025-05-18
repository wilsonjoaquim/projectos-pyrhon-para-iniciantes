import time
import random
def boas_vindas():
    print("PEDRA PAPEL TESOURA")
    print("\nREGRAS:")
    print("- PEDRA machoca TESOURA")
    print("- TESOURA corta PAPEL")
    print("- PAPEL cobre PEDRA")
    print("Primeiro a ganhar 3 Rounds é o campeão")
    print("\n--------------------------------------")

def obter_escolha_usuario():
    while True:
        print(f"\n Faça a sua escolha:")
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        try:
            escolha = int(input("Escolha (1-3) > "))
            if 1 <= escolha <= 3:
                return escolha
            else:
                print("Por favor somente 1 a 3")
        except ValueError:
            print("Insira um numero valido")

def obter_escolha_computador():
    return random.randint(1,3)

def converter_escolha_p_texto(escolha):
    opcoes = {
        1 :"Pedra",
        2 :"Papel",
        3 :"Tesoura"
    }
    return opcoes[escolha]

def determinar_vencedor(escolha_usuario,escolha_computador):
    # empate
    if escolha_usuario ==  escolha_computador:
        return "empate"
    # caso usuario vencedor:
    elif ((escolha_usuario == 1 and escolha_computador == 3) or
          (escolha_usuario == 2 and escolha_computador == 1) or
          (escolha_usuario == 3 and escolha_computador == 2)):
        return "Utilizador"
    else:
        return "Computador"

def ronda_resultado(escolha_usuario, escolha_computador,resultado):

    texto_usuario = converter_escolha_p_texto(escolha_usuario)
    texto_computador = converter_escolha_p_texto(escolha_computador)
    print(f"Voce escolheu: {texto_usuario}")
    print("Computador está escolhendo", end="")

    for _ in range(3):
        print(".", end="",flush=True)
        time.sleep(0.5)
    print(f"Computador escolheu: {texto_computador}")

    if resultado == "empate":
        print("Isto é um Empate!")
    elif resultado == "Utilizador":
        print("Voce venceu este round!")
    else:
        print("Computador venceu este round!")
    
def iniciar_jogo():
    """Funcao Principal do Jogo"""
    boas_vindas()

    pontuacao_usuario = 0
    pontuacao_computador = 0
    pontuacao_meta = 3
    rounda_numero = 1

    while pontuacao_usuario < pontuacao_meta and pontuacao_computador < pontuacao_meta:
        print(f"\n ==== Ronda {rounda_numero} ====")
        print(f"Pontuacao: Voce {pontuacao_usuario} - {pontuacao_computador} Computador")
        
        escolha_usuario = obter_escolha_usuario()
        escolha_computador = obter_escolha_computador()

        resultado = determinar_vencedor(escolha_usuario,escolha_computador)
        ronda_resultado(escolha_usuario, escolha_computador,resultado)

        if resultado == "Utilizador":
            pontuacao_usuario += 1
        elif resultado == "Computador":
            pontuacao_computador += 1
        
        rounda_numero += 1
    print("\n==== Fim do Jogo ====")
    print(f"Pontuacao final: Voce {pontuacao_usuario} - {pontuacao_computador} Computador")

    if pontuacao_usuario > pontuacao_computador:
        print("Parabens! Voce é o ** campeao **")
    else:
        print("Boa sorte pela proxima! O computador venceu este jogo.")
    
    jogar_novo = input("\nQuer jogar novamente (s/n)? ").lower()
    if jogar_novo.startswith("s"):
        iniciar_jogo()
    else:
        print("Tchau")
        

iniciar_jogo()