""" Conversion Types """

# implicit type conversion - int + float = float
num_int = 15
num_float = 4.5

result = num_int + num_float

print(result)
print(type(result))


# implicit type conversion - int + complex = complex
num_int = 7
num_complex = 2 + 3j

result = num_int + num_complex

print(result)
print(type(result))


# implicit type conversion - boolean + int = int
is_active = True
count = 5

total = count + is_active

print(total)
print(type(total))


# limitation 
num = 10
text = "20"

total = num + text
print(total) # TypeError: unsupported operand type(s) for +: 'int' and 'str'