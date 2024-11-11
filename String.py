# Initialize a string
my_string = "  Hello, Python World!  "
print("Original String:", my_string)

# format() -  specified value(s) and insert them inside the string's placeholder.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# strip() - Remove leading and trailing whitespace
print("\nstrip():", my_string.strip())

# upper() - Convert all characters to uppercase
print("upper():", my_string.upper())

# lower() - Convert all characters to lowercase
print("lower():", my_string.lower())

# replace() - Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# find() - Find the first occurrence of a substring
print("find('Python'):", my_string.find('Python'))

# count() - Count occurrences of a substring
print("\ncount('o'):", my_string.count('o'))

# capitalize() - Capitalize the first character
print("\ncapitalize():", my_string.capitalize())

# title() - Capitalize the first letter of each word
print("title():", my_string.title())
 