class Persona:#constructor con parametros
    def __init__(self, nombre, apellido, annio) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._annio = annio
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def annio(self):
        return self._annio
    
    @annio.setter
    def annio(self, annio):
        self._annio = annio
        
    