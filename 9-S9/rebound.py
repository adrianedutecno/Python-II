def agregar_info_al_archivo(texto):
    try:
        with open ("informacion.dat", "a", encoding="utf-8") as file:
            file.write(texto+"\n")
    except FileNotFoundError:
        print("ERROR: ARCHIVO NO ENCONTRADO")
    except Exception as e:
        print("ERROR: ", e)
agregar_info_al_archivo("Hola Mundo")
agregar_info_al_archivo("Este en una nueva línea en el archivo")
agregar_info_al_archivo("finalizando la línea agregada")