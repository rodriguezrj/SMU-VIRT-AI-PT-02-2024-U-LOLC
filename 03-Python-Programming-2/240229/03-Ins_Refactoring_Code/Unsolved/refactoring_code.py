"""Refactoring Examples"""

# Code using for loop.
numbers = [1, 2, 3, 4, 5]

squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
# print(squared_numbers)

# Refactored the code to use a list comprehension
squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

# Code that uses the range() function.
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
    print(f"Index: {i}, Value: {numbers[i]}")

print()

# Refactored the code to use enumerate()
for i, num in enumerate(numbers):
    print(f"Index: {i}, Value: {num}")

# Code without a function.
numbers1 = [5, 10, 15, 20, 25]
total = 0
count = 0
for num in numbers1:
    total += num
    count += 1
average = total / count
print(f"The average is: {average}")

numbers2 = [1, 2, 3, 4, 5]
total = 0
count = 0
for num in numbers2:
    total += num
    count += 1
average = total / count
print(f"The average is: {average}")

# Refactored code with a function
# def calculate_average(numbers):
#     "Definition: calculates the average from a list of numbers"
#     total = sum(numbers)
#     length_of_list = len(numbers)
#     average = total / length_of_list
#     return average

def calculate_average(numbers):
    "Definition: calculates the average from a list of numbers"
    return sum(numbers) / len(numbers)

print(calculate_average(numbers1))
print(calculate_average(numbers2))

numbers3 = [0, 10, 434, 42, 25]
print(calculate_average(numbers3))