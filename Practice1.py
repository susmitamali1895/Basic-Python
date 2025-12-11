class Cars:
    def __init__(self,bname, cname):
        self.brandname = bname
        self.carname = cname 

    def printname(self):
        print(self.brandname, self.carname)

class Subcar(Cars):
    def __init__(self, bname, cname , year):
        super().__init__(bname,cname)
        self.modelyear = year

    def welcome(self):
        print("Congratulation for your new", self.brandname, self.carname, self.modelyear)

x = Subcar("ford","Mustang", 2020)
x.welcome()
