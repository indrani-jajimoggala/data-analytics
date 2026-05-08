#OPERATORS:
Operators are symbols useed to perform operations in values or variables.
Operator=action(add,compare,...)
Operands=values(x,y,numbers)

# 1. Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print(a + b)   # Addition -> 13
print(a - b)   # Subtraction -> 7
print(a * b)   # Multiplication -> 30
print(a / b)   # Division -> 3.33
print(a % b)   # Modulus -> 1
print(a ** b)  # Exponent -> 1000
print(a // b)  # Floor Division -> 3


# 2. Comparison Operators
print("\nComparison Operators:")
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False


# 3. Logical Operators
print("\nLogical Operators:")
x = 5
print(x > 2 and x < 10)  # True
print(x > 10 or x < 10)  # True
print(not(x > 2))        # False


# 4. Assignment Operators
print("\nAssignment Operators:")
x = 5
x += 2
print(x)  # 7

x -= 1
print(x)  # 6

x *= 2
print(x)  # 12

x /= 3
print(x)  # 4.0


# 5. Bitwise Operators
print("\nBitwise Operators:")
a = 5   # 101
b = 3   # 011

print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6
print(~a)     # -6
print(a << 1) # 10
print(a >> 1) # 2


# 6. Membership Operators
print("\nMembership Operators:")
list1 = [1, 2, 3]

print(2 in list1)      # True
print(5 not in list1)  # True


# 7. Identity Operators
print("\nIdentity Operators:")
c = [1, 2]
d = c
e = [1, 2]

print(c is d)      # True
print(c is e)      # False
print(c is not e)  # True
