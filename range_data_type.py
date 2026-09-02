""" Sequence Data Types """

# range data type - immutable
"""Syntax of range()
The range() function can be written in three ways: range(start, stop, step)
1) range(stop) — Starts from 0 and runs up to stop - 1.
2) range(start, stop) — Starts from start and runs up to stop - 1.
3) range(start, stop, step) — Specifies the increment or decrement value (step) between each number."""

# starts from 0 and goes up to 4 (up to, but not including 5)
numbers = range(5)
print(list(numbers))

numbers = range(10)
print(*numbers)


# range(start, stop, step)
nums = range(2,10)
print (tuple(nums))


# odd numbers from 1 to 10 (with a step of 2)
odd_numbers = range (1,10,2)
print(list(odd_numbers))


# decrease from 10 down to 1 or counting down from 10 to 1
reverse_nums = range(10,0,-1)
print (list(reverse_nums))


# using range() in loops
for i in range(5):
 print(f"Iteration number: {i}")


