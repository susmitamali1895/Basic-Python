class Bank:
    def __init__(self, name , branch):
        self.name = name
        self.branch = branch
b1 = Bank("ICICI", "pune")
print(b1.name)
print(b1.branch)