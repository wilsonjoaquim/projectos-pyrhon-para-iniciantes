import random
print("BARALHADOR DE PALAVRAS")

while True:
    palavra = input("Insira uma palavra para misturar (ou sair): ")
    if palavra.lower() == "sair":
        print("Tchau")
        break
    letras = list(palavra)
    random.shuffle(letras)
    print(f"Baralhadas: {"".join(letras)}")