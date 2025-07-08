import keyboard
import os
from pystyle import *
import arabic_reshaper
from bidi.algorithm import get_display

user_name = "r"
user_balance = 0
user_id = 0
user_k = 0
is_running = True
# ANSI escape codes for reverse video (swap foreground/background)
REVERSE = '\033[7m'
RESET = '\033[0m'

mydict = {
    0: {"id":0,  "name": "sataff", "balance": 0},
    1: {"id":1,  "name": "rami",   "balance": 1000},
    2: {"id":2,  "name": "rema",   "balance": 0},
    3: {"id":3,  "name": "fasil",  "balance": -50}

}

def main ():
    global user_name, user_balance, user_id, user_k
    global is_running
    is_running = True
    while is_running:
        os.system('cls' )
        print ("wellcome ")
        id = Write.Input("enter your id : ", Colors.blue_to_green, interval=0.1)
        found = 0
        if id.isdigit() and found == 0:
            for k, v in mydict.items():
                for sk, sv in mydict[k].items():
                    if  int (id) == mydict[k]["id"]:
                        user_name = mydict[k]["name"]
                        user_balance = mydict[k]["balance"]
                        user_id = mydict[k]["id"]
                        user_k = k
                        is_running = False
                        found = 1
        if id.isdigit() and found == 0:
            print ("id not found ")
            input("press any key ....")
        if not id.isdigit() : 
            print ("bad input enter number only 🥵 ")
            input("press any key ....")
    os.system('cls' )
    print (Box.DoubleCube(f"Welcome [{user_id}] Mr.  {user_name} "),Colors.black)
    print (Box.Lines("[1] balance"),Colors.black)
    print (Box.Lines("[2] deposit"),Colors.black)
    print (Box.Lines("[3] withdraw"),Colors.black)
    print (Box.Lines("[4] Add new customer"),Colors.black)
    print (Box.Lines("[5] Display all customers "),Colors.black)
    print (Box.Lines("[6] exit "),Colors.black)
    print (Box.Lines("[7] main menu"),Colors.black)



    is_running = True
    while is_running:
        choise = input("enter your choise : ")
        if choise.isdigit():
            choise = int(choise)    
            match choise:
                case 1 :
                    is_running = False
                    print (f"your balance is {user_balance} $")
                    kp = input("press any key to continue or q to main  ...")
                    if kp == 'q':
                        main()
                    else:
                        is_running = True
                case 2: 
                    deposit = int (input("enter the amount to deposit : "))
                    if deposit > 0:
                        user_balance += deposit
                        print (f"your new balance is {user_balance} $")
                        mydict[user_k]["balance"] = user_balance
                    else:
                        print ("the amount must be greater than 0")
                    kp = input("press any key to continue or q to main ...")
                    if kp == 'q':
                        main()
                    else:
                        is_running = True
                case 3:
                    if user_balance <= 0:
                        print ("you don't have any balance to withdraw")
                        kp = input("press any key to continue or q to main ...")
                        if kp == 'q':
                            main()
                        else:
                            is_running = True
                        continue
                    withdraw = int (input("enter the amount to withdraw : "))
                    if withdraw > 0 and withdraw <= user_balance:
                        user_balance -= withdraw
                        print (f"your new balance is {user_balance} $")
                        mydict[user_k]["balance"] = user_balance
                    elif withdraw > user_balance:
                        print ("you don't have enough balance")
                    else:
                        print ("the amount must be greater than 0")
                    kp = input("press any key to continue or q to main ...")
                    if kp == 'q':
                        main()
                    else:
                        is_running = True

                case 4:
                    os.system('cls')
                    print (Box.DoubleCube ('Add new customer ') )
                    Write.Print ("[+] Enter the new customer information", Colors.blue_to_green, interval=0.1)
                    new_id = mydict[len(mydict) - 1]["id"] + 1
                    print (f"the new customer id is {new_id}")    
                    new_name = input("enter the new customer name : ")
                    new_balance = int (input("enter the new customer balance : "))  
                    mydict[len(mydict)] = {"id": new_id, "name": new_name, "balance": new_balance}
                    print (f"new customer {new_name} with id {new_id} and balance {new_balance} $ added successfully")
                    kp = input("press any key to go to main ...")
                    main()
                case 5 :
                    os.system('cls')
                    print (Box.DoubleCube ('Display all customers\n') )
                    Write.Print ("[+] All customers information\n", Colors.blue_to_green, interval=0.1)
                    for k, v in mydict.items():
                        print (f"ID: {mydict[k]['id']}        Name: {mydict[k]['name']}        Balance: {mydict[k]['balance']} $")
                    kp = input("press any key to go to main ...")
                    main()
                case 6:
                    exit()
                case 7:
                    is_running = False
                    main()
                case _:
                    print ("your choice is not valid !")
        else :
            print ("you must enter number [1~6] !")   
    print ("good bye")

if __name__ ==  '__main__':
    main()