import array

# Initialize an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])
print("Original Array:", my_array)

# append() - Add an element to the end of the array
my_array.append(6)
print("\nAfter append(6):", my_array)

# insert() - Insert an element at a specific position
my_array.insert(2, 10)  # Insert 10 at index 2
print("After insert(2, 10):", my_array)

# pop() - Remove and return an element at a specific position (or last element if no index is specified)
popped_element = my_array.pop()  # Remove last element
print("\nAfter pop():", my_array)
print("Popped element:", popped_element)

# remove() - Remove the first occurrence of a specific element
my_array.remove(10)
print("After remove(10):", my_array)