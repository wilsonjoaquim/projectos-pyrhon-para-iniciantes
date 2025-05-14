import random

print("GERADOR DE RECEITAS ALEATÓRIOS")
proteinas = ["frango","bife","tofu","peixe","ovos"]
vegetais = ["brocolis", "cenouras","espinafre", "turtulhos"]
carbos = ["arroz","massa","batatas","pão"]
sabores = ["limao", "ervas","docoe"]
metodos = ["grelhado", "assado", "cozido", "dourado"]

while True:
    proteina = random.choice(proteinas)
    vegetai = random.choice(vegetais)
    carbo = random.choice(carbos)
    sabor = random.choice(sabores)
    metodo = random.choice(metodos)
    print(f"\nTua receita: {sabor} {metodo} {proteina} com {vegetai} e {carbo}")

    if not input("\nGerar uma outra receita? (s/n)").lower().startswith("s"):
        print("Tchau")
        break
