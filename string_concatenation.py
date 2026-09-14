""" String Concatenation """

first_name = "Nasim"
last_name = "Ahmed"
full_name = first_name + " " + last_name
print(full_name)


name = "Nasim Ahmed"
age = 27
message = name + " is " + str(age) + " years old."
print(message)


# Using F-String
name = "Nasim"
role = "Developer"
experience = 5

profile = f"my name is {name}. i am a {role} with {experience} years experience"
print(profile)


# Join() Method
words = ["Python", "String", "Concatenation"]
sentence = " ". join(words) # Concatenation with space
print (sentence)

slug = "-".join(words) # Concatenation with slug
print(slug)