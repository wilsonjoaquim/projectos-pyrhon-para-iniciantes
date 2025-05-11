print("Verificador de tipos de caracter")
char = input("Insira um único caracter: ")

if char.isalpha():
    print("É uma letra")
elif char.isdigit():
    print("É um digito")
else:
    print("É um caracter especial")