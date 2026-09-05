""" Immutable Data Type """

"""
-int / float / complex (numeric Types)
-str (String )
-tuple
-bool (Boolean)
-frozenset
-bytes

"""
# immutable - int & bool
a = 3
first_location = id(a)
a = 2.90
second_location = id(a)

print(first_location)
print(second_location)


# tuple data type
x = (1,2,3)
y = (4,5,6)

print(id(x))
print(id(y))



# frozenset 
a = frozenset([1,2,3,4])
b = frozenset([1,2,3,4])

print(id(a))
print(id(b))