import re
txt = "Opportunities dont happen, you create them"
x = re.search("^Opportunities.*them$", txt)
if x :
    print("Yes, we have a match!")
else:
    print("No match")