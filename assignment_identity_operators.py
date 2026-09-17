"""Assignment Identity Operators"""

"""
=	Simple Assignment	        x = 10 	   x = 10
+=	Add and Assign	            x += 5	   x = x + 5
-=	Subtract and Assign	        x -= 3     x = x - 3
*=	Multiply and Assign	        x *= 2     x = x * 2
/=	Divide and Assign	        x /= 4	   x = x / 4
//=	Floor Divide and Assign	    x //= 2	   x = x // 2
%=	Modulus and Assign	        x %= 3	   x = x % 3
**= Exponent and Assign         x**= 2     x = x ** 2

"""

score = 10
score += 5
print(score)

score *=2
print(score)


# Identity Operators
list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

#Value Check (==)
print(list1 == list2)

# Identity Check (is)
print(list1 is list2)
print(list1 is list3)

# Memory Id
print(id(list1))
print(id(list2))