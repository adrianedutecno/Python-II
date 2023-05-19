class Departamento:
    def __init__(self, nombre_depto, nombre_corto_dpto) -> None:
        self._nombre_depto = nombre_depto
        self._nombre_corto_dpto = nombre_corto_dpto
        
    @property
    def nombre_depto(self):
        return self._nombre_depto
    
    @nombre_depto.setter
    def nombre_depto(self, nombre_depto):
        self._nombre_depto = nombre_depto
        
    @property
    def nombre_corto_dpto(self):
        return self._nombre_corto_dpto
    
    @nombre_corto_dpto.setter
    def nombre_corto_dpto(self, value):
        self._nombre_corto_dpto = value
        