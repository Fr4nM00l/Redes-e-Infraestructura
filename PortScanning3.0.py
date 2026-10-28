from email import errors
import socket
from datetime import datetime
import concurrent.futures

def obtener_banner(s):
    try:
        banner_bytes=s.recv(1024)
        return banner_bytes.decode('utf-8',errors='ignore').strip()
    except :
        return "No se pudo obtener el banner (servicio silencioso o timeout)"


def escaner(puerto,target):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        resultado=s.connect_ex((target, puerto))

        if resultado==0:
            banner=obtener_banner(s)
            print(f"Puerto {puerto} Abierto || Servicio: {banner}")
        s.close()
    except Exception as e:
        print(f"Error escaneando el puerto {puerto}: {e}")
        return None
    except KeyboardInterrupt:
        print("Escaneo interrumpido por el usuario")
        exit()
    except socket.gaierror:
        print("No se pudo resolver el nombre del host")
        exit()
    except socket.error:
        print("No se pudo conectar al servidor")
        exit()

def runner(target):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for puerto in range(1,65535):
            executor.submit(escaner, puerto, target)

if __name__ == "__main__":
    target=print("Ingrese la direccion IP a escanear: ")
    target=input()
    runner(target)
    print("Escaneo finalizado")