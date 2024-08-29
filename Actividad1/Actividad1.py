def cifrar_cesar(texto, corrimiento):
    resultado=""
    for char in texto:
        if char.isalpha():
            desplazamiento = corrimiento % 26 
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            resultado += chr((ord(char) - base + desplazamiento)%26 + base)
        else:
            resultado += char
    return resultado

def main():
    texto = input("Ingrese el texto a cifrar: ")
    corrimiento = int(input("Ingrese el corrimiento (número entero): "))
    texto_cifrado = cifrar_cesar(texto, corrimiento)
    print("Texto cifrado:", texto_cifrado)
    
    
if __name__ == "__main__":
    main()