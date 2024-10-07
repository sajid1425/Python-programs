import re
message="Hello this is my message by Alfaj and my roll number is 14 & Atharavs roll number is 10 & password is pass@123"

# \d is used for decimals
regex='\d'
match=re.findall(regex,message)
print(match)

# \d+ is used for decimals & concate 
regex='\d+'
match=re.findall(regex,message)
print(match)

# \D is used to match the input other than character
regex ='\D+'
match=re.findall(regex,message)
print(match)

# \S is used to match all character other than white space
regex ='\S+'
match=re.findall(regex,message)
print(match)

# \s is used to match white spaces
regex ='\s+'
match=re.findall(regex,message)
print(match)

# \w is used to match all alpha numeric character
regex ='\w+'
match=re.findall(regex,message)
print(match)

# \W is used to match non alpha numeric character
regex ='\W+'
match=re.findall(regex,message)
print(match)

#