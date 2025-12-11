class Flowers:
    def __init__(self, fname, cname):
        self.flowername = fname
        self.colourname = cname

    def printname(self):
        print(self.flowername, self.colourname )

class petals(Flowers):
    def __init__(self, fname, cname, quantity):
        super().__init__(fname,cname)
        self.flowerquantity = quantity

    def welcome(self):
        print("Hi, I want to buy some",self.flowerquantity,  self.colourname,self.flowername )     

x = petals(4, "pink", "rose", ) 
x.welcome()  
