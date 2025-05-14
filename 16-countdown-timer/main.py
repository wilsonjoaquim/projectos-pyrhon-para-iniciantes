import time
print("\n *** Contador Regressiva ***")
print("Contagem regressiva ao segundo escolhido!")

while True:
    try:
        segundos = int(input("\n Insira o segundo de partida para contagem regressiva: "))
        # validar a entrada do valor
        if segundos <= 0:
            print("Por favor insira um valor positivo")
            continue
        print(f"Começando a contagem a partir de {segundos} segundos")
        for i in range(segundos,0,-1):
            print(f"{i} segundos restando...")
            time.sleep(1)
        print("Contagem completada!!!")
        responde = input("Deseja contar novamente (S/N)").lower()
        if not responde.startswith("s"):
            print("Tchau")
            break
    except ValueError:
        print("Por favor insira um número")
