# Type casting with user input

# Ask the user for their name (input is always a string)
name = input("Enter your name: ")

# Ask the user for their age
# input() returns a string, so we cast it to float to allow decimal ages
age = float(input("Enter your age: "))

# Optionally, we could cast to int using: age = int(age)
# But using float allows for inputs like 20.5

# Add 1 to the age (this works because it's a number now)
age = age + 1

# Display output using f-strings
print(f"Hello {name}")
print(f"You are {age} years old")  # Displays float (e.g., 21.0 if 20 was input)


import math  # Import math module to use math.sqrt()

pi = 3.141592653589793  # Assign the value of pi (a float)

# Compute the square root of pi (result is a float by default)
result_pi = math.sqrt(pi)

# --- Casting Demonstration ---

# Cast the result to float explicitly (not necessary here but shown for learning)
print(f"The square root of pi as a float: {float(result_pi)}")  # float → 1.7724538509...

# Cast the result to int (this will truncate the decimal part)
print(f"The square root of pi as an integer: {int(result_pi)}")  # int → 1

