tarefas = []

def menu():
    print("\n=== Gestor de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefa")
    print("3. Completar Tarefa")
    print("4. Deletar Tarefa")
    print("0. Sair")
    print("===================================")

def adicionar_tarefa():

    titulo = input("\nInsira o título da tarefa >")
    tarefas.append({"titulo": titulo, "completada": False})
    print(f"Tarefa {titulo} adicionada com sucesso!")

def visualizar_tarefa():

    if not tarefas:
        print("Nenhuma tarefa encontrada")
        return False
    print("\n=== Minhas Tarefas ===")

    for indice, tarefa in enumerate(tarefas):
        estado = "✔" if tarefa["completada"] == True else " "
        print(f"{indice + 1}. [{estado}] {tarefa["titulo"]}")
    
    print("=============================")

def completar_tarefa():
    
    visualizar_tarefa()

    if not tarefas:
        return
    
    try:
        tarefa_num = int(input("Insira o número da tarefa p/ marcar como completada >"))
        if tarefa_num < 1 or tarefa_num > len(tarefas):
            print("Número da tarefa inválido")
            return
        
        tarefa_a_completar = tarefas[tarefa_num - 1]
        tarefa_a_completar["completada"] = True
        print(f"Tarefa '{tarefa_a_completar["titulo"]}' marcada como completada!")

    except ValueError:
        print("Por favor, insira um número válido")


def deletar_tarefa():

    visualizar_tarefa()

    if not tarefas:
        return
    
    try:
        tarefa_num = int(input("Insira o numero da tarefa a deletar> "))

        if tarefa_num < 1 or tarefa_num > len(tarefas):
            print("Número de tarefa inválido")
            return
        
        tarefa_a_deletar = tarefas.pop(tarefa_num)
        print(f"Tarefa '{tarefa_a_deletar["titulo"]}' deletada com sucesso!")
    except ValueError:
        print("Por favor insira um numero valido")

def principal():
    """Funcao principal do codigo responsavel por chamar outras funcoes"""
    
    while True:
        menu()
        escolha = input("Faça a sua escolha (0-4)> ").strip()

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            visualizar_tarefa()
        elif escolha == "3":
            completar_tarefa()
        elif escolha == "4":
            deletar_tarefa()
        elif escolha == "0":
            print("bye bye")
            break
        else:
            print("Apenas são válidas as opções (0-4)")
principal()