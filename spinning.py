import os
import random as R
import time
import sys
from pystyle import *
import msvcrt



def start():
    balance = 1000
    rahan = 50
    is_running = 1
    while is_running :
        os.system("cls")
        sys.stdout.write('\033[0m')
        print (Box.DoubleCube ('your balance is : ' + str(balance) + ' $') )
        print (Box.DoubleCube ('your rahan  is : ' + str(rahan) + ' $') )
        print (Box.Lines (' [+] this is SPIN GAME ') )  
        Write.Print ('[-] this is game is role  \n\n', Colors.purple_to_red, interval=0.1)
        Write.Print ('["   🍌    ","   🍒   ","   🍋   ","   🍉   ","   ⭐   ","   ❤️   "]  \n\n', Colors.purple_to_red, interval=0.02)
        input("are you ready to play ❓ press ENTER to spin ...")
        balance -=rahan 

        list = ["🍌","🍒","🍋","🍉","⭐","❤️"]
        cou = 20
        while cou>0:
            os.system("cls") 
            for i in list:
                x = R.choice(list)
                y = R.choice(list)
                z = R.choice(list)
                l = R.choice(list)
                m = R.choice(list)
                n = R.choice(list)


                sys.stdout.write (f"\r \t\t\t{x}    {y}    {z}    {l}    {m}    {n}")
            time.sleep(.1)
            cou -=1
        new_list =[]
        new_list.append (x)
        new_list.append (y)
        new_list.append (z)
        new_list.append (l)
        new_list.append (m)
        new_list.append (n)


        print ()
        score=[]
        count_x =new_list.count("🍌")
        #print ("x (banana)= " , count_x)
        score.append(count_x)

        count_y =new_list.count("🍒")
        #print ("y (karaz)= " , count_y)
        score.append(count_y)

        count_z =new_list.count("🍋")
        #print ("z (lemon)= " , count_z)
        score.append(count_z)

        count_l =new_list.count("🍉")
        #print ("l (watermelon)= " , count_l)
        score.append(count_l)

        count_m =new_list.count("⭐")
        #print ("m (star)= " , count_m)
        score.append(count_m)

        count_n =new_list.count("❤️")
        #print ("n (hart)= " , count_n)
        score.append(count_n)


        # print (max(score))
        global max_
        max_= score[0]
        location = 0
        for i in range(0,len(list)):
            if score[i] >= max_:
                max_ = score[i]
                location = i
        #print ("location is : ",location)
        #print ("max  is : ", max_)

        def cheq2(number):
            print ("\n\n\t\t\t\t  ",list[location] , "   * ", max_)

            if location== 0:
                #print ("*2")
                return number * 2 
            if location== 1:
                #print ("*4")
                return number * 4
            if location== 2:
                #print ("*6")
                return number * 6 
            if location== 3:
                #print ("*8")
                return number * 8     
            if location== 4:
                #print ("*10")
                return number * 10
            if location== 5:
                #print ("*12")
                return number * 12
            
        def cheq() :
            global max_
            match max_:
                case 0 :
                    return 0
                case 1 :
                    return 1
                case 2:
                    return 4
                case 3 :
                    return 9
                case 4 :
                    return 16
                case 5 :
                    return 25
                case _:
                    print ("not hppend ")

        x = cheq ()
        #print ('the x total is : ' , x )

        #print ("location is : ",location)
        y = cheq2(x)

        print ("\n\n\n\n\t\t\t\t   you have :", y)
        if y> 40 :
            print ("\n\n \t\t\t\t     😁😁😁")
            win = y-40 
            print ("\n\n\t\t\t\t  you win  :  " + str(win) + "  $ ")
            balance += win
            print ("\n\n\t\t\t\tyour balance is : " + str(balance) + " $")
        elif y <=40:
            print ("\n\n \t\t\t\t     🤬🤬🤬")
            print ("\n\n \t\t\t    less than 40 >>> you lose  ")
        print()

        print ("\t\t\t             [y  -  n ]")
        agine = 1
        while agine:
            con= msvcrt.getwch()
            print (con)
            if con == 'n':
                print("\n\nthank you for using my program >>>>>   good bye....\n\n")
                agine = 0
                time.sleep(3)
                exit()
            elif con == 'y':
                agine = 1
                break
            else :
                print ("\n\t\t\t             bad  input")
                time.sleep(1)
        # input_ = msvcrt.getwch()  # أو getch() لو أردت منع طباعة الحرف
        # print(input_)  # لطباعة الحرف إذا استخدمت getwch
        # input_ = Write.Input("\n\n[+]Enter the number : ", Colors.blue_to_green, interval=0.1)
    #     while is_running :
    #         if input_ == '1':       
    #             is_running = False
    #         elif input_ == '2': 
    #             print ("\n\n\t\t\t\t  you have : " + str(balance) + " $")
    #             print ("\n\n\t\t\t\t thank you good bye")
    #             time.sleep(2)   
    #             exit()
    #         else:           
    #             Write.Print ('unkown input \n', Colors.blue_to_green, interval=0.1)
    #             input_ = Write.Input("\n\n[+]Enter the number : ", Colors.blue_to_green, interval=0.1)
    #             is_running = True               
    # else:
    #     Write.Print ('your balance is : ' + str(balance) + ' $', Colors.blue_to_green, interval=0.1)
    #     Write.Print ('\n\n[-] you dont have enough balance to play \n', Colors.purple_to_red, interval=0.1)
    #     print ("thank you good bye")
    #     time.sleep(2)
if __name__ == "__main__":
    start()