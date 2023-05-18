usuarios = {'001':'Marca','002':'Mónica','003':'Jacob'}
id_usuario = '004'
mensaje = 'La clave 004 no está en el diccionario'
try:#intenta hacer esto
    print(usuarios[id_usuario])

except KeyError: #Oh no!
    print(mensaje)
usuarios[id_usuario]= None #le asignamos valor al error

print(usuarios)