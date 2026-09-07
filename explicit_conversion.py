""" Conversion Types """

# explicit - type casting -int()
# float to int
price = 99.85
price_int = int(price)
print(price_int)
print(type(price_int))


# string to int
age_str = "25"
age = int(age_str)
print(age + 5 )
print(type(age))


# int to float
score = 100
score_float = float(score)
print(score_float)


# str to float
temp_str = "35.5"
temp = float (temp_str)
print(temp)


""" Collection Type Casting """

# list from set(remove duplicate value)
raw_numbers = [1,2,3,3,4,4,5]
unique_numbers = set(raw_numbers)
print(unique_numbers)


# tuple from list (change value)
point_tuple = (10,20)
temp_list = list(point_tuple)
temp_list[0] = 15
print(temp_list)
point_tuple = tuple(temp_list)
print(point_tuple)


# string from list (every word separation)
word = "Python"
char_list = list(word)
print(char_list)