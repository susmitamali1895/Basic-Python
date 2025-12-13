#MAKE A searh that returns no match
import re
txt = "The rain in Spain"
x= re.search("Portugal", txt)
print(x)