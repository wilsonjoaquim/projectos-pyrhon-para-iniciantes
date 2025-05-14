import random

print("Seja Bem-vindo ao jogo Acerte o número")
print("Estou pensando num número de 1 a 100. Tu tens 10 Tentativas")

def jogar():
    tentativas = 1
    numero_escolhido = random.randint(1,100)

    while tentativas <= 10:
            print("Tentativa {}/10".format(tentativas))
            escolha = int(input())
            if escolha == numero_escolhido:
                print(f"\nParabéns você acertou o número {numero_escolhido} em {tentativas} tentativas")
                break
            elif escolha != numero_escolhido and tentativas == 10:
                print("Tentativas esgotadas")
                break 
            elif escolha > numero_escolhido:
                print("\nMuito alto. Tente um número abaixo!")
                tentativas += 1
                continue
            elif escolha < numero_escolhido:
                print("\nMuito baixo, tente um número acima disto!")
                tentativas += 1
                continue
            
def menu():
        jogar()   
        resposta = input("\nGostaria de jogar novamente? (s/n)")
        if not resposta.startswith("s"):
            print("Obrigado por jogar, até mais...")
        else:
             jogar()

menu()
