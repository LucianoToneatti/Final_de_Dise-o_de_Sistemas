from handler import Handler

#
## BASE HANDLER
#

class BaseHandler(Handler):

    ###Clase base para manejar la sucesión en la cadena.###
    
    def __init__(self, sucesor=None):
        self._sucesor = sucesor

    def set_sucesor(self, sucesor):
        self._sucesor = sucesor

    def aprobar(self, monto):
        if self._sucesor:
            return self._sucesor.aprobar(monto)
        else:
            print("Nadie pudo aprobar el préstamo solicitado de " + str(monto))
            return False
