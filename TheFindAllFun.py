import re
#return a list contsining every occurance of "ai"

txt= "The rain in Spain"
x = re.findall("ai", txt) # find out perticular "ai"alphabates in each word of string in x
print(x)