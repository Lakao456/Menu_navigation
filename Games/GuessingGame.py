from tkinter import *
from tkinter import messagebox

import random

print("1--Easy",
      "2--Moderate",
      "3--Hard",
      "4--Custom",
      sep='\n', end="\n ----------------------------- \n")

difficulty = int(input("Select a level of difficulty::"))

if difficulty == 1:
    lower_limit, upper_limit = 1, 100
elif difficulty == 2:
    lower_limit, upper_limit = 1, 9999
elif difficulty == 3:
    lower_limit, upper_limit = -1000, 34500
elif difficulty == 4:
    print("Enter the range of the random number")
    lower_limit = int(input("Lower limit::"))
    upper_limit = int(input("Upper limit::"))

x = random.randint(lower_limit, upper_limit)

# print(x)
print("you have to guess the random number between ", lower_limit, " and ", upper_limit)
repeat, c, ci, un = True, 0, 0, 0
u = int(input("Your guess here::"))
c += 1
ci += 1
while (repeat == True):
    if u == x or un == x:
        print("your guess is right !")
        print("you guessed  the no. in ", c, " turns")
        repeat = False
    elif u > x:
        if ci == 1:
            print("Your guess is greater than the number")
        un = int(input("Your next guess here::"))
        c += 1
        ci += 1
        if un > u:
            print("going the wrong way...")
            u = un
        elif un <= u and un > x:
            print("getting closer!")
            u = un
        elif un < x:
            u = un
            ci **= 0

    elif u < x:
        if ci == 1:
            print("Your guess is smaller than the number")
        un = int(input("Your next guess here::"))
        c += 1
        ci += 1
        if un < u:
            print("going the wrong way...")
            u = un
        elif un >= u and un < x:
            print("getting closer!")
            u = un
        elif un > x:
            u = un
            ci **= 0

end = input("Press enter to exit.")

# print("G",u,un,c,sep='|')
