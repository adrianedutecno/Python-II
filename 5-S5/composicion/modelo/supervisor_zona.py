class SupervisorZona():
    def __init__(self, Supervisor, Capacidades):
        self._supervisor = Supervisor
        self._capacidades = Capacidades
        
    @property    
    def supervisor(self):
        return self._supervisor
    
    @supervisor.setter
    def supervisor(self, supervisor):
        self._supervisor = supervisor
        
    @property
    def capacidades(self):
        return self._capacidades
        
    @capacidades.setter
    def capacidades(self, capacidades):
        self._capacidades = capacidades
        
        