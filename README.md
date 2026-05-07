Python is high level programming language, interpreted, dynamically typed language, gerenal-purpose programming language.

High level : We can write the code easily.

Interpreted : Line-by-line code executation. Case - sensetive.
print("Hello")
print(10/0) #error. Execution stops here. 
print("World") 

Object-oriented : It treats the everything as an object. Object = data(properties) + actions or Behavior (methods).
x = 10 --> 10 is an object. because 10 is a value and we can do actions like (+,-,*,/ - arthimetic operations).
Car is an object. car have color, brand, design comes under data and actions are (start the car,stop the car).

Dynamic : Before creating a variable. no need mention the datatype before the variable.
x = 10 # int
x = "hello" # string
same variable holds different types.

OOP's :
Class, Object, Inheritance, Polymorphism, Encapsulation

General Purpose Language : Using the python we can do different types of works or projects.
Web development, Data analysis, Machine learning, Automation, AI

How it works?
- We write Python code is called source code(.py)
- Python converts source code -> byte code
- Bytecode is stored in -> .pyc file
- Byte is given to PVM
- PVM converts it into -> machine code(binary)
CPU executes -> gives output

If Python is interpreted, then why does it convert code into bytecode first?
Python is a high-level programming language. Computers understand only binary. 
So Python converts the code into bytecode, which is an intermediate form. 
This bytecode is executed by the Python Virtual Machine (PVM), which converts it into machine code and gives output.

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

Type Casting:
It is converting one data type into another data type.
It is used when we need to perform operations between different data type.
(or) when we want to change  the format of data.
Types of Type Casting: 1.Implicit 2. Explicit

1.Implicit (automatic):  It is automatically  done by python.
2.Explicit(Manual):It is manually done using function like int(),float(),str().

String - A string is a sequence of characters (letters, numbers, symbols) enclosed in quotes.
String Methods:
1. replace() : Replaces a substring with another substring.
   str = "python is programming"
   print(str.replace("python","java")) #java is programming
   str is immutable datatype. Doesnot modify the original string.
   print(str) #python is programming

2. strip() : removes spaces (or characters) from both ends.
    str1 = "  python is programming language  "
    print(str1.strip(" "))
    str1 = "python is programming language"
    print(str1.strip("age"))
    print(str1.strip("p"))

3. join() : joins the elements of a list into a string.
    str2 = ["i","am","raju"]
    print(" ",join.(str2))

4. count() : counts occurrences of a substring.
   str = "python is programming"
   print(str.count("a"))
   print(str.count("i"))

5. index() : returns first position of substring(error if not found). and execution stops there when substring is not found.
   str = "python is programming"
   print(str.index("p"))

6. rindex() : returns last position of substring.
   str = "python is programming"
   print(str.rindex("p"))

7. find() : returns first index, returns (-1) when substring is not found.
   str = "python is programming"
   print(str.find("y"))
   print(str.find("z"))

8. rfind() : returns last index, -1 if not found.
   str = "python is programming"
   print(str.rfind('i'))
   
9. isupper() : checks if all charaters are uppercase.
   str = "python is programming"
   print(str.isupper())

10. upper() : converts all characters into uppercase.
    str = "python is programming"
    print(str.upper())
    
11. islower() : checks if all charaters are islower.
    str = "python is programming"
    print(str.islower())
    
12. lower() : converts all characters into uppercase.
    name = "pyTHon is programming"
    print(name.lower())
    
13. isalpha() : checks if string contains only letters.
    str = "python is programming"
    print(str.isalpha())
    
14. isnumeric() : checks if string contains only digits.
    str3 = "123"
    print(str3.isnumeric())
    
15. isalnum() : checks if string contains only letters + numbers.
    str5 = "python is programming123"
    print(str5.isalnum())
    
16. isdigits() : checks digits only.
    print(str3.isdigit())
    
17. endswith() : checks if strings ends with given value.
    str = "python is programming"
    print(str.endswith("programming"))
    
18. startswith() : checks if strings starts with given value.
    str = "python is programming"
    print(str.startswith("python"))
    
19. Concatenation() : joins the two strings.
    str = "python is programming"
    str3 = "123"
    print(str+str3)
    
20. zfill() :


Data types:
Data types specify what kind of value a variable refers to.
Python is  dynamically typed, so we don't need a declare the datatype explicity.
It is automatically determined based on the value.
Mutable object can be modified after creation, such as lists, sets and dictionaries.
Immutable object cannot modifies after creation such as int, float, str, tuple.
type() function is used to find the dat type of a variable.

str, int, float, tuple -> new object created
list, set, dict -> same object will be modified
