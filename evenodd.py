import os # لمسح الشاشة في أنظمة Windows
import random # مكتبة لتوليد أرقام عشوائية
import keyboard  #  مكتبة لمراقبة ضغطات المفاتيح
import time # مكتبة لتأخير التنفيذ
t=0
while True :
    time.sleep(2)
    t=2
    os.system  ('cls')
    x = int (input ("Enter the number : "))
    if (x >= 0):
        if (x%2) == 0:
            print (f"the number {x} is even number ")
        else : 
            print (f"the numer {x} is odd number ")
    else:
        print ( "the number is  negative number ")
        break

"""
n = input("Enter a number: ")
# Check if n is None    
if n is "":
    print("n is None")-
else:
    print("n is not None")



n = input("Enter a number: ")
while True:
    n = input()
    if n is "":
        print(random.randint(1,100))
    elif (keyboard.is_pressed('esc')):  # 
        print("Program stopped by user.")
        break
    else :
        break"""