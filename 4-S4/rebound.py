class Libro:
     
    def __init__(self, autor=None, titulo=None, publicado=None): 
        self._autor = autor 
        self._titulo = titulo 
        self._publicado = publicado 
        
    @property 
    def autor(self): 
        return self._autor 
    @autor.setter 
    def autor(self, autor): 
        self._autor = autor 
    
    @property 
    def titulo(self): 
        return self._titulo 
    
    @titulo.setter 
    def titulo(self, titulo): 
        self._titulo = titulo 
        
    @property 
    def publicado(self): 
        return self._publicado 
    
    @publicado.setter 
    def publicado(self, publicado): 
        self._publicado = publicado 
        
    def __str__(self) -> str: return f"autor: {self._autor}, titulo: {self._titulo}, publicado: {self._publicado}" 
    
libro_1 = Libro('Dan Brown','Infierno') 
libro_2 = Libro('Dan Brown', 'El Codigo Da Vinci', '2003') 
print(libro_1.__dict__) 
print(libro_1.__str__) 
libro_1.publicado = '1998' 
print(libro_1.__dict__) 
print('================================') 
print(libro_2.__dict__) 
print(libro_2.__str__) 
print('================================') 
print(libro_1)