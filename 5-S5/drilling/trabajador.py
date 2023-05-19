from persona import Persona
from departamento import Departamento

class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, annio, nombre_depto, nombre_corto_dpto) -> None:
        Persona.__init__(self, nombre, apellido, annio)
        Departamento.__init__(self, nombre_depto, nombre_corto_dpto)
        self._salario = 0
        
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
        