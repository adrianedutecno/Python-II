"""
Las excepciones pueden ocurrir en el momento de transformacion, asignacion, evaluacion de variables o atributos
Las execepciones ocurren con errores de ejecución
Comunicando con entes externos al proyecto
class Exception es la clase principal de todos las excepciones que ocurran en la logica
"""
# Error aritmetico
def division():
    try:
        num1 = 10
        num2 = 0
        resultado = num1 / num2
        print(resultado)
        
    except ZeroDivisionError as e:
        print(f'Error: {e} no permitido') #Error: division by zero no permitido
    except Exception as error:
        print(f'Error: {error}')
'''
'''
# input invalido, transformacion de datos
def ingreso():
    try:
        ingreso = int(input('Ingrese un número: '))
        print(f'El numero ingresado es: {ingreso}')
    except ValueError as e:
        print(f'Error: {e} no permitido') #Error: invalid literal for int() with base 10: 's' no permitido
        
def division_ingreso():
    try:
        num1 = int(input('Ingrese primer numero: '))
        num2 = int(input('Ingrese segundo numero: '))

        resultado = num1 / num2
        print(resultado)
        
    except Exception as e:
        print(f'Error: {e} no permitido') #Error: division by zero no permitido
        division_ingreso() #recursividad

#crear excepcion propia, para ciertos casos        
class CustomException(Exception):
    def __init__(self, mensaje, codigo) -> None:
        super().__init__(mensaje)
        self.codigo = codigo

def excepcion_propia():
    try:
        edad = int(input("Ingrese edad para manejar exepciones: "))
        if edad < 0:
            raise CustomException("Excepcion propia ejecutada",460) #levantar exepcion
        print(f'edad: {edad}')
    except ValueError:
        print(f'Error: ingreso no es valido')
    except CustomException as e:
        print(f'Error: {e} y manejada')
        print(f'Error: {e.codigo}')

        
        
excepcion_propia()
