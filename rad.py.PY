import os

def clear_terminal():
    # لمسح الشاشة في أنظمة Windows
    if os.name == 'nt':
        os.system('cls')
    # لمسح الشاشة في أنظمة Unix/Linux/Mac
    else:
        os.system('clear')

# مثال على الاستخدام:
clear_terminal()
print ("*********************************************************************")
NAME = input (" ENTER YOR NAME : \n\t ")
print (f"***********WELLCOME BACK MR. {NAME}******************\n")

""""
mark1 = input ("Enter your 1st mark : ")
mark2 = input ("Enter your 2nd mark : ")
mark3 = input ("Enter your 3rd mark : ")

avg_ = ( float (mark1 ) + float (mark2 ) + float (mark3 ))/3

print (f"MR {NAME} you are Enter ( {mark1} , {mark2} , {mark3} ) and the avarage is : {avg_:.5f}")
"""
radus = float ( input ("Enter the Radies : \n\t"))
PI = float ( 3.141592653589793 )
area  = float ( PI * (radus **2))

import math
print ("the pi constants is : ",math.pi)

print (f"\nthe area of  {radus:.1f} is {area:.2f}\n\n\n")