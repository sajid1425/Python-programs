# Initialize a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# append() - Add an element to the end of the list
my_list.append(6)
print("\nAfter append(6):", my_list)

# insert() - Insert an element at a specific position
my_list.insert(2, 10)  # Insert 10 at index 2
print("After insert(2, 10):", my_list)

# remove() - Remove the first occurrence of a specific element
my_list.remove(10)
print("After remove(10):", my_list)

# pop() - Remove and return the element at a specific position (or last element if no index is specified)
popped_element = my_list.pop()  # Remove last element
print("After pop():", my_list)
print("Popped element:", popped_element)

# extend() - Extend the list by adding elements from another list
my_list.extend([7, 8])
print("After extend([7, 8]):", my_list)

# count() - Return the number of occurrences of a specific element
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)

# reverse() - Reverse the order of the list
my_list.reverse()
print("After reverse():", my_list)

# copy() - Return a shallow copy of the list
list_copy = my_list.copy()
print("\nCopy of List:", list_copy)

# clear() - Remove all elements from the list
my_list.clear()
print("After clear():", my_list)