import time
import os 

os.system('cls')  # لمسح الشاشة في أنظمة Windows
import sys
def loading_bar():
    print("\t\t    Loading...\n")
    bar_length = 50  # طول شريط التحميل
    for i in range(bar_length + 1):
        # حساب النسبة المئوية
        percent = int((i / bar_length) * 100)
        # إنشاء الشريط
        bar = "█" * i + "_" * (bar_length - i)
        # طباعة الشريط مع النسبة المئوية
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.1)  # تأخير بسيط بين كل خطوة
    print("\n")  # الانتقال إلى السطر التالي بعد انتهاء التحميل

# استدعاء دالة شريط التحميل
loading_bar()
os.system('cls')