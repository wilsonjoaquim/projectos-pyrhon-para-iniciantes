import random

print("MUSIC RECOMMENDER\n")

generos = {
    "rock": ["AC/DC","Queen", "Led Zeepelin"],
    "pop": ["Taylor Swift", "Ed Sheeran", "Michael Jackson"],
    "hip-hop": ["Kendrik lamar", "Drake", "J Cole"]
}

escolha = input("Qual o género musical que gostas (rock/pop/hip-hop): ")
if escolha not in generos:
    print("Desculpa, eu não conheço este género.")
else:
    print(f"Sugiro este aqui {random.choice(generos[escolha])}")


