""" Frozenset Data Type """

# frozenset - immutable
numbers = [1,2,3,3,4]
frozen_numbers = frozenset (numbers)
print(frozen_numbers)
print(type(frozen_numbers))


# union, intersection, difference
a = frozenset([1,2,3])
b = frozenset([3,4,5])

print (a | b)
print (a & b)
print ( a - b)


# dictionary key - frozenset
student_groups = {

    frozenset (["Nasim", "Bulbul"]): "Group Alpha"
}
group_members = frozenset (["Nasim", "Bulbul"])
print(student_groups[group_members])