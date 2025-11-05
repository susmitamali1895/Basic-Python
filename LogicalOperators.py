x = 5
y = 10

# Logical AND
# Both conditions must be True
print("x > 3 and y < 15:", x > 3 and y < 15)  # True and True => True

print("x > 3 and y > 15:", x > 3 and y > 15)  # True and False => False

# Logical OR
# At least one condition must be True
print("x > 6 or y < 15:", x > 6 or y < 15)    # False or True => True

print("x > 6 or y > 15:", x > 6 or y > 15)    # False or False => False

# Logical NOT
# Reverses the result
print("not(x > 3):", not(x > 3))              # not(True) => False

print("not(y < 5):", not(y < 5))              # not(False) => True