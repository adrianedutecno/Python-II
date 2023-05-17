class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    def metodo_a(self):
        print("Método heredado de A")
        
class B:
    def __init__(self):
        print("Clase B")
    def metodo_b(self):
        print("Método heredado de B")
        
class C(B,A):
    def metodo_c(self):
        print("Método de clase C")
    
    #sobreescritura de metodo 
    # def metodo_a(self):
    #     print("Método sobreescrito A")
        
#str, int, float, bool, list(), tuple(), set(), dict(), Object()

#instancia
c = C() #invocando al constructor, necesario para crear objetos
c.metodo_a()
c.metodo_b()
c.metodo_c()

#acceso estatico o a traves del nombre de la clase
C.metodo_a(C)