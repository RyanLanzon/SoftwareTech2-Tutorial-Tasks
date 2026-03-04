import math


factorials = {x: math.factorial(x) for x in range(1, 11)}


result = factorials[6] * factorials[5]

print(factorials)
print("6! * 5! =", result)