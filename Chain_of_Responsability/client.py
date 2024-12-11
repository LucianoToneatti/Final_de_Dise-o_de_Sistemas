from concrete_handlers import EjecutivoCuenta, Lider, Gerente, Director

#
# CLIENT
#

if __name__ == "__main__":
    
    director = Director()
    gerente = Gerente(director)
    lider = Lider(gerente)
    ejecutivo = EjecutivoCuenta(lider)

    
    cadena = ejecutivo

    # Ejemplo de uso
    monto = 1  # Monto del préstamo 
    cadena.aprobar(monto)
