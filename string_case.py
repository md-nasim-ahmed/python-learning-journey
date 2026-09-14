""" String Case Conversion """

# Upper()
text = "python developer"
print(text.upper())


# lower()
text = "PYTHON DEVELOPER"
print(text.lower())


# title()
text = "welcome to python programming"
print(text.title())


# capitalize()
text = "hello world"
print(text.capitalize())


# swapcase()
text = "nASIM"
print(text.swapcase())


# casefold()
text = "ß"
print(text.lower())
print(text.casefold())



# Case Insensitive Input Check
user_input = input("Do you want to continue? (yes/no): ").strip().upper()

if user_input == "YES":
    print("Continuing the process...")
else: 
    print("Process stopped")


user_input = input("Are you developer? (yes/no): ").strip().lower()

if user_input == "yes":
    print("Python Developer")
else:
    print("No")