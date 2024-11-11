# Initialize two frozensets
fset_a = frozenset([1, 2, 3, 4, 5])
fset_b = frozenset([4, 5, 6, 7, 8])

# union() - Returns a new frozenset containing elements from both sets
frozen_union = fset_a.union(fset_b)
print("Union of fset_a and fset_b:", frozen_union)  # frozenset({1, 2, 3, 4, 5, 6, 7, 8})

# intersection() - Returns a new frozenset containing only elements that are in both sets
frozen_intersection = fset_a.intersection(fset_b)
print("Intersection of fset_a and fset_b:", frozen_intersection)  # frozenset({4, 5})

# difference() - Returns a new frozenset containing elements in frozen_set_a but not in frozen_set_b
frozen_difference = fset_a.difference(fset_b)
print("Difference of fset_a and fset_b (fset_a - fset_b):", frozen_difference)  # frozenset({1, 2, 3})
