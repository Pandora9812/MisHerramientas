import os
import shutil

# Ruta de la carpeta Descargas
ruta = os.path.expanduser("~/Downloads")

# Diccionario con tipos de archivos y sus carpetas
formatos = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".csv"],
    "Programas": [".deb", ".sh", ".py"]
}

print("Iniciando limpieza...")

# El "corazón" del programa: revisa cada archivo
for archivo in os.listdir(ruta):
    nombre, extension = os.path.splitext(archivo)
    for carpeta, ext_lista in formatos.items():
        if extension.lower() in ext_lista:
            # Crea la carpeta si no existe
            nueva_carpeta = os.path.join(ruta, carpeta)
            os.makedirs(nueva_carpeta, exist_ok=True)
            # Mueve el archivo a su lugar
            shutil.move(os.path.join(ruta, archivo), os.path.join(nueva_carpeta, archivo))
            print(f"Movido: {archivo} -> {carpeta}")

print("¡Limpieza terminada con éxito!")
