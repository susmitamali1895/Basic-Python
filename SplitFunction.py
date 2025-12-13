#split at each whitespace character 
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)