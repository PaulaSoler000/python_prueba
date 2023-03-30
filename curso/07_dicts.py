# dicts

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Paula",
                 "Apellido": "Soler", "Edad": 35, 1: "Python"} # relacion clave-valor debemos definirlo

my_dict = {
    "Nombre": "Paula",
    "Apellido": "Soler",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print("--------------------------")

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])


print("Paula" in my_dict)
print("Apellido" in my_dict)

print("--------------------------")

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

print("--------------------------")

# Actualizacion

my_dict["Nombre"] = "Pino"
print(my_dict["Nombre"])

print("--------------------------")

# Eliminación

del my_dict["Calle"]
print(my_dict)

print("--------------------------")

# comprobación

print("Paula" in my_dict)
print("Apellido" in my_dict)

print("--------------------------")

# otras operaciones

print(my_dict.items()) # listado de cada uno de los items
print(my_dict.keys()) # solo nos retorna las claves
print(my_dict.values()) # solo nos retorna los valores

my_new_dict = dict.fromkeys(("Nombre", 1, "Pisa"))
print(my_new_dict)

my_list = ["Nombre", 1, "Pisa"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Soler") # pondrá el valor en todas las claves
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(list(my_new_dict)) # solo se obtendrán las claves
print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))


