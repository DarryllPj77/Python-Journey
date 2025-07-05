# Built-in Functions Demo

x = 3.14   # originally a float number (pi)
y = 14     # an integer
x = 5      # x is reassigned to 5, overwriting 3.14

# result = round(x) 
# → Would round x to the nearest integer. Since x is now 5, round(5) = 5

# result = abs(y)
# → Would return the absolute value of y. Since y = 14, abs(14) = 14

result = pow(4, 3)
# → Raises 4 to the power of 3 → 4^3 = 64

# result = max(x, y, z)
# → Would return the largest value among x, y, and z 
# → This line is currently commented out and would raise an error unless 'z' is defined

print(result)  # Output will be 64 since pow(4, 3) = 64
