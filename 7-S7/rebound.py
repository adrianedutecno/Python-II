"""Diseñe un programa en Python que pida la edad al usuario por consola. El usuario debe ingresarun número entero; en caso contrario, el programa arrojará una excepción y le solicitará queingrese su edad nuevamente.Seguidamente, el programa debe imprimir que es Adulto si es mayor o igual a 18; y en casocontrario, no es un adulto."""
while True:    
    try:        
        edad = int(input('Ingrese su edad: '))        
        break    
    except ValueError:        
        print('Error! Debe ser un número entero, intente nuevamente.')    
    except Exception as e:        
        print('Error, ', e)
        
        
if edad >= 18:    
    print('Usted es adulto.')
else:    
    print("Usted no es un adulto.")