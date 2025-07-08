import keyboard  # مكتبة لمراقبة ضغطات المفاتيح
import random  # مكتبة لتوليد أرقام عشوائية
import os  # لمسح الشاشة في أنظمة Windows

os.system('cls')  # مسح الشاشة

print("Press 'Enter' to generate a random number.")
print("Press 'Esc' to stop the program.")

i = 10  # الحد الأقصى للأرقام العشوائية
counter = 0  # عداد للأرقام المولدة

while True:
    if keyboard.is_pressed('enter'):  # التحقق من الضغط على مفتاح Enter
        counter += 1
        random_number = random.randint(1, i)
        print(f"{counter}: {random_number}")
        while keyboard.is_pressed('enter'):  # انتظار تحرير مفتاح Enter
            pass

    if keyboard.is_pressed('esc'):  # التحقق من الضغط على مفتاح Esc
        print("Program stopped by user.")
        break
def key ():
    import keyboard  # مكتبة لمراقبة ضغطات المفاتيح
    import random  # مكتبة لتوليد أرقام عشوائية
    import os  # لمسح الشاشة في أنظمة Windows
    counter = 0
    while True:
        if keyboard.is_pressed('enter'):  # التحقق من الضغط على مفتاح Enter
            counter += 1
            print(f"{counter}")
            while keyboard.is_pressed('enter'):  # انتظار تحرير مفتاح Enter
                pass
        if keyboard.is_pressed('esc'):  # التحقق من الضغط على مفتاح Esc
            print("Program stopped by user.")
            break

key()

