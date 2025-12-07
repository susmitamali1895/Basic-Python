def my_function (n): # function declaration
    return lambda a: a *n #multiplication
mydoubler = my_function(2) #value of n in new variable mydoubler
print(mydoubler(11))  # value of a with new variable myoubler