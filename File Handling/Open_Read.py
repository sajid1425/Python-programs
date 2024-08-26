# You can open a file in two ways by using open() & by using with

#Open file in read mode
file = open('sample.txt','r')
#read entire content
content=file.read()
print(content)
# Go back to the beginning of the file
file.seek(0)
#read line by line
line=file.readline()
print(line)
# Go back to the beginning of the file
file.seek(0)
#read line into a list
lines = file.readlines()
print(lines)
#close a file
file.close()
