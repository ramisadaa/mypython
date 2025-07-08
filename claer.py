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
print ("*********************************************************************\n\n")





import os; os.system('cls' if os.name == 'nt' else 'clear')
# لمسح الشاشة في أنظمة Windows
