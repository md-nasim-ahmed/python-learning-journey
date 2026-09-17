"""Logical Operators"""

# and operator
age = 25
has_license = True

can_drive = (age>= 18) and (has_license == True)
print(can_drive)


# or Operator
is_admin = False
has_permission = True

can_access = is_admin or has_permission
print(can_access)


# not Operator
is_logged_in = False

if not is_logged_in:
    print("Please log in to continue.")