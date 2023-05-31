#clase vehiculo
class Vehiculo:
    #constructor
    def __init__(self, marca , modelo , numero_ruedas) -> None:
        #atributos del objeto Vehiculo
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
        
#clase Automovil hereda de Vehiculo
class Automovil(Vehiculo):#Herencia con Vehiculo
    #constructor
    def __init__(self, marca , modelo , numero_ruedas , velocidad , cilindrada) -> None:
        super().__init__(marca, modelo , numero_ruedas)
        #atributos del objeto Automovil
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self) -> str:
        return f'Marca: {self.marca}, Modelo: {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada}cc'

#clase Particular hereda de Automovil
class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos) -> None:
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puestos = numero_puestos
    

#clase Carga hereda de Automovil
class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga) -> None:
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga
    

#clase Bicicleta hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo) -> None:
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo
        
    
#clase Motocicleta hereda de Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, numero_radios, cuadro, motor) -> None:
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.numero_radios = numero_radios
        self.cuadro = cuadro
        self.motor = motor
        
        
#crear las instancias necesarias para practicar
#verificar las instancias con isinstance(), funcion o metodo para verificar de que tipo es el dato u objeto


























def imprimir_objetos(lista):
        for i in lista:
            print(str(i))

def crear_automovil():
    marca = input('Ingrese la marca: ')
    modelo = input('Ingrese el modelo: ')
    numero_ruedas = input('Ingrese el número de ruedas: ')
    velocidad = input('Ingrese la velocidad: ')
    cilindrada = input('Ingrese la cilindrada: ')
    
    #instancia, permiten acceder a las clases y crear objetos
    return Automovil(marca,modelo,numero_ruedas,velocidad,cilindrada)       

ingreso = int(input('Ingrese cuantos vehiculos se crearan: ')) 
lista = [] #lista vacia
for i in range(1,ingreso + 1):
    automovil_creado = crear_automovil()
    lista.append(automovil_creado)
    print(f'Se ha creado el automovil numero {i}')
    print(str(automovil_creado))

print('La lista de automoviles creados es:')
print(imprimir_objetos(lista))