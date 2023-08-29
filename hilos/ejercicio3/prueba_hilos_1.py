from variable_compartida import variableCompartida
from Concurrente2 import concu
from otro_lado import concurrente2

# Crear una instancia de la clase VariableCompartida
vc = variableCompartida()

# Crear instancias de la clase Concurrente y pasarles la instancia de VariableCompartida
c1 = concu(vc)
c2 = concurrente2(vc)

# Iniciar la ejecución de los hilos concurrentes
c1.start()
c2.start()
