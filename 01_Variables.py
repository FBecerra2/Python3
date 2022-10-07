from re import A


my_variable = "My string variable."

print(my_variable)

my_int_variable = 5

print(my_int_variable)

my_bool_varible = True

print(my_bool_varible)

print(my_bool_varible, my_int_variable,  my_variable)

print("Este es el valor de:", my_bool_varible)

print(len(my_variable))


# Variables en una sola linea

name, surname, alias, age = "Fak", "El perro", "Loco", 2

print(name, surname, age, "Este es el Alias", alias)

name = input("What is your name?:  ")
age = input("How old are you?: ")
print("Mi nombre es ", name)
print("Mi edad es ", age)
