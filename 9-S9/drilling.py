def remplazar_datos_archivo(texto_viejo, texto_nuevo):
    try:
        archivo = open('informacion.dat', 'r', encoding='utf-8')  #  aperturar archivo
        lineas = archivo.readlines()  #  leer lineas
        archivo.close()  #  cerrar archivo

        remplazo = ""  #  acumular las lineas reemplazadas
        contador = 0  #  contador de lineas reemplazadas

        for linea in lineas:  #  se recorre la lista de lineas
            if texto_viejo in linea:  #  se verifica si el texto_viejo existe en la linea que se recorre
                linea = linea.replace(texto_viejo, texto_nuevo)  #  se reemplaza el texto_viejo con el texto_nuevo
                contador += 1  #  se cuenta el reemplazo
            remplazo += linea  # se acumula la linea

        if contador > 0:  #  se verifica el contador si se reemplazaron lineas 
            archivo_remplazo = open('informacion.dat', 'w')  #  se apertura
            archivo_remplazo.write(remplazo)  #  se escribe en el archivo
            archivo_remplazo.close()  #  se cierra el archivo

        print("Se realizaron {} remplazos".format(contador))

    except FileNotFoundError:
        print('No se encuentra el archivo informacion.dat')
    except Exception as error:
        print('Se ha generado un error no previsto:', type(error).__name__)

remplazar_datos_archivo("información", "Procesamiento")
