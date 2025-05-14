import random
import time

pares_palavras = {
    "céu": ["azul","nuvem","pássaro","voo","sol"],
    "água": ["bebida","ocenano","peixe", "barco"],
    "comida":["comer","cozinhar","saboroso","refeição","restaurante"],
    "musica":["som","dança","ouvir","banda","ritmo"],
    "livro":["ler","página","autores","livraria"],
    "carro":["dirigir","estrada","roda","viajar","velocidade"]
}

print("\n *** JOGO DE ASSOCIAÇÃO DE PALAVRAS ***")
print("Responda com a palavra relacionada rapidamente")

pontuacao = 0
rondas = 0

while True:
    # selecionar uma palavra aleatoria
    comando = random.choice(list(pares_palavras.keys()))
    palavra_relacionada = pares_palavras[comando]

    print(f"\n Palavra de comando: {comando.upper()}")
    print("Rápido! Escreva uma palavra relacionada para este comando")

    # tempo de resposta do jogador
    tempo_inicio = time.time()
    resposta = input("> ").lower().strip()
    tempo_resposta = time.time() - tempo_inicio

    print("Tempo de resposta", tempo_resposta)

    # checar se a resposta é relacionada
    if resposta in palavra_relacionada:
        pontos = max(1, 5 - int(tempo_resposta))
        pontuacao += pontos
        print(
            f"Boa Associação + {pontos} (respondido em {tempo_resposta:.1f}s)")
    else:
        print(
            f"Associação Incomum. Palavras relacionadas incluidas: {', '.join(palavra_relacionada)}")
    
    rondas += 1
    print(f"Pontuação: {pontuacao}/{rondas * 5} possíveis pontos")


    # Perguntar para ganhas
    if input("\nJogar novamente? (Sim/Não): ").lower().startswith("n"):
        print(f"Pontuação final: {pontuacao}. Obrigado por jogar")
        break