from abc import ABC, abstractmethod

#
# HANDLER
#

class Handler(ABC):
    ###Interfaz para todos los manejadores de la cadena.###
    
    @abstractmethod
    def set_sucesor(self, sucesor):
        pass

    @abstractmethod
    def aprobar(self, monto):
        pass
