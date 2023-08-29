from variable_compartida import variableCompartida
from hilos.ejercicio2.Concurrente import Concurrente

# Crear una instancia de la clase VariableCompartida
vc = variableCompartida()

# Crear instancias de la clase Concurrente y pasarles la instancia de VariableCompartida
c1 = Concurrente(vc)
c2 = Concurrente(vc)

# Iniciar la ejecución de los hilos concurrentes
c1.start()
c2.start()
