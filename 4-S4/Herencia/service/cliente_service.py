from modelo.cliente import Cliente

class ClienteService:
    def crear_cliente(self):
       #(self, nombre, apellido, rut, descuento)
       nombre = input('Ingrese el nombre del cliente: ')
       apellido = input('Ingrese el apellido del cliente: ')
       rut = input('Ingrese el rut del cliente: ')
       descuento = input('Ingrese el descuento del cliente: ') 
       
       #instanciar un cliente
       cliente = Cliente(nombre, apellido, rut, descuento)
       print(f'Cliente creado: {cliente}')