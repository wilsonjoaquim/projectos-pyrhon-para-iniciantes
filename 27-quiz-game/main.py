import random
import time


def bemvindo():
    print("\n" + "=" * 50)
    print("Bem-vindo ao Desafio Ate ao Ultimo Quiz".center(50))
    print("=" * 50)
    print("\n Instrucoes:")
    print("-Escolha uma categoria de quiz")
    print("-Responda a questao multipla-escolha")
    print("-Cada resposta correta vale 10 pontos")
    print("-Veja a tua pontuacao final no fim")
    print("-Divirta-se e aprenda alguma coisa nova!")


def categorias():
    print("\nCategorias do Quiz:")
    print("1. Conhecimento Geral")
    print("2. Filmes e programas tv")
    print("3. Ciencia e Natureza")
    print("4. Ronda Mix (questoes de todas as categorias)")
    print("-Divirta-se e aprenda alguma coisa nova!")


def escolha_usuario():
    while True:
        try:
            escolha = int(input("\nSelecione uma categoria(1-5): "))
            if 1 <= escolha <= 5:
                return escolha
            else:
                print(f"por favor insira um numero entre (1-5)")
        except ValueError:
            print("Apenas valores validos")


def processar_questoes():

    geral = [
        {
            "questao": "Qual a capital de Franca?",
            "opcoes": ["A. Londres", "B. Berlin", "C. Paris", "D. Madrid"],
            "resposta": "C"
        },
        {
            "questao": "Qual planeta e conhecido como Vermelho?",
            "opcoes": ["A. Venus", "B. Marte", "C. Jupter", "D. Saturno"],
            "resposta": "B"
        },
        {
            "questao": "Quantos lados tem um hexagono?",
            "opcoes": ["A. 5", "B. 8", "C. 6", "D.7"],
            "resposta": "B"
        }
    ]

    filmes = [
        {
            "questao": "Quem actuou com Iron Man na Marvel?",
            "opcoes": ["A. Chris Evans", "B. Robert Dowwneyn", "C. Chris Hems", "D. Mark Ruffalo"],
            "resposta": "B"
        },
        {
            "questao": "Como se chama o filme com carros velozes?",
            "opcoes": ["A. Velocidade maluca", "B. Maluquice na estrada", "C. Velocidade Furiosa", "D. O piloto diurno"],
            "resposta": "C"
        },
        {
            "questao": "Quantos premios tem o Jackie chan?",
            "opcoes": ["A. 1", "B. 4", "C. 3", "D.+29"],
            "resposta": "B"
        }
    ]

    ciencia = [
        {
            "questao": "Quem e o pai da quimica?",
            "opcoes": ["A. Chris fred", "B. Antoine Lavoiser", "Sulivan Mafb", "Demidovitch"],
            "resposta": "B"
        },
        {
            "questao": "qual e a raiz quadrada de 16?",
            "opcoes": ["A. 1", "B. 3", "C. 12", "D. 4"],
            "resposta": "D"
        },
        {
            "questao": "Quantos estados da materia existem?",
            "opcoes": ["A. 1", "B. 4", "C. 3", "D.20"],
            "resposta": "C"
        }
    ]

    return {
        1: {"nome": "Geral", "questoes": geral},
        2: {"nome": "filmes", "questoes": filmes},
        3: {"nome": "ciencia", "questoes": ciencia},
        4: {"nome": "ciencia", "questoes": ciencia + geral + filmes}
    }


def rodar_quiz(categoria):
    categoria_nome = categoria["nome"]
    questoes = categoria["questoes"]

    random.shuffle(questoes)
    print(f"\n Comecando a {categoria_nome} quiz!")
    print("Responda a questao escrevendo a letra a sua escolha (A,B,C ou D)")

    pontos = 0
    correta_respostas = 0
    for i, q in enumerate(questoes):
        print(f"\n------- Questao {i+1}/{len(questoes)}-------")
        print(f"? {q["questao"]}")

        for opcao in q["opcoes"]:
            print(opcao)
        while True:
            resposta = input("\nSua resposta: (A/B/C/D): ").upper()
            if resposta not in ["A", "B", "C", "D"]:
                print("Insira A,B,C ou D")
            else:
                break
        correta = resposta == q["resposta"]
        if correta:
            pontos += 10
            correta_respostas += 1
            print("Correto! + 10 pontinhos")
        else:
            print(f"Errado! A resposta correta e {q["resposta"]}")

        if i < len(questoes) - 1:
            print("Proxima questao...")
            time.sleep(1.5)
    print("\n" + "=" * 50)
    print("RESULTADOS DO QUIZ".center(50))
    print("=" * 50)
    print(f"Categoria: {categoria_nome}")
    print(f"Respostas certas: {correta_respostas}")
    print(f"Pontos total: {pontos}")

    percentagem = (pontos / len(questoes) * 10) * 100
    if percentagem == 100:
        print("\n PERFEITA PONTUACAO! TU ES BOM(BOA)")
    elif percentagem >= 80:
        print("EXCELENTE")
    elif percentagem >= 60:
        print("BOM TRABALHO")
    elif percentagem >= 40:
        print("NAO MUITO MAL")
    else:
        print("CONTINUE APRENDENDO")
    return pontos


def principal():
    bemvindo()

    total_pontuacao = 0
    jogar_novo = True
    while jogar_novo:
        categorias()
        escolha_categoria = escolha_usuario()

        todas_categorias = processar_questoes()
        pontos = rodar_quiz(todas_categorias[escolha_categoria])

        total_pontuacao += pontos

        de_novo = input("\nJogar novamente? (sim/nao) ").lower()

        while not (de_novo.startswith("s") or de_novo.startswith("n")):
            print("Por favor insira sim ou nao")
            de_novo = input("\nJogar novamente? (sim/nao) ").lower()

        jogar_novo = de_novo.startswith("s")

    print(
        f"Obrigado por jogar. Tua pontuacao total de todos os rondos: {total_pontuacao}")


principal()
