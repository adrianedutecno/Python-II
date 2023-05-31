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