import random

print("GERADOR DE NOMES FANTASIA")

parte_um = ["Sky", "Star", "Moon", "Sun", "Fire", "Ice"]
parte_dois = ["Rider", "Walker", "Hunter",
              "seeker", "dancer", "keeper","fulano"]

qtd_nomes = int(input("Quantos nomes queres? "))

for i in range(qtd_nomes):
    primeiro_nome = random.choice(parte_um)
    segundo_nome = random.choice(parte_dois)
    print(f" {primeiro_nome}{segundo_nome}")