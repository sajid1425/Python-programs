# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 1. copy() method - Creates a shallow copy of the dictionary
copied_dict = my_dict.copy()  
print(f"Copied Dictionary: {copied_dict}")  

# 2. get() method - Retrieves the value for a specified key, or returns a default value if the key does not exist
value_a = my_dict.get('a')  
value_not_found = my_dict.get('d', 'Not Found') 
print(f"get('a'): {value_a}")  
print(f"get('d'): {value_not_found}")  

# 3. fromkeys() method - Creates a new dictionary from a sequence of keys, all having the same value
new_dict = dict.fromkeys(['x', 'y', 'z'], 0)  
print(f"New Dictionary fromkeys(): {new_dict}") 

# 4. items() method - Returns a view object of all key-value pairs as tuples
items = my_dict.items()  
print(f"Items: {items}")  

# 5. pop() method - Removes the specified key-value pair and returns the value, or returns a default value if the key doesn't exist
removed_value = my_dict.pop('b') 
print(f"Popped 'b': {removed_value}") 
print(f"Dictionary after pop: {my_dict}")  

# 7. update() method - Adds key-value pairs from another dictionary or iterable to the current dictionary
my_dict.update({'e': 5, 'a': 7}) 
print(f"Dictionary after update: {my_dict}") 

# 8. values() method - Returns a view object of all the values in the dictionary
values = my_dict.values()  
print(f"Values: {values}")  

# 9. popitem() method - Removes and returns the last key-value pair as a tuple (insertion order is preserved)
popped_item = my_dict.popitem() 
print(f"Popped item: {popped_item}")  
print(f"Dictionary after popitem: {my_dict}")  

