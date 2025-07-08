# print ("\u25cf  \u250c \u2500 \u2510 \u2502 \u2514 \u2518 \u2510")
import time 
import os 
import random
import sys
from pystyle import *
import msvcrt

os.system ("cls")

class res():
    @staticmethod
    def clar_res():
        os.system("cls")
        sys.stdout.write('\033[0m')
        formatted_time = time.strftime("%d/%m/%Y - %I:%M:%S %p")
        print("*" * 20, formatted_time, "*" * 20)

def show_rand (n):
    counter = 0

    while counter < 30 :
        x = int (random.randint(1,6))
        os.system("cls")
        print ("your number is :", n )
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
        time.sleep(0.01)
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

def game():

    print ("hi")
    res.clar_res()
    #**********************البداية الحقيقية للكود **********************#
    loading_intro()
    loading_bar() # استدعاء لدالة التحميل 
    res.clar_res()

    try_ = 5
    agine = False
    is_play = True
    agine = 1
    while is_play :
        if try_ == 0:
            while agine:
                Write.Print("\n\nDo you want to play again ? [y/n] ", Colors.blue_to_green, interval=0.1)
                con=msvcrt.getwch()
                print(con) 
                if con == 'n':
                    print("\n\nthank you for using my program >>>>>   good bye....\n\n")
                    time.sleep(3)
                    exit()
                elif con == 'y':
                    os.system("cls")
                    game()
                else :
                    print ()
                    print ("  \t >>>   bad input")
                    time.sleep(1)
        res.clar_res()
        
        n = input (" enter number [1 === > 6 ] : ")
        if n.isdigit() == True :
         print ("is d ")
         if int (n) <= 6 and int (n) >= 1 :
            print (" and <6 , >1")
            try_ -= 1
            m = show_rand(n)
            i = msvcrt.getwch()
            if m == int(n) :
                print (f"you enter {n} and the random is {m} welldone ")
                cong ()
                try_=0    
        else :
            print ("not d ")
            print ("bad input")
        

        # if m == int (n) :
        #     print (" you are like man ")
        #     cong ()
        #     sys.exit

if __name__ == "__main__":
    game()