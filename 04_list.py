my_list = list()
my_other_list = []

name = "Perro"
print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]


print(len(my_list))
print(my_list)

my_other_list = [35, 1.77, "Fak", "Pepito", name]

print(my_other_list)
print(type(my_other_list))

print(my_list[6])
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(24))


my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)


my_other_list[1] = "Rojo"
print(my_other_list)
print("---------------------------------------------------")
my_other_list.remove("Rojo")
print(my_other_list)
my_list.remove(30)
print(my_list)

my_new_list = my_list.copy()

print(my_list.pop())
print(my_list)
my_pop = my_list.pop(2)
print(my_pop)
print(my_list)

del my_list[2]
print(my_list)


my_list.clear()
print(my_list)
print(my_new_list)
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])
"""
age, height, surname, name2, ojo = my_other_list

print(ojo)

my_list = "Hola perrito"

print(my_list)
"""
