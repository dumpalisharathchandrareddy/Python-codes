# Populate a list with strings of alphanumeric characters
myList = ["A1", "12", "Z", "34", "A2", "52", "Z1", "64", "A12"]

# List comprehension to create a new list with only numeric values
numericList = [x for x in myList if x.isnumeric()]

print("List created after List Comprehension:", numericList)
