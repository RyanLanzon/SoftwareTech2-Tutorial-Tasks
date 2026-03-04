import math

# List of tuples (x, factorial of x) for numbers 5 to 10
result = [(x, math.factorial(x)) for x in range(5, 11)]

print(result)