#The search function 
import re
txt = "The rain in Spain" #counting characters indexwise  starts rom 0
x = re.search("\s", txt)
print("The first white-space character is located in position", x.start())