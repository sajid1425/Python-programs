#using with
with open('example.txt', 'w') as file:
    file.write('this is sample sample')
file.close

with open('example.txt','r') as file:
    content=file.read()
    print(content)
file.close