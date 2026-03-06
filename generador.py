import random
import string
from datetime import datetime

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(caracteres) for i in range(longitud))

print("--- 🔐 MI GESTOR DE CLAVES OCULTO ---")
servicio = input("¿Para qué cuenta es? (ej: Netflix): ")
largo = int(input("¿Longitud? (Sugerido 20): "))
mi_password = generar_password(largo)
fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

with open(".mis_claves.txt", "a") as archivo:
    archivo.write(f"[{fecha}] {servicio}: {mi_password}\n")

print(f"\n✅ Clave para {servicio}: {mi_password}")
print("--- 💾 Guardada en el baúl oculto (.mis_claves.txt) ---")
