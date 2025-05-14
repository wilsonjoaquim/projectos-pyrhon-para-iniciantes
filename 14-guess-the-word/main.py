import random

print("Jogo Acerta a Palavra desordenada (Mexida kkk)")
print("Ordene a sequência das letras para encontrar a palavra")

palavras = [
    "aprender",
    "comida",
    "desafio",
    "certeza",
    "sumo"
]

while True: 
    palavra_sorteada = random.choice(palavras)
    letras = list(palavra_sorteada)
    random.shuffle(letras)
    palavra_mexida = "".join(letras)
    print(f"\nPalavra desordenada (mexida): {palavra_mexida}")
    escolha = input("Qual é a palavra correta correspondente? ").lower()
    if escolha == palavra_sorteada:
        print(f"Correcto!!! Você ganhou {palavra_mexida} corresponde a {palavra_sorteada}")
    else:
        print(f"Errou! A palavra correta era: {palavra_sorteada}")
    
    novo_jogo = input("Jogar novamente? (s/n)").lower()
    if not novo_jogo.startswith("s"):
        print("Tchau")
        break