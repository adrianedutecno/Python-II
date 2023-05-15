class Animal:
    #constructor con parametros
    #self señala al mismo objeto
    def __init__(self,nombre,raza,edad,peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def comer(self):
        print(f"El animal {self.nombre} esta comiendo")
        
    def caminar(self):
        print(f"El animal de raza {self.raza} esta caminando")
        
    def dormir(self):
        print(f"El animal {self.nombre} esta durmiendo")
              
#Definir una instancia de tipo Animal para un objeto llamado perro
perro = Animal("Brando","San Bernardo",3,30)
#Definir una instancia de tipo Animal para un objeto llamado gato
gato = Animal("Roll","Persa",4,3)

#setear valores a los atributos
perro.nombre = "Bob"
#accediendo a los atributos con notacion de puntos
perro.edad

#accediendo a los metodos de la clase Animal mediante el nombre del objeto creado
perro.caminar()
perro.comer()
perro.dormir()
gato.dormir()
gato.comer()

#realizar 5 instancias de diferentes tipos de animales, modificar y asignar sus valores a los atributos



