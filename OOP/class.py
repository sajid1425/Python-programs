class name :  #Class
    def __init__(self,uname,uy): #constructor
        self.uname=uname
        self.uy=uy      
    def year(self): # method
        print(self.uname+" is studing in "+self.uy)
    def intro(self):
        print("Hello I m "+self.uname)
name1 = name("Atharv","TY") #objectts
name2 = name("Alfaj","TY")
name1.intro()
name2.intro()
name1.year() #method call
name2.year()
name3 = name("Piyush","TY")
name3.intro()
name3.year()