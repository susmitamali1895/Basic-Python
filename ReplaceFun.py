#replace the first 2 occurance 
import re 
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) #substitute space with 9 replacement
print(x)