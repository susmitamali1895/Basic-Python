import json 
print(json.dumps({"name":"john", "age":30})) #dictionary
print(json.dumps(["apple", "bananas"])) #list
print(json.dumps(("apple","bananas"))) #tuple
print(json.dumps("hello")) #string
print(json.dumps(42)) #int
print(json.dumps(31.56)) #float
print(json.dumps(True)) #boolean 
print(json.dumps(False)) #boolean 
print(json.dumps(None))