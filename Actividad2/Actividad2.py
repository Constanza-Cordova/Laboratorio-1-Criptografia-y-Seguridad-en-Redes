from scapy.all import IP, ICMP, send, Raw
import time

def enviar_icmp_custom(texto):
    seq = 1
    timestap = int(time.time() * 1000)
    timestap_hex = f"{timestap:016x}"
    
    for char in texto:
        hex_char = char.encode('utf-8').hex()
        playload = str(timestap_hex) + str(hex_char)
        paquete = IP(dst="127.0.0.1") / ICMP(seq=seq) / Raw(load=bytes.fromhex(playload))
    
    send(paquete)
    seq +=1
    time.sleep(1)

def main():
    texto = input("Ingrese el texto a enviar: ")
    enviar_icmp_custom(texto)
            
if __name__ == "__main__":
    main()