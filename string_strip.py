""" String Strip """

# strip()
text = " Hello Python! "
clean_text = text.strip()
print(f"'{clean_text}'")


# lstrip() (Left Strip) / rstrip() (Right Strip)
text = "---Hello Python!---"
print(text.lstrip("-"))
print(text.rstrip("-"))
print(text.strip("-"))


# User Input Cleaning
email = input("Enter email: ").strip().lower()