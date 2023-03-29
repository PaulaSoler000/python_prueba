# tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Paula", "Soler", "Paula")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print("----------------")

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Paula"))  # cuenta cantos hay
print(my_tuple.index("Soler"))  # dice en qué posición está
print(my_tuple.index("Paula"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment, son valores inmutables

print("----------------")

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print("----------------")

# Subtuplas

print(my_sum_tuple[3:6])

print("----------------")

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Pino"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined