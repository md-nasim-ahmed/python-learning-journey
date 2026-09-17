""" String Checking and Counting """

# Check if string starts with a substring
text = "Hello World"
print(text.startswith("Hello"))

# Check if string ends with a substring
print(text.endswith("World"))

# Find the position of a substring
print(text.find("World"))

# Count occurrences of a substring
print(text.count("o"))

# Check if all characters ar alphanumeric
print(text.isalnum())

# Check if all characters ar alphabetic
print(text.isalpha())

# Check if all characters are digits
print(text.isdigit())

# Check if the string contains only whitespace
print(text.isspace())

# Check if the string is title case
print(text.istitle())
