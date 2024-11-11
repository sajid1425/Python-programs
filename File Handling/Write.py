file = open("C:/Users/Sajid/OneDrive/Desktop/Sajid/Python/File HAndling/Text.txt", "w")
file.write("Hello, world!\n")
file.write("I am Sajid Sayyad.\n")
file.close()

file = open("C:/Users/Sajid/OneDrive/Desktop/Sajid/Python/File HAndling/Text.txt", "r")
content = file.read()
print(content)
file.close()
