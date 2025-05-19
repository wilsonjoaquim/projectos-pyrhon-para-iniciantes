import random
import string


def gerar_palavra_passe(tamanho, minusculas, maiusculas, numeros, especial):
    caracteres = ""

    if minusculas:
        caracteres += string.ascii_lowercase
    if maiusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if especial:
        caracteres += string.punctuation
    if not caracteres:
        print("Oops! Nenhum tipo de caracter selecionado, usando carateres minusculas por padrao")
        caracteres = string.ascii_lowercase
    palavra_passe = ""
    for _ in range(tamanho):
        palavra_passe += random.choice(caracteres)
    return palavra_passe


def checar_forca_da_passe(palavra_passe):
    pontos = min(len(palavra_passe) / 16, 1.0)

    tem_minusculas = any(c.islower() for c in palavra_passe)
    tem_maiusculas = any(c.isupper() for c in palavra_passe)
    tem_digito = any(c.isdigit() for c in palavra_passe)
    tem_especial = any(c in string.punctuation for c in palavra_passe)

    variacao = (tem_maiusculas + tem_minusculas +
                tem_digito + tem_especial) / 4.0
    pontuacao_final = (pontos * 0.6) + (variacao * 0.4)

    if pontuacao_final >= 0.8:
        return "ULTRA FORTE PASSE KKK"
    elif pontuacao_final >= 0.4:
        return "DECENTE"
    else:
        return "Necessita de melhoria"


def obter_sim_nao_input(questao):
    while True:
        resposta = input(questao + "s(sim) ou n(nao)").lower()
        if resposta in ["sim", "s",]:
            return True
        elif resposta in ["nao", "n"]:
            return False
        else:
            print("Nao consegui perceber! Por favor insira 's' ou 'n'.")


def principal():
    print("\n ==== GERADOR DE PALAVRAS PASSE ====")
    print(" Criar uma palavra-passe forte e segura com facilidade")

    while True:
        try:
            tamanho = int(
                input("\nInsira o tamanho da palavra passe (8-30) > "))
            if 8 <= tamanho <= 30:
                break
        except ValueError:
            print("Oops! Por favor insira um numero, como 12 ou 16")
    print("\n Vamos customizar sua palavra-passe!")
    minuscula = obter_sim_nao_input("Incluir letras minusculas (a-z)? > ")
    maiuscula = obter_sim_nao_input("Incluir letras minuscula (A-Z)? > ")
    numeros = obter_sim_nao_input("Incluir numeros (0-9)? > ")
    especial = obter_sim_nao_input("Incluir caracteres especiais (!#@$)? > ")

    print("\n Gerando a sua palavra passe magica...")
    palavra_passe = gerar_palavra_passe(
        tamanho, maiuscula, maiuscula, numeros, especial)
    print("\n==== SUA NOVA PALAVRA PASSE ====")
    print(f" {palavra_passe}")

    forca = checar_forca_da_passe(palavra_passe)
    print(f" Forca: {forca}")

    if obter_sim_nao_input("Criar novamente uma passe magica?"):
        principal()
    else:
        principal("\nObrigado por usar o gerador de passes")


principal()
