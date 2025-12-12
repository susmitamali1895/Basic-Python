class Person:  #class declaration Person
    def __init__(self, name,age): #person properties name and age, same class declaration that why we use self
        self.name = name
        self.age = age
p1 = Person("Gaurav",34) # p1 is object
print(p1.name) 
print(p1.age)