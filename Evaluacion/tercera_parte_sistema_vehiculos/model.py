import csv

#clase vehiculo
class Vehiculo:
    #constructor
    def __init__(self, marca , modelo , numero_ruedas) -> None:
        #atributos del objeto Vehiculo
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
        
    def guardar_datos_csv(self,nombre_archivo):
        try: #intentar ejecutar
            archivo = open(nombre_archivo, "a+", newline='') # a+ abre el archivo y escribe, si no existe lo crea
            datos = [(self.__class__, self.__dict__)] # se crea una lista con tupla interna
            archivo_csv = csv.writer(archivo) # se apertura la escritura del archivo
            archivo_csv.writerows(datos) # se escribe dentro del archivo
            archivo.close() # se cierra el archivo
        except FileNotFoundError: #archivo no existe
            print('Error: File not found:',nombre_archivo)
            # with open(nombre_archivo, 'w'): #forma de crear
            #     print('archivo creado')
        except Exception as e:
            print('Error:',e)
        
    def recuperar_datos_csv(self,nombre_archivo): 
        try: #intentar ejecutar
            vehiculos = [] # lista para agregar los datos o lineas leidas desde el archivo, en cada posicion de la lista
            archivo = open(nombre_archivo, "r") # r, se abre el archivo como escritura
            archivo_csv = csv.reader(archivo) # se establece escribir el archivo con .reader()
            for vehiculo in archivo_csv: # se recorre la lista obtenida de la lectura
                vehiculos.append(vehiculo) # se agrega el objeto temporal vehiculo dentro de la lista con .append()
            archivo.close() # se cierra el archivo
            return vehiculos
        except FileNotFoundError: #archivo no existe
            print('Error: File not found:',nombre_archivo)
        except Exception as e:
            print('Error:',e)
        
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
particular = Particular("Ford", "Fiesta", "4", "180", "500", "5") 
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
#verificar las instancias con isinstance(), funcion o metodo para verificar de que tipo es el dato u objeto
print('Moticicleta es instancia de Particular: ', isinstance(motocicleta,Particular))
print('Moticicleta es instancia de Carga: ', isinstance(motocicleta,Carga))
print('Moticicleta es instancia de Bicicleta: ', isinstance(motocicleta,Bicicleta))
print('Moticicleta es instancia de Vehiculo: ', isinstance(motocicleta,Vehiculo))
print('Moticicleta es instancia de Vehiculo: ', isinstance(motocicleta,Motocicleta))

"""
Crear el método que permita guardar cada uno de los objetos previamente creados en el archivo vehiculos.csv, 
el nombre del método es: guardar_datos_csv(self)
Tome como referencia los siguientes objetos: 
particular = Particular("Ford", "Fiesta", "4", "180", "500", "5") 
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

• En el archivo vehiculos.cvs se guardan de la siguiente manera: 
<class 'Vehiculo.Particular'>,"{'marca': 'Ford', 'modelo': 'Fiesta', 'nro_ruedas': '4', 'velocidad': '180', 'cilindraje': '500', 'nro_puestos': '5'}"
"""
# guardando cada instancia dentro del archivo
particular.guardar_datos_csv('vehiculos.csv')
carga.guardar_datos_csv('vehiculos.csv')
bicicleta.guardar_datos_csv('vehiculos.csv')
motocicleta.guardar_datos_csv('vehiculos.csv')
print(particular.recuperar_datos_csv('vehiculos.csv'))

print(str(type(particular)))

        









