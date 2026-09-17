""" Python Comparison Operators """

"""
== Equal to
!= Not Equal to
> Greater than
< Less than
> = Greater than or equal to
< = Less than or equal to

"""

a = 15
b = 20

# Equality check
print("a == b:", a==b)
print("a != b:", a!=b)

# Greater / Less than
print("a > b:", a > b)
print("a < b:", a < b)

# Greater/Less than or Equal
print("a >= 15:", a >= 15)
print("b <= 10:", b <= 10)


""" Multiple Comparison (Chained Comparison) """
age = 25
is_valid = 18 <= age <= 30
print(is_valid)