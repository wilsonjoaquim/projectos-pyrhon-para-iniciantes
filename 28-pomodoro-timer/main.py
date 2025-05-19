import time
import os
import platform


def limpar_ecra():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def formatar_tempo(segundos):
    # formatar (30) => 00.30
    # formatar (75) => 01.15
    # formatar (0) => 00.00

    minutos = segundos // 60
    segundos_restador = segundos % 60
    return f"{minutos:02d}:{segundos_restador:02d}"


def contar_regressivo(segundos, etiqueta):
    for restante in range(segundos, 0, -1):
        limpar_ecra()
        print(f"\n *** {etiqueta} ***")
        print(f"\n# Tempo restante: {formatar_tempo(restante)}")

        if etiqueta == "Sessao Trabalho":
            print("\nFoca-te na tua tarefa!!")
        elif "Break" in etiqueta:
            print("\n Tire um repouso...")
        time.sleep(1)

    limpar_ecra()
    print(f"\n {etiqueta} completada")

    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)


def pomodoro():
    limpar_ecra()
    print("\n ==== TEMPORIZADOR POMODORO ====")
    # Definicoes padroes
    minutos_trabalho = 25
    minutos_intervalo_c = 5
    minutos_intervalo_l = 15
    ciclos = 4

    customiza = input(
        "\n Usa definicoes padrao (25min trabalho, 5min de intervalo curto, 15min de intervalo longo? (sim/nao): ").lower()
    if customiza != "sim" and customiza != "s":
        try:
            minutos_trabalho = int(
                input("Insira a duracao da sessao de trabalho (em minutos)> "))
            minutos_intervalo_c = int(
                input("Insira a duracao do intervalo curto (em minutos)> "))
            minutos_intervalo_l = int(
                input("Insira a duracao do intervalo longo (em minutos)> "))
            ciclos = int(
                input("Insira o numero de ciclos antes do intervalo longo> "))
        except ValueError:
            print("Valor invalido! Usando definicao padrao")
            time.sleep(2)

    limpar_ecra()
    print(f"\n Comecando o Temporizador Pomodoro com:")
    print(f". {minutos_trabalho} minutos de sessao de trabalho")
    print(f". {minutos_intervalo_c} minutos de intervalo menor")
    print(
        f". {minutos_intervalo_l} minutos de intervalo maior depois de {ciclos} ciclos")
    print(f". {minutos_intervalo_c} minutos de intervalo menor")
    print("\n Pressione CTRL+C em qualquer momento para sair")
    input("\nPressione Enter para comecar")

    # converter minutos em segundos
    segundos_trabalho = minutos_trabalho * 60
    segundos_intervalo_c = minutos_intervalo_c * 60
    segundos_intervalo_l = minutos_intervalo_l * 60

    ciclos_completos = 0
    try:
        while True:
            contar_regressivo(segundos_trabalho, "Sessao de Trabalho")
            ciclos_completos += 1

            if ciclos_completos % ciclos == 0:
                input(
                    "\nTempo para intervalo longo! Pressione Enter para comecar o intervalo...")
                contar_regressivo(segundos_intervalo_l, "Intervalo Longo")
                input(
                    "\nTempo de intervalo longo completo! Pressione Enter para comecar a proxima sessao de trabalho...")
            else:
                input(
                    "\nTempo para intervalo curto! Pressione Enter para comecar o intervalo...")
                contar_regressivo(segundos_intervalo_c, "Intervalo Curto")
                input(
                    "\nTempo de intervalo curto completo! Pressione Enter para comecar a proxima sessao de trabalho...")
    except KeyboardInterrupt:
        # limpar_ecra()
        print("Tchau")


pomodoro()
