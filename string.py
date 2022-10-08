my_string = "My string"
my_other_string = "My other string"

print(len(my_string))
print(len(my_other_string))


print(my_string + " " + my_other_string)

my_new_line_string = "Es es un String\ncon un salto de linea"

print(my_new_line_string)


name = "Fak"
surname = "Becerra"
edad = 31

print("Mi nombre es {}, {} y mi edad es {}".format(name,surname,edad))
print("Mi nombre es %s, %s y mi edad es %d" %(name,surname,edad))
print("Mi nombre es" , name ,  surname , "y mi edad es" , edad , ".")
print(f"Mi nombre es {name} {surname} , y mi edad es {edad}.")


language = "python"
language2 = "python pepe"

a,b,c,d,e,f, = language

print(a)
print(b)

reverse_language = language[::-1]

print(reverse_language)

#funciones del sistema python

print("Capitalize ", language.capitalize())
print("Capitalize ",language2.capitalize())
print("Upper ",language.upper())
print("ISnumeric ",language.isnumeric())
print("1".isnumeric())
print("Count ",language.count("t"))
print(language.lower())
print(language.upper().isupper())
