def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero não é permitido."
    return a / b

def main():
    print("\n **** CALCULADORA SIMPLES ****")
    print("Seleciona a operação:")
    print("1. + Adição")
    print("2. - Subtração")
    print("3. X Multiplicação")
    print("4. / Divisão")

    while True:
        escolha = input("\nInsira a escolha (1-4): ")
        if escolha not in["1","2","3","4","5"]:
            print("Escolha inválida, somente é válido entre 1 e 4")
        else:
            break
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
    except ValueError:
        print("Dados inválidos, insira apenas números válidos")
        return
    
    if escolha == "1":
        print(f"\n {num1} + {num2} = {adicionar(num1, num2)}")
    if escolha == "2":
        print(f"\n {num1} - {num2} = {subtrair(num1, num2)}")
    if escolha == "3":
        print(f"\n {num1} * {num2} = {multiplicar(num1, num2)}")
    if escolha == "4":
        print(f"\n {num1} / {num2} = {dividir(num1, num2)}")

    novo = input("\n Quer fazer outro cálculo? (sim/não): ").lower()
    if not novo.startswith("s"):
        print("Tchau...")
        return
    else:
        main()
main()