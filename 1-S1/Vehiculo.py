class Vehiculo:
    #constructor con parametros para realizar una instancia de la clase Vehiculo
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
    
    #constructor sin parametros de entrada para instanciar un objeto Vehiculo
    def __init__(self,marca=None,color=None,modelo=None,peso=None,ancho=None,alto=None):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto    

#creando una instancia de la clase Vehiculo        
vehiculo_uno = Vehiculo("Mazda","Blanco","M3",2000,2.5,2.0)
vehiculo_dos = Vehiculo("BMW","Gris","M4",800,2,1.5)
vehiculo_tres = Vehiculo() #instancia con el constructor sin parametros

#accediendo a los atributos del objeto Vehiculo
print(vehiculo_uno.marca)#mazda
print(vehiculo_uno.color)
print(vehiculo_uno.modelo)
print(vehiculo_uno.peso)
print(vehiculo_uno.ancho)
print(vehiculo_uno.alto)

#cambiar los valores de los atributos del objeto llamado vehiculo_uno
vehiculo_uno.marca = "Toyota"
vehiculo_uno.modelo = "Camry"
vehiculo_uno.color = "Negro"
vehiculo_uno.peso = 1000
vehiculo_uno.ancho = 2.0
vehiculo_uno.alto = 1.5

#asignar valores al objeto Vehiculo llamado vehiculo_tres
vehiculo_tres.marca = "VW"
vehiculo_tres.color = "Rosado"
vehiculo_tres.modelo = "Escarabajo"
vehiculo_tres.peso = 600
vehiculo_tres.ancho = 1.5
vehiculo_tres.alto = 1.5

#accediendo a los atributos
print(vehiculo_uno.marca)#Toyota
print(vehiculo_tres.color)#Rosado

