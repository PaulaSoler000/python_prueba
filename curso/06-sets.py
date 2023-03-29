# sets

my_set = set()
my_other_set = {}  # el diccionario y el set se declaran igual

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Paula", "Soler", 35}
print(type(my_other_set))

print(len(my_other_set))

print("-------------------")

# Inserción

my_other_set.add("Pino")
print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("Pino")  # Un set no admite repetidos
print(my_other_set)

print("-------------------")

# Búsqueda

print("Pino" in my_other_set)
print("Pine" in my_other_set)

print("-------------------")

# Eliminación

my_other_set.remove("Pino")
print(my_other_set)

my_other_set.clear()  # clrear solo limpia, el elemento sigue ahi mientras que el del elimina por completo
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

print("-------------------")

# Transformación

my_set = {"Paula", "Soler", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

print("-------------------")

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))  # no se muestras javascript ni c# porque no está almacenado
