'''
'r': Por defecto, para leer el fichero.
'w': Para escribir en el fichero.
'x': Para la creación, fallando si ya existe.
'a': Para añadir contenido a un fichero existente.
'b': Para abrir en modo binario.

algunas funciones para files
open()
close()
write()
writelines()
read()
readline()
readlines()
'''

#carga de archivo, lectura y creacion si el archivo no existe
def load_file():
    try:
        with open('nombre_archivo.txt','r') as file:#apertura y cierra el archivo, se puede establecer el tipo de apertura, r es para leer
            datos = file.readlines() #retorna una lista de tipo str con todas las lineas existentes
    except FileNotFoundError: #si ocurre el error de archivo no existe, se procede a crearlo
        datos = []
        with open('nombre_archivo.txt','w') as file:
            file.writelines(datos) #crear el archivo si no existe, w es para escribir
    return datos

#crear solo el arhivo
def create_file():
    datos = []
    with open('nombre_archivo.txt','w') as file:
            file.writelines(datos) #crear el archivo si no existe, w es para escribir
    
#crear solo el arhivo y no cerrarlo automaticamente
def create_file():
    file = open('nombre_archivo.txt','w') #se crea el arhivo
    file.close() #se cierra el archivo
    
    
#guardado o escribiendo un dato dentro del archivo
def save_file():
    with open('nombre_archivo.txt','w') as file:
        dato = "dato a escribir"
        file.write(str(dato)) #se va escribiendo en el archivo

#guardado o escribiendo un dato dentro del archivo
def write_in_file():
    file = open('nombre_archivo.txt','w')
    file.write("dato a escribir") #se va escribiendo en el archivo
    file.close() #se cierra el archivo
            
