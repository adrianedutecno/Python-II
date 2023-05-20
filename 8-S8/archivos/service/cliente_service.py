from modelo.cliente import Cliente

class ClienteService:
    #constructor
    def __init__(self):
        #ClienteService tiene una lista de clientes como atributos para que la lista persista en la ejecución
        self._clientes = self.load_clientes() #se carga la lista de clientes cuando se instancia ClienteService
    
    #carga de archivo, lectura y creacion si el archivo no existe
    def load_clientes(self):
        try:
            with open('clientes.txt','r') as file:#apertura y cierra el archivo, se puede establecer el tipo de apertura, r es para leer
                clientes = file.readlines() #retorna una lista de tipo str con todas las lineas existentes
        except FileNotFoundError: #si ocurre el error de archivo no existe, se procede a crearlo
            clientes = []
            with open('clientes.txt','w') as file:
                file.writelines(clientes) #crear el archivo si no existe, w es para escribir
        return clientes
    
    #guardado de archivo, escritura sobre el archivo de la lista de clientes
    def save_clientes(self):
        with open('clientes.txt','w') as file:
            for cliente in self._clientes: #se recorre la lista existente de clientes
                file.write(str(cliente)) #se va escribiendo en el archivo cliente a cliente
            
    #metodo para crear clientes
    def crear_cliente(self):
       #(self, nombre, apellido, rut, descuento)
       nombre = input('Ingrese el nombre del cliente: ')
       apellido = input('Ingrese el apellido del cliente: ')
       rut = input('Ingrese el rut del cliente: ')
       descuento = input('Ingrese el descuento del cliente: ') 
       
       #instanciar un cliente
       cliente = Cliente(nombre, apellido, rut, descuento)
       print(f'Cliente creado: {cliente}')
       
       #agregar el cliente a la lista existente en ClienteService
       self._clientes.append(cliente)
       
       #guardar los clientes
       self.save_clientes()
    
    #metodo para listar los clientes en la lista existente en ClienteService   
    def list_clientes(self):
        print('Lista de clientes: ')
        for cliente in self._clientes:
            print(cliente)