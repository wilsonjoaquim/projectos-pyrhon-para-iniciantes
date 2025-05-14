print("MISTURADOR DE COR")

cores = {
    ("vermelho", "azul"): "roxo",
    ("vermelho","amarelo"): "laranja",
    ("azul", "amarelo"): "verde",
    ("azul", "verde"): "leite",
    ("branco", "vermelho"): "rosa",
    ("vermelho", "verde"): "castanho"
    }

while True:
    cor1 =input("Insira a cor primária: ").lower().strip()
    cor2 = input("Insira a cor secundária: ").lower().strip()

    mistura = None
    if (cor1,cor2) in cores:
        mistura = cores[cor1,cor2]
    elif (cor2, cor1) in cores:
        mistura = cores[cor2, cor1]
    if mistura:
        print(f"Quando você mistura {cor1} e {cor2}, tu tens {mistura}")
    else:
        print("Eu não sei se que cores dão ao misturar")
    escolha = input("\n Misturar mais cores ou não (s/n)").lower()
    if not escolha.startswith("s"):
        print("Tchau") 
        break
