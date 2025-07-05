#Type casting with user input
name = input("Enter your name: ")
age =float(input("Enter your  age: "))

#age = int(age)                                       
age = age + 1

print(f"Hello {name}")
print(f"Your are {age} years old")

import math  # Import math module to use math.sqrt()

pi = 3.141592653589793  # Assign the value of pi (a float)

# Compute the square root of pi (result is a float by default)
result_pi = math.sqrt(pi)

# --- Casting Demonstration ---

# Cast the result to float explicitly (not necessary here but shown for learning)
print(f"The square root of pi as a float: {float(result_pi)}")  # float → 1.7724538509...

# Cast the result to int (this will truncate the decimal part)
print(f"The square root of pi as an integer: {int(result_pi)}")  # int → 1

