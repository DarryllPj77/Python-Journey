# Typecasting -> Typecasting (also called type conversion) 
# is the process of converting one data type into another.
#               (string, integer, float, boolean)
#                   Explicit vs Implicit

name = "Darryll"
age = 21
gpa = 1.9
student = True

#Type Function
#type(name)
print(type(name)) # string
print(type(age)) # integer
print(type(gpa)) # float
print(type(student)) # bool

#Explicitly casting
age = float(age)
print(age)
#print(type(age))

gpa = int(gpa)
print(gpa)

student = str(student)
print(type(student))
print(student)

#Implicitly casting
x = 2
y = 2.0
x = x / y

print(x)

#Explicit Typecasting -> Manual conversion by the programmer
#Implicit Typecasting -> Automatic conversion by Python

"""
Explicit = You tell Python what to do.
Implicit = Python decides what to do.
"""


