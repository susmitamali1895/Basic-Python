squares = [x**2 for x in range (1,21) if x%2 ==0]
filter =[num for num in squares if num%4 != 0]
print(filter)
print(squares)