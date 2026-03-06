import socket

def escanear_banner(ip, puerto):
    try:
        # Creamos el conector
        s = socket.socket()
        s.settimeout(2) # No esperamos más de 2 segundos
        s.connect((ip, puerto))
        
        # Intentamos recibir el "saludo" del servidor (Banner)
        banner = s.recv(1024).decode().strip()
        print(f"[+] Puerto {puerto} ABIERTO: {banner}")
    except:
        # Si no responde con texto, al menos sabemos que está abierto
        print(f"[+] Puerto {puerto} ABIERTO (No soltó banner)")
    finally:
        s.close()

target = input("Introduce la IP del objetivo (ej. 192.168.1.1): ")
puertos = [21, 22, 25, 80, 443, 3306] # FTP, SSH, SMTP, HTTP, HTTPS, MySQL

print(f"\nIniciando recolección de información en {target}...\n")
for p in puertos:
    escanear_banner(target, p)

