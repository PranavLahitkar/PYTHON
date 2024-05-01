# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Displaying sets
print("Set 1:", set1)
print("Set 2:", set2)

# Adding elements to a set
set1.add(6)
print("After adding element to set 1:", set1)

# Removing elements from a set
set2.remove(8)
print("After removing element from set 2:", set2)

# Set operations
print("\nSet operations:")
# Union
union_set = set1.union(set2)
print("Union of set 1 and set 2:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of set 1 and set 2:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference of set 1 and set 2:", difference_set)

# Symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set 1 and set 2:", symmetric_difference_set)

# Checking for subset and superset
print("\nSubset and superset:")
subset = {4, 5}
print("Is", subset, "a subset of set 1?", subset.issubset(set1))
print("Is set 1 a superset of", subset, "?", set1.issuperset(subset))

# Set iteration
print("\nIterating through set elements:")
for item in set1:
    print(item)

# Set comprehension
print("\nSet comprehension:")
set3 = {x for x in range(10) if x % 2 == 0}
print("Set 3:", set3)
