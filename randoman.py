import os
import random

def clear_terminal():
    # لمسح الشاشة في أنظمة Windows
    if os.name == 'nt':
        os.system('cls')
    # لمسح الشاشة في أنظمة Unix/Linux/Mac
    else:
        os.system('clear')

# مثال على الاستخدام:
clear_terminal()
print("*********************************************************************\n\n")

# إدخال القيم
print("Enter the 1st number: ")
x = int(input())
print("Enter the 2nd number: ")
y = int(input())
print("Enter the number of random integers you want: ")
z = int(input())

# التحقق من صحة المدخلات
if x > y:
    x, y = y, x  # تبديل القيم إذا كان x أكبر من y

if z <= 0:
    print("Error: The number of random integers must be greater than 0.")
elif z > (y - x + 1):
    print("Error: The count cannot be greater than the range of numbers.")
else:
    # توليد الأرقام العشوائية باستخدام random.sample
    random_numbers = random.sample(range(x, y + 1), z)
    print("Random numbers: " + ", ".join(map(str, random_numbers)))