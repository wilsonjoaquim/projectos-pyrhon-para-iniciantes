
def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)
def contar_caracterers(texto, espaco_incluido):
    if espaco_incluido:
        return len(texto)
    else:
        return len(texto.replace(" ",""))
def contar_frase(texto):
    frase_terminacao = [".","!","?"]
    conta = 0

    for caracter in texto:
        if caracter in frase_terminacao:
            conta += 1
    if conta == 0 and texto.strip():
        conta = 1
    return conta
def analiza_texto(texto):
    conta_palavras = contar_palavras(texto)
    conta_caracte_c_espaco = contar_caracterers(texto,True)
    conta_caracte_s_espaco = contar_caracterers(texto,False)
    conta_frases = contar_frase(texto)

    if conta_frases > 0:
        palavra_por_frase  = conta_frases / conta_palavras
    else:
        palavra_por_frase = 0
    
    if conta_palavras > 0:
        caracter_por_frase = conta_caracte_c_espaco / conta_palavras
    else:
        caracter_por_frase = 0
    print("=== Resultado da análise do texto ===")
    print(f". Words: {contar_palavras}")
    print(f". Caracteres (com espaço): {conta_caracte_c_espaco}")
    print(f". Caracteres (sem espaço): {conta_caracte_s_espaco}")
    print(f". Frases (com espaço): {conta_frases}")
    print(f". Média de palavras por frase: {palavra_por_frase:.1f}")
    print(f". Média de caracteres por palavra: {caracter_por_frase:.1f}")

    tempo_leitura_minutos = conta_palavras / 255
    if tempo_leitura_minutos < 1 :
        tempo_leitura_segundos = tempo_leitura_minutos * 60
        print(f". Tempo estimado para leitura: {tempo_leitura_segundos:.0f} segundos")
    else:
        print(f". Tempo estimado para leitura: {tempo_leitura_minutos:.1f} minutos")

def principal():
   print("==== CONTADOR DE PALAVRAS ====")
   print("Conta palavras, caracteres, e frases no seu texto")



   while True:
       print("\nEscolha uma opcao >  ")
       print("1. Insira um texto para analizar")
       print("2. Sair")

       escolha = input("\nTua escolha (1/2): ")
       if escolha == "1":
           print("\nInsira ou cola o texto abaixo (Pressione Enter duas vezes para finalizar): ")
           linhas  = []

           while True:
               linha = input()
               if not linha and not linhas[-1]:
                   break
               linhas.append(linha)
           texto = "\n".join(linhas)

           if not texto.strip():
               print("Nenhum texto fornecido, tente novamente")
               continue
           analiza_texto(texto)
       elif escolha == "2":
           print("Tchau")
           break
       else:
           print("Escolha inválida, escolha 1 ou 2.")

principal()