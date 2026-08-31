# Built-in Data Types
 
"""
Text Type: str
Numeric Types: int, float, complex
Sequence Type: list, tuple, range
Mapping Type: dist
Ste Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType

"""

#str
a = "Python Developer"
print (type(a))

#int
b = 10
print (type(b))


#float
c = 10.1
print(type(c))

#complex
d = 5j
print (type(d))

#list
x = ["Bangladesh", "India", "China"]
print(type(x))

#tuple
y = ("USA", "UK","CA")
print(type(y))

#range
z = range(10)
print(list(z))

#dict
a = dict(
    name ="Nasim",
    age = 27
)
print(type(a))

#set
b = set (("apple", "banana", "cherry"))
print(type(b))

#frozenset
c = frozenset(("Dhaka","Khulna","Chittagong"))
print(type(c))

#bool
x = bool(10)
print(type(x))

#bytes
y = bytes(15)
print(type(y))

#bytearray
z = bytearray(20)
print(type(z))

#memoryview
x = memoryview(bytes(1))
print(type(x))



"""Numeric Data Types"""
age = 27 #int data types
print (age)

marks = 80.5 #float data types
print (marks)

complex_number = 10 + 20j #complex data types
print (complex_number)