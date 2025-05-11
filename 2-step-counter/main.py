print("🏃Contador de passos 🏃")
meta = int(input("Qual é a tua meta diária de passos: "))
passos_dados = int(input("Quantos passos deu hoje: "))
restantes = (meta - passos_dados)
if restantes > 0 :
    print(f"Você precisa dar mais {restantes} passos para alcançar sua meta")
elif restantes < 0 :
    print(f"Parabéns! você excedeu a sua meta por {-restantes} passos.")
else:
    print(f"Parabéns, você alcançou a sua meta")