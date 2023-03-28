# listas

my_list = list()
my_other_list = []  # los dos son listas

print(len(my_list))
print("-------------------")

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

print("-------------------")

my_other_list = [35, 1.77, "Paula", "Soler"]

print(my_other_list)
print(len(my_other_list))

print("-------------------")

print(type(my_list))
print(type(my_other_list))

print("-------------------")

# acceso a elementos y búsqueda
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))  # retorna el numero de veces que esta repetio el mismo valor
print(my_other_list.count("Paula"))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print("-------------------")

age, height, address, surmane = my_other_list  # necesita todos los elementos de la lista hecha

print(address)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]  # no es aconsejable
print(age)

print("-------------------")

# Concatenación
print(my_list + my_other_list)

print("-------------------")

# creación, inserción, actualización y eliminación
my_other_list.append("Hola")
print(my_other_list)

my_other_list.insert(1, "Verde")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)  # solo elimina uno
print(my_list)  # utilizamos remove en vez de del cuando sabemos cual es el elemento

print(my_list.pop())  # elimina el ultimo
print(my_list)

print(my_list.pop(2))  # elimina el elemnto que este en esa posicion
print(my_list)

my_pop_element = my_list.pop(2)  # guardarlo en una variable
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

print("-------------------")

# Operaciones con listas
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()  # esta ordenano de menor a mayor or defecto
print(my_new_list)

print("-------------------")

# Sublistas

print(my_new_list[1:3])
