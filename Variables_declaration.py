#In Python, a variable is a name that refers to a value stored in memory. 
#You use variables to store data so you can work with it later.

#String variables for string Data type
first_name = "Darryll"
food = "Pizza"
email = "darryll@gmail.com"

#use f-string
print(f"Hello {first_name}")
print(f"I like {food}")
print(f"My email is: {email}")


#Integers
age = 25
number = 8
students = 30
print(f"You are {age} years old")
print(f"My favorite decimalnumber is {number}")
print(f"The number of students in my class is {students}")

#float
price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is ${price}")
print(f"My gpa is {gpa}")
print(f"You ran {distance}km")


#Boolean
is_student1 = False
is_student2 = True
print(f"Are you a student?:{is_student1}")
print(f"Are you a student?:{is_student2}")

if is_student1:
    print("You are a student")
else:
    print("You are not a student")

if is_student2:
    print("You are a student")
else:
    print("You are not a student")
    
    
    
its_online_class = True

if its_online_class:
    print("We have online class")
else:
    print("We have onsite class")
    
#Output - Technically, these are multi-line strings, not actual comments. But Python ignores them if they aren’t assigned to a variable, so they work like comments.
"""
Hello Darryll
I like Pizza
My email is: darryll@gmail.com
You are 25 years old
My favorite decimalnumber is 8
The number of students in my class is 30
The price is $10.99
My gpa is 3.2
You ran 5.5km
Are you a student?:False
Are you a student?:True
You are not a student
You are a student
We have online class
"""





