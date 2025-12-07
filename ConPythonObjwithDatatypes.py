import json 
x = {
    "name": "john",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Anna", "Billy"),
    "Pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model":"Ford edge", "mpg": 24.1}
    ]
    }
# convert into json
y = json.dumps(x)

#the result is a JSON string:
print(y)