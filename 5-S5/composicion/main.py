from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService
from modelo.supervisor_zona import SupervisorZona
from modelo.supervisor import Supervisor
from modelo.capacidades import Capacidades

def main():
    #Creando instancias para acceder
    menu_service = MenuService()
    supervisor_service = SupervisorService()
    cliente_service = ClienteService()
    
    while True:
        menu_service.imprimir_menu() #Imprimiendo menu
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                cliente_service.crear_cliente()
            case "2":
                supervisor_service.crear_supervisor()
            case "3":
                print("Saliendo del Programa")
                break
            case _:
                print("Opcion invalida")

# Funcion inicializadora para darle un punto de entrada/inicio al programa
if __name__ == "__main__":
    #main()
    supervisor = Supervisor('Jose','Feliciano','1-9','agricola')
    capacidades = Capacidades('5','6')
    supervisor_zona = SupervisorZona(supervisor,capacidades)
    print(supervisor_zona.supervisor.area)
    print(supervisor_zona.capacidades.ncertificados)
    
    capacidades_2 = Capacidades('8','5')
    supervisor_zona.capacidades = capacidades_2
    print(supervisor_zona.capacidades.ncertificados)
    
    
    # crear 3 supervisores de zona
    # cada supervisor de zona debe llevar su supervisor y capacidades
    












# persona = Persona("Fulanito","Perez","1-9")
# print(persona)
# print(str(persona))
# persona.get_tipo()

# cliente = Cliente("Fulanita","Gonzales","1-8","0.1")
# print(cliente)
# print(str(cliente))
# cliente.get_tipo()