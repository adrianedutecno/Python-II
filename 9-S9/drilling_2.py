with open("informacion.dat", "r+") as archivo:
    contenido = archivo.read()
    contador_reemplazos = contenido.count("Informacion")
    nuevo_contenido = contenido.replace("Informacion", "Procesamiento")
    archivo.seek(0)
    archivo.write(nuevo_contenido)
    archivo.truncate()
print(f"Se realizaron: {contador_reemplazos} reemplazos")
print("El contenido del archivo informacion.dat es:")

with open("informacion.dat", "r") as archivo:
    contenido = archivo.read()
    print(contenido)