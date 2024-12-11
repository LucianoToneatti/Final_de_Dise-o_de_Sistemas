from base_handler import BaseHandler

#
# CONCRETE HANDLERS
#

class EjecutivoCuenta(BaseHandler):
    def aprobar(self, monto):
        if monto <= 1000:
            print("El Ejecutivo de Cuenta aprueba el préstamo solicitado de " + str(monto))
            return True
        else:
            return super().aprobar(monto)

class Lider(BaseHandler):
    def aprobar(self, monto):
        if 1000 < monto <= 5000:
            print("El Líder aprueba el préstamo solicitado de " + str(monto))
            return True
        else:
            return super().aprobar(monto)

class Gerente(BaseHandler):
    def aprobar(self, monto):
        if 5000 < monto <= 10000:
            print("El Gerente aprueba el préstamo solicitado de " + str(monto))
            return True
        else:
            return super().aprobar(monto)

class Director(BaseHandler):
    def aprobar(self, monto):
        if 10000 < monto <= 30000:
            print("El Director aprueba el préstamo solicitado de " + str(monto))
            return True
        else:
            return super().aprobar(monto)
