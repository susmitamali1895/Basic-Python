class Cars :
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    
    def __str__(self):
        return f"{self.name}{self.colour}"
    
c1 = Cars("Thar", "Black")
print(c1.name)
print(c1.colour)        