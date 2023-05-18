def division():
    try:
        suma = 3000
        contador = 0
        resultado = suma / contador
        print(resultado)
        
    except ZeroDivisionError as e:
        print(f'Error: {e} no permitido') #Error: division by zero no permitido
        
division() #invocando a la funcion division()