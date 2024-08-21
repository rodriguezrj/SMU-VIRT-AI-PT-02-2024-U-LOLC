# Create a variable and set it as a list
info_list = ["Brad", 25, "John", 20]
print(info_list)

# Methods for accessing parts of a list
print(info_list[0])
print(info_list[-1])

# Return the value of a list at a given index


# Return the index of the first object with a matching value
print(info_list.index("John"))

# Return a list slice [index_start:index_end]
print(info_list[1:2])
print(info_list[1:3])
print(info_list[:2])


# Methods for modifying a list

# Add an element onto the end of a list
info_list.append("fun")
print(info_list)

# Change a specified element within a list at the given index
info_list[3] = "funny"

# Remove a specified object from a list
info_list.remove("John")

# Remove the object at the index specified
info_list.pop(2)

# Functions for accessing information about a list
# Define a list named scores
scores = [92, 87, 68, 75, 96]

# Return the max (or highest value) item in a list
print(max(scores))

# Return the min (or lowest) item in a list
print(min(scores))

# Return the sum of the items in a list
print(sum(scores))

# Return the length of the list
print(len(scores))

# Use sum and len to calculate average
print(f"Average: {sum(scores) / len(scores)}")

# Create a tuple, a sequence of immutable Python objects that cannot be changed
info_tuple = ("Python", 100, 4.65, False)

# Information functions also work on tuples, provided they contain valid data
# types
names_tuple = ("Melanie", "Jacinta", "Yindi", "Li")

print(len(names_tuple))
print(max(names_tuple))
print(min(names_tuple))

guests_tuple = (3, 5, 2, 4, 3)
print(sum(guests_tuple))