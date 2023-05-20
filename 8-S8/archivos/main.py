from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService

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
                cliente_service.list_clientes()
            case "4":
                rut = input('Ingrese el rut del cliente a buscar: ')
                print(cliente_service.get_cliente_by_rut(rut))
            case "5":
                print("Saliendo del Programa")
                break
            case _:
                print("Opcion invalida")

# Funcion inicializadora para darle un punto de entrada/inicio al programa
if __name__ == "__main__":
    main()
    #instancia de cliente service para invocar al metodo load_clientes()
    # cliente_service = ClienteService()
    #accedemos a load_clientes() mediante la instancia de ClienteService
    # print(cliente_service.load_clientes())












# persona = Persona("Fulanito","Perez","1-9")
# print(persona)
# print(str(persona))
# persona.get_tipo()

# cliente = Cliente("Fulanita","Gonzales","1-8","0.1")
# print(cliente)
# print(str(cliente))
# cliente.get_tipo()