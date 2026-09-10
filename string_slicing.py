""" String Slicing - Start, Stop and Step"""

"""
use case:
-Extracting Substring
-Reversing String
-Manipulating 
-parsing Data
-Validation and Formatting
-Analyzing data

"""

""" Positive String """

# General String ( Start and Stop)
text = "Python Developer"
print(text[0:3])
print(text[2:9])


# Default Parameters ( Start and Stop)
text_one = "Programming"
print(text_one[:4])
print(text_one[:6])
print(text_one[:])
print(text_one[::2])


# Step string Slicing
text_two = "Developer"
print(text_two[0:9:2])
print(text_two[1::3])
print(text_two[4:])


""" Negative String"""

text_three = "Python"
print(text_three[::-1])
print(text_three[::-2])
print(text_three[-5:-2])
