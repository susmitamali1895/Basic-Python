#return an Empty list if no match was found
import re 
txt= "The rain in Spain"
#check if "portugal" is in the string
x= re.findall("Portugal", txt)
print(x)

if (x):
    print("Yes, there is atleast one match!")
else:
    print("No match")