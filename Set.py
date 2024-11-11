# Initialize two sets
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# add() - Adds an element to the set
a.add(6)
print("After add(6) to a:", a)  # {1, 2, 3, 4, 5, 6}

# remove() - Removes an element from the set; raises KeyError if the element is not present
a.remove(6)
print("After remove(6) from a:", a) 

# union() - Returns a new set containing elements from both sets
set_union = a.union(b)
print("Union of a and b:", set_union)

# intersection() - Returns a new set containing only elements that are in both sets
set_intersection = a.intersection(b)
print("Intersection of a and b:", set_intersection) 

# difference() - Returns a new set containing elements in set_a but not in set_b
set_difference = a.difference(b)
print("Difference of a and b (a - b):", set_difference) 

# symmetric_difference() - Returns a new set with elements in either set_a or set_b but not in both
set_symmetric_difference = a.symmetric_difference(b)
print("Symmetric difference of a and b:", set_symmetric_difference) 

# issubset() - Checks if set_a is a subset of set_b
print("Is a a subset of b?", a.issubset(b)) 
