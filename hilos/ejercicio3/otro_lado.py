from threading import Thread, Lock
from variable_compartida import variableCompartida
import time


class concurrente2(Thread):
    def __init__(self, vc):
        Thread.__init__(self)
        self.vc = vc

    def run(self):
        try:
            time.sleep(0.5)
            n = self.vc.get()
            print(n)
        except Exception as e:
            print(e)


# Crear una instancia de la clase VariableCompartida
vc = variableCompartida()

# Crear una instancia de la clase Concurrente y pasarle la instancia de VariableCompartida
concurrente = concurrente2(vc)

# Iniciar la ejecución del hilo concurrente
concurrente.start()
