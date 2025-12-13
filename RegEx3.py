import re
txt = "Hello, Welcome to India"
x = re.search("^hi.*welcome$", txt)
if x:
    print("Yes, we have a match!")
else:
    print("No Match")