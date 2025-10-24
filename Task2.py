list1 = [25,30,84,45,98]
evennum= [num for num in list1 if num %2 ==0]
print("even  numbers" , evennum)

if evennum:
     avg = sum(evennum)/len(evennum)
     print(avg)