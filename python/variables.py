'''
A variable is a name that refers to an object stored in memory. 
When we assign a value, python first creates an object in memory, and then the variable points to that object.
Rules:
A variable name must start with a letter(A-Z,a-z) or the underscore character(_).
A variable name cannot start with a number.
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
2myvar = "John' ---> declaring wrong variable_name
'''

x = 10   #x is reference or pointing to the object(10).
print(x)

x = 20   #object is created
y = x    #y is reference to the same object
print(x)   #20
print(y)   #20. Both variables are reference to the same object

y = 30   #new object is created. so y is refernce to 30
print(y)   #30

a = "hello"
b = a
b = "world"
print(a)
print(b)

'''
integers, string are immutable.
new value -> new object
'''

a = [1,2]
b = a         #same object
b.append(3)   #same object is modified
print(a)

# lists are mutable
# same object is modified

# Reassignment vs Modification
x = 10
x = 20
print(x) #reassignment: leaving the old object and pointing to new object

a = [1,2]
a.append(3)   #modification: modified the existed list or same object, without creating new object.
print(a)

x = [1,2]
y = x.copy()   #copy(): creates a new object.
y.append(3)
print(a)    #[1,2]

a = 3
b = c = d = 4   #assigning a one value to the multiple variables
print(a)
print(b)
print(c)
print(d)

#swapping two variables
a = 5
b = 10
a,b = b,a
print(a,b)   #10,5
b,a = a,b
print(a,b)   #5,10
