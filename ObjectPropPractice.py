class Flowers :
    def __init__(self,name,colour):
        self.name = name 
        self.colour= colour
    
    def function(self):
        print("The garden includes beautiful" + self.name )

f1= Flowers("Roses", "Red")
f1.colour = "Pink"
print(f1.colour)