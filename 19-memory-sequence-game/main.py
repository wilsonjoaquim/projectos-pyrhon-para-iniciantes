import time
import os
import random

def limpar_ecra():
    """Limpar a tela do terminal"""
    os.system("cls" if os.name == "nt" else "clear")

print("**** JOGO DE MEMORIA SEQUENCIAL ****")
print("Lembra a sequência e escreva de volta!")
print("\nRegras:\n-Veja como os números aparecem um a um\n" \
        "-Depois que a sequência é mostrada, escreva de volta na mesma ordem\n" \
        "-Cada ronda acresce mais um número para lembrar\n" \
        "Quão longe você pode ir?\n")

input("Pressione enter para começar")

sequencia = []
ronda_actual = 1
fim_jogo = False

while not fim_jogo:
    sequencia.append(random.randint(1,9))
    limpar_ecra()

    print(f"\n === Ronda {ronda_actual} ===")
    print(f"Lembre esta sequência de {len(sequencia)} números: ")
    for numero in sequencia:
        time.sleep(0.8)
        print(f"\n{numero}")
        time.sleep(0.8)
        limpar_ecra()
    
    print("\nAgora repita a sequência escrevendo cada número, separado por espaços")
    resposta = input("> ")

    # converter o meu input "2,1,3" em uma lista ["2","1","3"] => [2,1,3]
    try:
        resposta_sequencial = [int(numero) for numero in resposta.split()]
    except ValueError:
        print("Por favor insira números apenas")
        fim_jogo = True
        continue

    # checar a resposta do user
    if resposta_sequencial == sequencia:
        print(f" Parabéns você lembrou todos os {len(sequencia)} números")
        ronda_actual += 1
        time.sleep(2)
    else:
        print(f"Fim do jogo! Tu lembraste todos os {ronda_actual-1} numeros")
        print(
            f"A sequência correta era: {" ".join(str(num) for num in sequencia)}"
        )
        fim_jogo = True

    # perguntar se quer jogar novamente
    if fim_jogo:
        jogar = input("Quer jogar novamente (sim/nao)").lower()
        if jogar.startswith("s"):
            sequencia = []
            ronda_actual = 1
            fim_jogo = False
        else:
             print("tchau")
