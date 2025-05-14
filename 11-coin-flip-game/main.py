import random

print("JOGO ATIRA MOEDA - CARA OU COROA")
print("Advinhe Cara ou Coroa ")

while True:
    escolha = input("\n Insira a sua escolha (cara/coroa): ").lower()
    if escolha != "cara" and escolha != "coroa":
        print("Por favor insira 'cara' ou 'coroa'")
        continue
    virar_moeda = random.choice(["cara", "coroa"])

    print(f"\n A moeda mostra {virar_moeda}")
    if escolha == virar_moeda:
        print("Acertou corretamente!!!")
    else:
        print("Errou amigo")

    nova_tentiva = input("\n Quer tentar novamente (s/n)").lower()
    if not nova_tentiva.startswith("s"):
        print("Tchau")
        break