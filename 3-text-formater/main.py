print("Formatador de texto")
text = input("Insira o texto a formatar: ")
print("1. UPPERCASE\n2. lowercase\n3. Title Case\n4. Sentence Case")
escolha = int(input("Escolha o formato (1-4): "))

if escolha == 1:
    print(text.upper())
elif escolha == 2:
    print(text.lower())
elif escolha == 3:
    print(text.title())
elif escolha == 4:
    print(text.capitalize())
else:
    print("Opção inválida")
