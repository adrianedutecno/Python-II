class Vehiculo:
    #constructor con parametros para realizar una instancia de la clase Vehiculo
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 0
        self.encendido = False
        
    #getters and setters son funciones para obtener o dar valor a los atributos
    #getters
    def get_marca(self):
        return self.marca
    
    def get_color(self):
        return self.color
    
    def get_modelo(self):
        return self.modelo
    
    #setters
    def set_marca(self,marca):
        self.marca = marca
        
    def set_color(self,color):
        self.color = color
        
    def set_modelo(self,modelo):
        self.modelo = modelo
    
    #funciones que realiza el objeto accediendo a traves de la instancia    
    def arrancar(self):
        if self.encendido:
            return f"Vehiculo de marca {self.marca} ya se encuentra en encendido, no se puede volver a arrancar"
        else:
            self.encendido = True #se cambia a True para cambiar el estado del vehiculo
            self.velocidad = 10
            return f"Vehiculo de marca {self.marca} esta en encendido a una velocidad de {self.velocidad}"
                      
    def frenar(self):
        if self.encendido and self.velocidad > 0:
            self.velocidad -= 10
            return f"vehiculo de marca {self.marca} y {self.modelo} esta frenando"
        else:
            return f"Vehiculo de marca {self.marca} y {self.modelo} ya esta detenido"
        
    def girar_izquierda(self):
        if self.encendido:
            return f"Vehiculo de marca {self.marca} esta girando a la izquierda"
        else:
            return f"Vehiculo de marca {self.marca} debe estar encendido"
        
    def girar_derecha(self):
        if self.encendido:
            return f"Vehiculo de marca {self.marca} esta girando a la derecha"
        else:
            return f"Vehiculo de marca {self.marca} debe estar encendido" 
        
    def apagar(self):
        if self.encendido:
            self.encendido = False
            return f"Vehiculo de marca {self.marca} se ha apagado"
        else:
            return f"Vehiculo de marca {self.marca} ya esta apagado"
            
        
    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"Vehiculo de marca {self.marca} ha sido encendido"
        else:
            return f"Vehiculo de marca {self.marca} ya esta encendido"
    
    def acelerar(self):
        if self.encendido:
              self.velocidad += 10
              return f"Vehiculo de marca {self.marca} ha aumentado su velocidad en 10 y la velocidad actual es {self.velocidad}"
        else:
            return f"Vehiculo de marca {self.marca} no se puede acelerar ya que no se encuentra encendido"     
        
    def retroceder(self):
        if self.encendido:
            self.velocidad -= 10
            return f"Vehiculo de marca {self.marca} esta retrocediendo"
        else:
            return f"Vehiculo de marca {self.marca} no puede retroceder porque no esta encendido"
    
    
#instanciar vehiculos para realiazar las acciones mediante sus funciones o metodos
mazda = Vehiculo("Mazda","Blanco","M4",2000,2.5,2)
toyota = Vehiculo("Toyota","Negro","Yaris",1500,1.5,1)

#cambiar el comportamiento mediante las funciones, accediendo desde la instancia a las funciones
print(mazda.arrancar()) #Vehiculo de marca Mazda esta en encendido a una velocidad de 10
print(mazda.acelerar()) #Vehiculo de marca Mazda ha aumentado su velocidad en 10 y la velocidad actual es 20
print(mazda.encender()) #Vehiculo de marca Mazda ya esta encendido
print(mazda.apagar()) #Vehiculo de marca Mazda se ha apagado
print("---------------------")
print(toyota.encender()) #Vehiculo de marca Toyota ha sido encendido
print(toyota.encender()) #Vehiculo de marca Toyota ya esta encendido
print(toyota.arrancar()) #Vehiculo de marca Toyota ya se encuentra en encendido, no se puede volver a arrancar
print(toyota.acelerar()) #Vehiculo de marca Toyota ha aumentado su velocidad en 10 y la velocidad actual es 10
print(toyota.frenar()) #vehiculo de marca Toyota y Yaris esta frenando

#get obtener el valor del atributo a traves de notracion de puntos
print(mazda.color) #Blanco
print(mazda.get_color()) #Blanco

#setear (cambiar) valor del atributo a traves de notacion de puntos
mazda.color = "Azul" #se cambia el valor del atributo color a Azul
mazda.set_color("Rosado") #se cambia el valor del atributo
print(mazda.get_color()) #Rosado
print(mazda.color) #Rosado

#instancia.set() instancia.get()
toyota.set_modelo("Corolla")
print(toyota.get_modelo())


        
        

















#creando una instancia de la clase Vehiculo        
# vehiculo_uno = Vehiculo("Mazda","Blanco","M3",2000,2.5,2.0)
# vehiculo_dos = Vehiculo("BMW","Gris","M4",800,2,1.5)
# vehiculo_tres = Vehiculo() #instancia con el constructor sin parametros

# #accediendo a los atributos del objeto Vehiculo
# print(vehiculo_uno.marca)#mazda
# print(vehiculo_uno.color)
# print(vehiculo_uno.modelo)
# print(vehiculo_uno.peso)
# print(vehiculo_uno.ancho)
# print(vehiculo_uno.alto)

# #cambiar los valores de los atributos del objeto llamado vehiculo_uno
# vehiculo_uno.marca = "Toyota"
# vehiculo_uno.modelo = "Camry"
# vehiculo_uno.color = "Negro"
# vehiculo_uno.peso = 1000
# vehiculo_uno.ancho = 2.0
# vehiculo_uno.alto = 1.5

# #asignar valores al objeto Vehiculo llamado vehiculo_tres
# vehiculo_tres.marca = "VW"
# vehiculo_tres.color = "Rosado"
# vehiculo_tres.modelo = "Escarabajo"
# vehiculo_tres.peso = 600
# vehiculo_tres.ancho = 1.5
# vehiculo_tres.alto = 1.5

# #accediendo a los atributos
# print(vehiculo_uno.marca)#Toyota
# print(vehiculo_tres.color)#Rosado

