mydict={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
#printing the dictionary
print(mydict)
#printing the dictionary by key
print(mydict.get(1))
#update the dictionary
mydict[1]="Mon"
print(mydict.get(1))
#deleting the key value pair
del mydict[5]
print(mydict)
#add new key value pair
mydict[8]="Hello"
print(mydict)
