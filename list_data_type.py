""" Sequence Data Types """

# list data type
number = [10,20,30,40]
fruits = ["apple", "banana","cherry"]
mixed_list = ["Nasim", 27, True, 5.8]
print(fruits)


# common list operations
fruits = ["apple", "banana","cherry"]
print(fruits[0])
print(fruits[-1])


# adding items
fruits = ["apple", "banana","cherry"]
fruits.append("orange")
fruits.insert(1,'mango')
print(fruits)


# removing items
fruits = ["apple", "banana","orange","cherry"]
fruits.remove("banana")
fruits.pop()
print(fruits)


# modifying items
fruits = ["apple", "banana","orange","cherry"]
fruits[1] = "strawberry"
print(fruits)
