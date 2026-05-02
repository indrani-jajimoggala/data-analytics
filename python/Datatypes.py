'''
Data types:
Data types specify what kind of value a variable refers to.
Python is  dynamically typed, so we don't need a declare the datatype explicity.
It is automatically determined based on the value.
Mutable object can be modified after creation, such as lists, sets and dictionaries.
Immutable object cannot modifies after creation such as int, float, str, tuple.
type() function is used to find the dat type of a variable.
'''

x = 10
print(type(x))
y = 15.5
print(type(y))
z = "hello"
print(type(z))
is_valid = "True"
print(type(is_valid))
a = [1,2,3,4]   #ordered, mutable
print(type(a))
b = (1,2,3,4)   #ordered, immutable
print(type(b))
c = 1,2,3,4
print(type(c))
d = {"name":"indu","age":18}   #key-value pairs
print(type(d))
s = {1,2,3,4}   #unordered, unique values
print(type(s))

'''
str, int, float, tuple -> new object created
list, set, dict -> same object will be modified
'''

#immutable:
name = "hello"
name = name+" "+"whats'up"
print(name)

#mutable:
#case1():
a = [1,2]
a.append(3)   #same object modified
print("case1: ",a)

#case2():
a = [1,2]
a = a+[3]   #new list created, a is pointing to the new object
print("case2: ",a)
