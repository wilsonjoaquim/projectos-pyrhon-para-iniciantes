print("CALCULADORA DE CLASSIFICAÇÃO DE NOTAS")

notas = []

while True:
    nota = input("Insira uma nota de exame (ou feito)")
    if nota.lower() == "feito":
        print("Goodbye")
        break
    notas.append(float(nota))
    media = sum(notas) / len(notas)
    print(f"Nota média: {media:.1f}")
    if media >= 90:
        print("Classe A")
    elif media >= 80:
        print("Classe B")
    elif media >= 70:
        print("Classe C") 
    else:
        print("Classe D ou F")

