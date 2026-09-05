""" Set Data Type"""

unique_numbers = {1,2,2,3,4,4,5}
print(unique_numbers)
print(type(unique_numbers))


# common set operations
fruits = {"apple", "banana"}
fruits.add("orange")
fruits.remove("banana")
fruits.discard("mango")

print(fruits)
print(type(fruits))


# union, intersection, difference
set_a = {1,2,3,4}
set_b = {3,4,5,6}

print(set_a | set_b) # union
print(set_a & set_b) # intersection(common)
print(set_a - set_b) # difference