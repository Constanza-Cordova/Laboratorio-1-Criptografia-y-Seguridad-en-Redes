import socket
import struct
import sys
import time
def calculo_de_verificacion(paquete):
    checksum = 0
    count_to = (len(paquete)// 2 )* 2
    index = 0
    
    while index < count_to:
        word = paquete[index + 1]* 256 + paquete[index]
        checksum &= 0xffffffff
        checksum += word
        index +=2
        
    if count_to < len(paquete):
        checksum += paquete[len(paquete) - 1]
        checksum &= 0xffffffff
    checksum = (checksum >> 16) + (checksum & 0xffff)
    checksum += (checksum >> 16)
    result = ~checksum & 0xffff
    result = result >> 8 | (result << 8 & 0xff00)
    return result
 
def creacion_icmp_paquete(id, sequence_number, payload):
    header = struct.pack("!BBHHH",8, 0,0, id, sequence_number)
    paquete = header + payload.encode()
    checksum_value = calculo_de_verificacion(paquete)
    header= struct.pack("!BBHHH",8, 0, checksum_value, id, sequence_number)
    return header + payload.encode()

def enviar_icmp_paquete (ip_destino, paquete):
    icmp = socket.getprotobyname("icmp")
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) as sock:
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, struct.pack('I', 64))
        sock.sendto(paquete, (ip_destino, 0))
def main():           
        ip_destino = input("Ingrese la IP de destino:")
        texto= input("Ingrese el tecto a enviar en paquetes ICMP; ")
        
        id = 1
        sequence_number = 1
        
        source_ip = socket.gethostbyname(socket.gethostname())
        print(f"Enviando paquetes ICMP desde {source_ip} a {ip_destino}...")
         
        for char in texto:
            payload = f"{ord(char)}:{time.time()}"
            paquete = creacion_icmp_paquete(id, sequence_number, payload)
            enviar_icmp_paquete (ip_destino, paquete)
            sequence_number +=1
            time.sleep(0.1)
            
        print("Listo")
        
if __name__ == "__main__":
    main()
    