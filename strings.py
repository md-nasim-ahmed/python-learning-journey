""" String - Immutable Data Type """

# Different methods of creating strings
single_quote = 'Hello'
double_quote = "Pyhton"

multiple_str = """Hello Nasim,
Welcome to Python Programming"""

print(type(double_quote))


# String Slicing & Indexing
text = "Python Developer"

# Indexing
print(text[0])
print(text[-1])

# Slicing
print(text[0:6])
print(text[7:])
print(text[::-1])


# String Formatting (f-strings) — Best Practice
name = "Nasim"
role = "Python Web Developer"
years = 3

profile = f"My name is {name}, I am a {role} with {years}+ years of experience."
print(profile)


# String Methods
msg = "  python programming is fun  "
print(msg.upper())
print(msg.title())

# Stripe
cleaned_msg = msg.strip()
print(cleaned_msg)

# Replace
print(cleaned_msg.replace ("fun", "awesome"))

# Split
words = cleaned_msg.split(" ")
print(words)

# Join 
joined_text = "_".join(words)
print(joined_text)

# Check find string start and end
print(cleaned_msg.startswith("python"))
print(cleaned_msg.find("programming"))

# String Concatenation
first_name = "Nasim"
last_name = "Ahmed"
full_name = first_name + " " + last_name
print(full_name)

