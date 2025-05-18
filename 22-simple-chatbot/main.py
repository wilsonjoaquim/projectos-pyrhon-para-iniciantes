import random
import time

def chatbot():
    saudacoes = ["Olá!","Olá amigo",
                 "Oi, prazer em conhecer você","OIIII"]
    despedida = ["Vejo voce depois", "Adeus", "Até mais", "Pela próxima"]

    engracado = ["Por que o espantalho ganhou um prêmio? Porque ele era excepcional na sua área!",
                "Estou lendo um livro sobre a história da cola. Simplesmente não consigo parar!",
                "Eu costumava tocar piano de ouvido, mas agora uso as mãos.",
                "Como se chama um queijo que não é seu? Queijo Nacho!",
                "Eu disse à minha esposa que ela deveria aceitar seus erros. Ela me deu um abraço."]

    factos = ["Angola é um país de ÁFRICA",
                "Há um novo continente a ser desenvolvido na Ásia",
                "Existem 3 tipos de estado da matéria",
                "A indepencia foi conquistada em 1975"]
    nome_bot = "ChatBot"
    print(f" {nome_bot} está começando...")
    time.sleep(1)

    print(f"""
            Bem vindo ao {nome_bot}
            Eu posso conversar sobre:
            'Brincadeiras' - Ouça uma boa brincadeira
            'Factos' -  Aprenda alguma coisa nova
            'Cores' - Minha cor favorita
            'Tchau' - Fechar nossa conversa
        """)
    
    chatting = True
    nome_usuario = input("Qual é seu nome? > ").lower()
    print(f" {nome_bot}: Prazer em conhecer você, { nome_usuario}! Como posso ajudar você?")

    while chatting:
        input_usuario = input(" Voce: ").strip()
        if input_usuario in ["ola","oi","como vai","ei"]:
            print(f" {nome_bot}: {random.choice(saudacoes)}")
        elif "engracado" in input_usuario:
            print(f" {nome_bot} {random.choice(engracado)}")

        elif "factos" in input_usuario:
            print(f"{nome_bot}: {random.choice(factos)}")
        elif "cores" in input_usuario:
            print(f"{nome_bot}: Minha cor favorita é azul marinho! Qual a sua?")
            cor = input(" Voce: >").strip()
            print(f" {nome_bot}: {cor} é uma boa cor!")
        elif input_usuario in ["chau","adeus","sair","romper"]:

            print(f" {nome_bot}: {random.choice(despedida)}")
            print(f" {nome_bot}: Foi divertido conversar contigo, {nome_usuario}")
            chatting = False
        else:
            respostas = [
            "Isto e interessante! Conta-me mais.",
            "Eu nao estou certo que entendi. Pode tentar novamente",
            "Hmm, vamos falar sobre alguma coisa qualquer. Tente perguntar por uma brincadeira ou facto",
            "Meu cerebro robo está processando isto..."
            ]
            print(f" {nome_bot}: {random.choice(respostas)}")
    
    print("Obrigado por conversar comigo")
chatbot()