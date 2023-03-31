# classes

# ejemplo: la clase persona tiene como funcion dormir pero no volar

class MyEmptyPerson:  # los nombres de las clases se escriben en camelcase, sin espacios
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

print("-----------------------")


# Clase con constructor, funciones y propiedades privadas y públicas

class Person:
    def __init__(self, name, surname, ):  # es requerido siempre llamar a self
        self.name = name
        self.surname = surname


my_person = Person("Paula", "Soler")
print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self):  # es requerido siempre llamar a self
        self.name = "Paula"
        self.surname = "Pino"


my_person = Person()
print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self, name, surname, alias="Sin alias"):  # es requerido siempre llamar a self
        self.full_name = f"{name} {surname} {alias}" #propiedad púlica
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name # accedes al nombre, pero no se puede modificar
    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Laura", "Soler")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Laura", "Soler", "Pino")
print(my_other_person.full_name)

my_other_person.walk()

my_other_person.full_name = "Celia"
print(my_other_person.full_name)
