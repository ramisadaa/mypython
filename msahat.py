
import os; os.system('cls' if os.name == 'nt' else 'clear')
# لمسح الشاشة في أنظمة Windows

import math 
print("enter the 1st number: ")
x = int(input())
print("enter the 2nd number: ")
y = int(input())


the_masaha = float ( math.pi * pow(x, 2))
print("the masaha is: " , (round(the_masaha, 0)),  "cm²")


the_masaha2 =  x * y
print("the masaha2 is: " , (the_masaha2) , "cm²")  

the_mohet = 2 * (x + y)
print("the mohet is: " , (the_mohet) , "cm")





