file = open("C:/Users/Sajid/OneDrive/Desktop/Sajid/Python/File HAndling/Text.txt", "a")
file.write("New added line is this.\n")
file.close()

file = open("C:/Users/Sajid/OneDrive/Desktop/Sajid/Python/File HAndling/Text.txt", "r")
Text = file.read()
print(Text)
file.close()