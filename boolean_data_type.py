""" Boolean Data Type """

# basic syntax
is_passed = True
is_logged_in = False
print(is_passed)
print(type(is_passed))


# comparison operators
x = 10
y = 5
print(x>y)
print(x==y)
print(x<=3)


#bool() function & Truthy / Falsy Values
print(bool(""))
print(bool(0))
print(bool(None))

print(bool("Nasim"))
print(bool(27))


#condition (If-Else) - boolean
is_admin = True

if is_admin:
    print("Welcome to Dashboard!")
else:
    print("Access Denied!")