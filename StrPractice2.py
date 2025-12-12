class Vegetables:
    def __init__(self,name,price):
        self.name = name 
        self.price= price
    def __str__(self):
        return f"{self.name}{self.price}"
    
v1= Vegetables("Potato", 40)
print(v1.name)
print(v1.price)