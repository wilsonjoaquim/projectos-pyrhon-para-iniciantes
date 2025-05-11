print("Contador de Vogais")

while True:
    texto = input("\nInsira um texto (ou saia): ")
    if texto.lower() == "saia":
        break
    contador_vogais = 0
    #for letra in texto.lower():
        #if letra in ["a","e","i","o","u"]:
            #contador_vogais +=1
    
    vogais = sum(1 for char in texto.lower() if char in "aeiou")
    print(f"Este texto tem {vogais} vogais")