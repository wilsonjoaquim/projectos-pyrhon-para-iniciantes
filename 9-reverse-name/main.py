print("REVERSE NAME GENERATOR")

while True:
    name = input("Insira um nome: ")
    print(f"Teu nome inverso é: {name[::-1]}")
    print(f"Num universo paralelo, eles te chamam de {name[::-1].title()}")
    escolha = input("\nTentar com outro nome? (s/n) ")
    if escolha.lower() != "s":
        print("Tchau")
        break
    
    