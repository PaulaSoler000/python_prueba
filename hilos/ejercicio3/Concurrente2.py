from threading import Thread, Lock
from variable_compartida import variableCompartida
import time


class concu(Thread):
    def __init__(self, vc):
        Thread.__init__(self)
        self.vc = vc

    def run(self):
        try:
            n = 0
            time.sleep(0.5)
            for i in range(99):
                self.vc.set(i)
        except Exception as e:
            print(e)


# Crear una instancia de la clase VariableCompartida
vc = variableCompartida()

# Crear una instancia de la clase Concurrente y pasarle la instancia de VariableCompartida
concurrente = concu(vc)

# Iniciar la ejecución del hilo concurrente
concurrente.start()
