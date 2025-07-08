import os
import math
import random # لمسح الشاشة في أنظمة Windows
import time

os.system('cls') 
import sys
os.system('figlet ALI')
print("""
 
 /$$$$$$$                          /$$
| $$__  $$                        |__/
| $$  \ $$  /$$$$$$  /$$$$$$/$$$$  /$$
| $$$$$$$/ |____  $$| $$_  $$_  $$| $$
| $$__  $$  /$$$$$$$| $$ \ $$ \ $$| $$
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$
| $$  | $$|  $$$$$$$| $$ | $$ | $$| $$
|__/  |__/ \_______/|__/ |__/ |__/|__/
                                      
                                                         
""")
def loading_bar():
    print("\t  Loading...")
    for i in range(30 + 1):
        bar = "█" * i + "_" * (30 - i)
        sys.stdout.write(f"\r[{bar}] ")
        sys.stdout.flush()
        time.sleep(0.1)  
    print("\n")  
while True :
    x = int (random.randint (0,10))
    y = int (input("Enter the number  : "))
    time.sleep(0.5)
    if (x > y):
        print (f"the number {x} is greater than {y}")
    elif (x < y):
        print (f"the number {y} is greater than {x}")
    else :
        print (f"the number {x} is equal to {y}")
        print ("you are win ")
        break
