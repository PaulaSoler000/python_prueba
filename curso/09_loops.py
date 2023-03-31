# loops

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

print("-------------------------")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución, mi ejecución es 15")
        break  # detiene el bucle
    print(my_condition)

print("La ejecución continúa")

print("-------------------------")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print("-------------------------")

my_tuple = (35, 1.77, "Paula", "Soler", "Pino")

for element in my_tuple:
    print(element)

print("-------------------------")

my_set = {"Paula", "Soler", 35}

for element in my_set:
    print(element)

print("-------------------------")

my_dict = {"Nombre": "Paula", "Apellido": "Soler", "Edad": 35, 1: "Python"}
# imprime solo los valores, no las claves
for element in my_dict:
    print(element)

    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

print("-------------------------")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
