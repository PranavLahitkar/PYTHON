import array

# Tuple demonstration
tuple_example = (1, 2, 3, 4, 5)
print("Tuple example:", tuple_example)

# List demonstration
list_example = [6, 7, 8, 9, 10]
print("List example:", list_example)

# Array demonstration
array_example = array.array('i', [11, 12, 13, 14, 15])  # 'i' indicates signed integer type
print("Array example:", array_example)

# Accessing elements
print("Accessing elements:")
print("Second element of tuple:", tuple_example[1])
print("Third element of list:", list_example[2])
print("Fourth element of array:", array_example[3])

# Modifying elements
print("\nModifying elements:")
# Tuples are immutable, so we can't modify them directly
# list_example[0] = 100  # Uncommenting this line would modify the list
array_example[0] = 100  # Modifying the first element of the array
print("Modified array example:", array_example)

# Iterating through elements
print("\nIterating through elements:")
print("Tuple elements:")
for item in tuple_example:
    print(item)

print("List elements:")
for item in list_example:
    print(item)

print("Array elements:")
for item in array_example:
    print(item)
