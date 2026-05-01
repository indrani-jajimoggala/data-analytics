'''
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
Class
Object
Inheritance
Polymorphism
Encapsulation

General Purpose Language : Using the python we can do different types of works or projects.
Web development
Data analysis
Machine learning
Automation
AI
'''

print("Hello Python")

a = 3
b = 6
print(a+b)

a = "hello"

'''
How it works?
- We write Python code is called source code(.py)
- Python converts source code -> byte code
- Bytecode is stored in -> .pyc file
- Byte is given to PVM
- PVM converts it into -> machine code(binary)
CPU executes -> gives output
'''

'''
If Python is interpreted, then why does it convert code into bytecode first?
Python is a high-level programming language. Computers understand only binary. 
So Python converts the code into bytecode, which is an intermediate form. 
This bytecode is executed by the Python Virtual Machine (PVM), which converts it into machine code and gives output.
'''
