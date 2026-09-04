""" Mapping Data Types"""


# basic syntax
user_profile = {
    "name":"Nasim",
    "age": 25,
    "role": "Developer",
    "skills": ["python", "javascript"]
}
print(user_profile)
print (type(user_profile))


# common dictionary operations
user_profile = {
    "name":"Nasim",
    "age": 25,
    "role": "Developer",
    "skills": ["python", "javascript"]
}
print(user_profile["name"])
print(user_profile["age"])


# key-value add or update
user_profile = {
    "name":"Nasim",
    "age": 25,
    "role": "Developer",
    "skills": ["python", "javascript"]
}
print(user_profile)

user_profile["location"] = "Narail"
user_profile["experience_years"] = 4
print (user_profile)

# update value
user_profile.update({
    "age": 27,
    "location": "Dhaka",
})

print(user_profile)

# show key or value
print(user_profile.keys())
print(user_profile.values())
print(user_profile.items())