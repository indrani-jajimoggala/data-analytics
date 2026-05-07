#Type Casting:
#1.Implicit (automatic):  It is automatically  done by python.
x = 5
y = 5.5
z = x+y   #int -> float
print("implict: ",z)

#2.Explicit(Manual):It is manually done using function like int(),float(),str().
x = 10
y = float(x)
z = x+y   
print("explicit: ",z)

#type casting:
#int():
x = 18
print(x)
y = float(x)
print(y)
y1 = str(x)
print(y1)

#y2 = set(x)
#print(y2) -> 'int' object is not iterable
#y3 = list(x)
#print(y3) -> 'int' object is not iterable
#we can say that we convert the int into float and string only.

#float(): 
x = 18.78
y = int(x)
print(x, type(x))
print(y, type(y))
y1 = str(x)
print(y1, type(y1))

#y2 = set(x)
#print(y2)
#print(type(y2))  -> 'float' object is not iterable.
#we can say that we convert the int into float and string only.'''

#string():
a = "hello"
print(a, type(a))
a1 = list(a)
print(a1, type(a1))
a2 = tuple(a)
print(a2, type(a2))
a3 = set(a)
print(a3, type(a3))

#a4 = int(a)
#print(a4, type(a4))   #ValueError: invalid literal for int() with base 10: 'hello'

#list():
print("LIST")
lst = [1,2,3]
print(lst, type(lst))
lst1 = str(lst)
print(a1, type(a1))
lst2 = tuple(a)
print(lst2, type(lst2))
lst3 = set(a)
print(lst3, type(lst3))
lst4 = int(a)
print(lst4, type(lst4))
