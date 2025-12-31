# Core python funcions
# 1. Print() - Display ouput to console
name = "Susmita"
print("Hello ", name )

# 2. Len() - Find length of strings, lists, tuples, dicts
print(len(name))
print(len([1,2,3]))

# 3. type() Check datatype
print(type(3.14))
print(type(name))

# 4. input - Take input from user 
#nameuser = input("Enter name: ")

# 5 id() Get memory location of object 
x = 10
print(id(x))

# List and Sequence functions 
# 6. range()- Used in loops 
for i in range(10):
    print(i) # o/p is from 0 to 10


# 7. enumerate()- Iterate with index + item
for idx, val in enumerate(['a','b']):
    print(idx, val) # index for a is 0 and  for b it is 1. 

fruits = ["apple","mango", "grape"]
for index, value in enumerate(fruits):
    print(index, value)

# 8. zip() - combine multiple iterables 
for x,y in zip([1,2],[3,4]):
    print(x,y) # o/p is combination x and x & y and y = 1,3 & 2, 4

names = ["john", "Amit", "sara"]
marks = [85,90,75]
for n,m in zip(names, marks):
    print(n,m)

# 9. sorted - returns sorted list 
sorted([5,3,1])

#10. reserved()- Iterate in reverse
for i in reversed("abcd"):

# Useful Built-ins 
