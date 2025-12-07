import json
#a python object(dict)
x = {
     "name":"John",
    "age": 30,
    "city": "New york"
}

#convert into Json
y = json.dumps(x)

#the result is a json string 
print(y)