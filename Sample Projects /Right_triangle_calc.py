#Calculating the formula of the hypotenuse of the right triangle
import math

a = (int(input(f"Enter the value of the leg a: ")))
b = (int(input(f"Enter the value of the leg b: ")))

c = math.sqrt(pow(a, 2) + pow(b, 2)) #formula for the hypotenuse of the righ triangle
print(f"The hypotenuse of the right triangle is: {c}")
