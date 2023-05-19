from trabajador import Trabajador
from persona import Persona
from departamento import Departamento

if __name__ == '__main__':
      trabajador = Trabajador('Juan', 'Perez', 2005, 'Ingenieria de Software', 'IS')
      print(trabajador)
      trabajador.salario = 20_000
      print(trabajador.__dict__)
      #es trabajador una instancia de tipo Persona
      print('es trabajador una instancia de Persona?: ', isinstance(trabajador, Persona))
      print('es trabajador una instancia de Departamento?: ', isinstance(trabajador, Departamento))
      print('es trabajador una instancia de Trabajador?: ', isinstance(trabajador, Trabajador))