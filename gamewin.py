# print ("\u25cf  \u250c \u2500 \u2510 \u2502 \u2514 \u2518 \u2510")
import time 
import os 
import random
import sys
os.system ("cls")
try_ = 1
def main ():
    global m 
    def cong ():
        # Get terminal size
        try:
            columns, rows = os.get_terminal_size()
        except OSError:
            columns, rows = 80, 24  # fallback default

        box_width = 42
        box_height = 5
        vertical_padding = max((rows - box_height) // 2, 0)
        horizontal_padding = max((columns - box_width) // 2, 0)

        print("\n" * (vertical_padding))
        print(" " * horizontal_padding + "╔" + "═" * 40 + "╗")
        print(" " * horizontal_padding + "║{:^40}║".format("Congratulations!"))
        print(" " * horizontal_padding + "║{:^40}║".format("You guessed the right number!"))
        print(" " * horizontal_padding + "║{:^40}║".format("Well done and celebrate!"))
        print(" " * horizontal_padding + "╚" + "═" * 40 + "╝")
        
        time.sleep(5)
        os.system("cls")
    
    while True :
        n = input (" enter number [1 === > 6 ] : ")
        if int (n) > 6 or int (n) < 1 :
            print ("out of range ")
        elif int (n) <= 6 or int (n) >= 1 :
            m = show_rand()
            if m == int (n) :
                print (" you are like man ")
                cong ()
                sys.exit
            elif try_ < 3:
                print (f" you have {3-try_} tryes ")
                break
            elif try_ == 3 :
                print (" you lose the Game ")
                break
        else:
            print ("you enter bad input ")
            print ("enter number [   1   ==== >>>   6  ]")


def show_rand ():
    counter = 0
    while counter < 30 :
        x = int (random.randint(1,6))
        os.system("cls")
        if x == 1:
            print ("┌─────────┐")
            print ("│         │")
            print ("│    ●    │")
            print ("│         │")
            print ("└─────────┘")
            time.sleep (.1)
        if x == 2:
            print ("┌─────────┐")
            print ("│  ●      │")
            print ("│         │")
            print ("│      ●  │")
            print ("└─────────┘")
            time.sleep (.1)
        if x == 3: 
            print ("┌─────────┐")
            print ("│  ●      │")
            print ("│    ●    │")
            print ("│      ●  │")
            print ("└─────────┘")
            time.sleep (.1)
        if x == 4:
            print ("┌─────────┐")
            print ("│  ●   ●  │")
            print ("│         │")
            print ("│  ●   ●  │")
            print ("└─────────┘")
            time.sleep (.1)
        if x == 5:
            print ("┌─────────┐")
            print ("│  ●   ●  │")
            print ("│    ●    │")
            print ("│  ●   ●  │")
            print ("└─────────┘")
            time.sleep (.1)
        if x == 6:
            print ("┌─────────┐")
            print ("│  ●   ●  │")
            print ("│  ●   ●  │")
            print ("│  ●   ●  │")
            print ("└─────────┘")
            time.sleep (.1)
        
        counter +=1
    return(x)

def loading_bar():
    """
    استدعاء دالة شريط التحميل
    """
    print("\t\t    Loading...\n")
    bar_length = 50  # طول شريط التحميل

    # الحصول على عرض التيرمنال
    try:
        columns, _ = os.get_terminal_size()
    except OSError:
        columns = 80  # قيمة افتراضية

    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = "█" * i + "_" * (bar_length - i)
        # حساب المسافة البادئة لجعل الشريط في المنتصف
        padding = max((columns - (bar_length + 7)) // 2, 0)
        sys.stdout.write("\r" + " " * padding + f"[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

def loading_intro() :
    print("""
          
    '   ▄█     █▄   ▄█  ███▄▄▄▄   ███▄▄▄▄    ▄█  ███▄▄▄▄      ▄██████▄  
    '  ███     ███ ███  ███▀▀▀██▄ ███▀▀▀██▄ ███  ███▀▀▀██▄   ███    ███ 
    '  ███     ███ ███▌ ███   ███ ███   ███ ███▌ ███   ███   ███    █▀  
    '  ███     ███ ███▌ ███   ███ ███   ███ ███▌ ███   ███  ▄███        
    '  ███     ███ ███▌ ███   ███ ███   ███ ███▌ ███   ███ ▀▀███ ████▄  
    '  ███     ███ ███  ███   ███ ███   ███ ███  ███   ███   ███    ███ 
    '  ███ ▄█▄ ███ ███  ███   ███ ███   ███ ███  ███   ███   ███    ███ 
    '   ▀███▀███▀  █▀    ▀█   █▀   ▀█   █▀  █▀    ▀█   █▀    ████████▀  
    '                                                                   
    """)


#**********************البداية الحقيقية للكود **********************#
loading_intro()
loading_bar() # استدعاء لدالة التحميل 
os.system("cls ")
while try_ <= 3 :
    #print (loading_bar.__doc__) تقوم بعرض الوصف عن function 
    
    main ()
    try_ +=1
print ("do you want to play agin  [ y - n ]: ")
input ("press any key to cont.....")