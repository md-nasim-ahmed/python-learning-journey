""" Mutable Data Types"""

"""
- list
- dict (dictionary/mapping)
- set
- bytearray

"""

# list data types
numbers = [10,20,30]
print(id(numbers))

numbers[0] = 90
numbers.append(40)

print(id(numbers))


# mapping/dictionary
user = {"name": "Name",
        "age": 25
        }
user_id = id (user)
print(user_id)

user ["role"] = "Developer"
user ["age"] = 27

print(user_id)


# mutable data types - copy behavior warning
list_a = [1,2,3]
list_b = list_a.copy() #.copy()-method

list_b.append(100)

print (list_a)
print (list_b)