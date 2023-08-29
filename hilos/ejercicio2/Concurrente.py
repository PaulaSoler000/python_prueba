from threading import Thread
from variable_compartida import variableCompartida
import time


class Concurrente(Thread):
    def __init__(self, vc):
        Thread.__init__(self)
        self.vc = vc

    def run(self):
        try:
            time.sleep(0.5)
            for i in range(11):
                self.vc.inc()
                print(self.vc.get())
        except Exception as e:
            print(e)


# Crear una instancia de la clase VariableCompartida
vc = variableCompartida()

# Crear una instancia de la clase Concurrente y pasarle la instancia de VariableCompartida
concurrente = Concurrente(vc)

# Iniciar la ejecución del hilo concurrente
concurrente.start()
