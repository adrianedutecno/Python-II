from modelo.supervisor import Supervisor #importando la clase supervisor

class SupervisorService:
    def crear_supervisor(self):
        nombre = input('Ingrese el nombre del supervisor: ')
        apellido = input('Ingrese el apellido del supervisor: ')
        rut = input('Ingrese el rut del supervisor: ')
        area = input('Ingrese el area del supervisor: ')
        
        #para crear un supervisor se realiza una instancia de su constructor
        supervisor = Supervisor(nombre, apellido, rut, area)
        print("Supervisor creado: ", supervisor)