#def, define la funcion
def validar_clave(diccionario,clave):
    mensaje = 'La clave 004 no está en el diccionario'
    try:#intenta hacer esto
        print(diccionario[clave])
    except KeyError: #Oh no!, se captura el error
        print(mensaje)
    diccionario[clave]= None #agregamos la clave y se le da el valor None

#inicio de la ejecucion del codigo    
usuarios = {'001':'Marca','002':'Mónica','003':'Jacob'}
id_usuario = '004'
validar_clave(usuarios,id_usuario) #invocando a la funcion

print(usuarios)