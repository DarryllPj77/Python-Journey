import math  # Importing the math module to access mathematical constants and functions

# Integer and float values
x = 9
x1 = 9.14
x2 = 9.14

# Print math constants from the math module
print(f"Circumference of a circle to its diameter value is: {math.pi}")  # π ≈ 3.14159
print(f"Mathematical constant approximately is equal to: {math.e}")     # e ≈ 2.71828

# --- Math operations ---

# Square root of x
result = math.sqrt(x)  # Returns float, sqrt(9) = 3.0

# Ceiling: smallest integer greater than or equal to x1
result1 = math.ceil(x1)  # ceil(9.14) = 10

# Floor: largest integer less than or equal to x2
result2 = math.floor(x2)  # floor(9.14) = 9

# Print results with type casting
print(f"The squareroot of x is: {(int(result))}")  # Casting 3.0 to 3
print(f"The ceil of x1 is: {result1}")             # Output: 10
print(f"The floor of x2 is: {result2}")            # Output: 9

# --- Extra: square root of pi (demonstrating both float and int casting) ---

pi = 3.141592653589793  # Accurate value of π
result_pi = math.sqrt(pi)  # Square root of pi ≈ 1.77245

# Casting result to float (optional, since it's already float)
print(f"The squareroot of pi is: {(float(result_pi))}")  # e.g., 1.7724538509055159

# Casting result to int (truncates decimal part)
print(f"The squareroot of pi is: {(int(result_pi))}")    # Output: 1
