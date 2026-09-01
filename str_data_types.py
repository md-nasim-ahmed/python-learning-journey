""" String Data Types - Start"""
name = "Md. Nasim Ahmed"
print(name)
print(type(name))

#Modify Strings
name = "Md. Nasim Ahmed"
print (name.upper())

name = "Md. Nasim Ahmed"
print (name.lower())

name = "Md. Bulbul Islam"
print (name.replace("Bulbul Islam", "Nasim Ahmed")) 

name = "Md. Nasim Ahmed"
print (name.split("."))

#String Concatenation
x = "Hello"
y = "World"
z =  x + y
print(z)

a = "Hello"
b = "world"
c = a + " "+ b
print(c)

"""Format Strings"""
#Basic Syntax
name = "Nasim"
age = 27
txt = f"My name is {name} and I am {age} years old."
print (txt)

#Math & Expressions
a = 10
b = 5
print (f"Total: {a + b}")

""" String Data Types - End"""