# List of numbers from 0 to 99
numbers = [x for x in range(100)]

# Numbers divisible by 5
divisible_by_5 = [x for x in numbers if x % 5 == 0]

print(numbers)
print(divisible_by_5)