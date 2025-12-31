cars = ['BMW', 'Audi', 'Venue', 'Honda', 'Hyundai', 'kia', 'Volkswagon']
print(cars)
print(len(cars))
print(type(cars))

#Access 1st car in List
print(cars[0])

#Print last item
print(cars[-1])

#list upto 4
print(cars[:4])

#list from index 3 
print(cars[3:])

#negative indexing
print(cars[-4:-1])

# check if item exist
if "BYD" in cars:
    print("Yes BYD Present")
else:
    print(" BYD Not present")

