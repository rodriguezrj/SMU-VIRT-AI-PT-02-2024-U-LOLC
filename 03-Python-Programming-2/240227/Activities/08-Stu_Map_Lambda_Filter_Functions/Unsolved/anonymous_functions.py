""" Anonymous Functions"""

# 1. Get the even numbers from a list using the filter and lambda functions.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)


# 2. Use the map and lambda functions to add the numbers from both lists.
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]

sum_of_nums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(sum_of_nums)


# 3. Use the map and lambda functions to split the following sentence into words.
sentence = "My favorite hobby is coding in Python"
print(sentence.split())

x = "  fun  "
print(x)
print(x.strip())

words = list(map(lambda x: x, sentence.split()))

words = list(map(lambda x: x.strip(), sentence.split()))
print(words)