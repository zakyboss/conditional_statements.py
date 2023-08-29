#Assignment 1
#write a program to check if a number is divisible by 7
number=input("Please Insert Number:\n")
number=int(number)
if number%7==0:print("Number Is Divisible")
else:print("Number Is Not Divisible")

#Assignment 2
#write a program to calculate electricity bill based on foolowing criteria 
# first 50 units ksh 20
# next 50 units ksh 40
# after 100 units ksh 100
electricity=input("Please insert Number of units")
electricity=int(electricity)
if electricity<=50:print(20)
elif electricity>50 &electricity<=100:print(40)
else:print(100)
