class Accesadores:
    def __init__(self):
        self.atributo_publico = "Puede ser accedido en toda la estructura"
        self._atributo_protected = "Puede ser accedido desde las sub clases"
        self.__atributo_privado = "Puede ser accedida desde la propia clase"

    def get_variable_privada(self):
        return self.__atributo_privado

    def set_variable_privada(self, __atributo_privado):
        self.__atributo_privado = __atributo_privado


objeto = Accesadores()
print(objeto._Accesadores__atributo_privado) #mangles name para acceder a un atributo con dos __ under slashes

print(objeto.get_variable_privada())
print(objeto._atributo_protected)
print("===============================")
# seteamos un nuevo valor para nuestro atributo privado
objeto.set_variable_privada("pan con palta")
print(objeto.get_variable_privada())
