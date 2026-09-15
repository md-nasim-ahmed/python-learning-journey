""" string join () """


# (" ")
words = ['Is', 'It', 'Case', 'Conversion?']
sentence = " ".join(words)
print(sentence)

# ("-")
words = ['Is', 'It', 'Case', 'Conversion?']
slug = "-".join(words)
print(slug)

# ("")
words = ['Is', 'It', 'Case', 'Conversion?']
combined = "".join(words)
print(combined)


# Using Split and Join (Round Trip)
text = "python-is-awesome"
words_list = text.split("-")
print("Tuple:", words_list )


# TypeError and Fix It
numbers = [1,2,3,4]
"""result = "-".join(numbers) # Error """
result = "-".join([str(num) for num in numbers])
print(result)


