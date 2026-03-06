import socket

# La dirección que quieres investigar (puedes probar con 'google.com')
objetivo = input("Introduce la web o IP a escanear: ")
puertos_comunes = [21, 22, 80, 443, 3306]

print(f"\n--- Escaneando a: {objetivo} ---")

for puerto in puertos_comunes:
    # Creamos un "socket" (un conector de red)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # Si no responde en 1 segundo, pasamos al siguiente
    
    resultado = s.connect_ex((objetivo, puerto))
    
    if resultado == 0:
        print(f"[+] Puerto {puerto}: ABIERTO")
    else:
        print(f"[-] Puerto {puerto}: Cerrado")
    
    s.close()

print("\nEscaneo finalizado.")

