import random

print("Bem-vindo ao jogo de advinha de números")
print("Estou pensando num número entre 1 e 100. Tens 10 tentativas")

jogando = True
while jogando:
    numero_secreto = random.randint(1,100)
    tentativas = 0
    tentativas_max = 10

    fim_jogo = False

    while tentativas < tentativas_max and not fim_jogo:
        try:
            escolha = int(input(f"Tentativa {tentativas + 1}/{tentativas_max}. Insira a sua escolha: "))
        except ValueError:
            print("Por favor insira um número válido")
            continue
        
        tentativas += 1
        if escolha < numero_secreto:
            print("Muito baixo! Tentar um número maior")
        elif escolha > numero_secreto:
            print("Muito alto! Tentar um numero menor")
        else:
            print(f"Parabéns! Você acertou o numero {numero_secreto} em {tentativas} tentativas")
            fim_jogo = True

        if tentativas < tentativas_max and not fim_jogo:
            print(f"Tu tens {tentativas_max - tentativas} tentativas restantes")
    if not fim_jogo:
       print(f"Fim do jogo. O número era {numero_secreto}") 
    
    jogar_novamente = input("Jogar novamente (S/N)").lower()
    if jogar_novamente.startswith("s"):
        print("Novo jogo...\n")
    else:
        print("Adeus")
        jogando = False
