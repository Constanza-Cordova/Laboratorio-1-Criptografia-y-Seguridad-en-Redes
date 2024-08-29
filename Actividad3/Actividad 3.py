def descifrar_cesar(texto_cifrado, corrimiento):
    resultado =""
    for char in texto_cifrado:
        if char.isalpha():
            desplazamiento = corrimiento % 26 
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            resultado += chr((ord(char) - base - desplazamiento) %26 + base)
        else:
            resultado += char
    return resultado
           
def es_mensaje_probable(texto): 
    palabras_comunes = ["the", "and", "is", "in", "to", "of"]
    texto_lower = texto.lower()
    return any(palabra in texto_lower for palabra in palabras_comunes)

def imprimir_resultados(texto_cifrado):
    mejor_corrimiento = None
    mejor_texto = None
    for corrimiento in range(26):
        texto_descifrado = descifrar_cesar(texto_cifrado, corrimiento)
        print(f"{corrimiento}:{texto_descifrado}")
        if es_mensaje_probable(texto_descifrado):
            mejor_corrimiento = corrimiento
            mejor_texto = texto_cifrado
    if mejor_texto:
        print(f"\033[92mCorrimiento Probable:{mejor_corrimiento}\nTexto descifrado: {mejor_texto}\033[m")
    else:
        print(f"No se encontro un texto descifrado probable")     
        
    return mejor_corrimiento, mejor_texto
    
def main():
    texto_cifrado = input("Ingrese el texto cifrado: ")
    print("\Probando todas las combunaciones posibles de corriemiento: ")
    imprimir_resultados(texto_cifrado)
    
    
if __name__ == "__main__":
    main()