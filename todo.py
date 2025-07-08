import os 
import time
import sys

os.system('cls')

print(                 """
 
                   /$$$$$$$                          /$$
                  | $$__  $$                        |__/
                  | $$  \ $$  /$$$$$$  /$$$$$$/$$$$  /$$
                  | $$$$$$$/ |____  $$| $$_  $$_  $$| $$
                  | $$__  $$  /$$$$$$$| $$ \ $$ \ $$| $$
                  | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$
                  | $$  | $$|  $$$$$$$| $$ | $$ | $$| $$
                  |__/  |__/ \_______/|__/ |__/ |__/|__/
                                      
      
""")

print ("                          wellcom to my project \n")

i = 0 
bar_length = 50
while i<=50 :
    bar = "█" * i + " " * (bar_length - i)
    percent = int((i / bar_length) * 100)

    
    sys.stdout.write (f"\r{bar} {percent}%")
    time.sleep(.1)
    i+=1

mylist = [[1 , 'python' , 'time' , 0]]
#print (mylist)
l_no = 0 
l_name = ""
l_date = ""
i = 0
number_item = 1
while True : 
    os.system('cls')


    print ("****************************")
    
    print (" priss [1] to ADD anew entry \n")
    print (" priss [2] to view entry \n")
    print (" priss [3] to modify entry \n")
    print (" priss [4] to del  entry \n")
    print (" priss [5] to search entry \n")
    print (" priss [6] to exit \n")



    print ("****************************")

    entry1 = int (input ("your choose is  : "))
    match entry1 : 
            case 1 :
                print ("******  WELLCOME TO ADDITON SECREEN ********")
                time.sleep(.5)
                l_name = input("enter your job : ")
                l_date = input("enter your date : ")
                mylist.append ([(len(mylist)+1) , l_name , l_date , 0])
                input ("press any key to continue")
              
            case 2 :
                print ("******  WELLCOME TO VIEW  SECREEN ********")
                
                while (i < len(mylist)) :
                    print (mylist[i])
                    i += 1 
                    time.sleep(.5)
                input ("press any key to continue")
                i = 0
            case 3 :
                print ("******  WELLCOME TO MODEFIY SECREEN ********")
                time.sleep(2)
                os.system('cls')
                print ("****************************")
                print ("****** Your list **********")
                while (i < len(mylist)) :
                    print (mylist[i])
                    i += 1 
                    time.sleep(.5)
                l_no = int (input ("enter the number of entry you want to modify : "))
                print (mylist[l_no-1])

                print ("****************************\n\n")
                print (" priss [N] to change name \n\n")
                print (" priss [D] to change date \n\n")
                print (" priss [S] to change status \n\n")
                print ("****************************")


                entry2 =(input ("your choose is  : "))
                
                match entry2.lower() :
                    case  'n' : 
                        print ("wellcome to change the name  ")
                        x = input ("enter the new name : ")
                        mylist[l_no-1][1] = x 
                    case 'd' :
                        print ("wellcome to change the date  ")
                        x = input ("enter the new date : ")
                        mylist[l_no-1][2] = x 
                    case 's' :
                        print ("wellcome to change the status  ")
                        x = input ("are you done the massion : [y or n] : ")    
                        if x == 'y' :
                            mylist[l_no-1][3] = 1
                        elif x == 'n' :
                            print ("you have to do it ")
                            mylist[l_no-1][3] = 0
                        else :
                            print ("your entry is not valid ")
                            time.sleep(1) 
                    case _ :
                        print ("your entry is not valid ")
                        time.sleep(1)
                time.sleep(.5)
            case 4 :
                time.sleep(.5)
                os.system ('cls')
                print ("******  WELLCOME TO DELET SECREEN ********")
                print ("          *****  what do you want to delet *****  \n\n")
                print (" press [1] to delet one list   \n\n")
                print (" press [2] to delet one list   \n\n")
                print (" press [3] to delet one list   \n\n")
                x = int (input (" enter your choise  :  "))
                if x == 1: 
                    os.system('cls')
                    print ("****************************")
                    print ("****** Your list **********")
                    while (i < len(mylist)) :
                        print (mylist[i])
                        i += 1 
                        time.sleep(.5)
                    l_no = int (input ("enter the number of entry you want to deledt  : "))
                    mylist.pop(l_no-1)
                elif  x == 2:
                    print  ("enter  range   you eant to delet : ")
                    from_no = int (input ("from : "))
                    to_no = int (input (" to : ") )
                    if (to_no) > len(mylist):
                        print ("out of range ")
                        time.sleep(3)
                    else:
                        while to_no >= from_no :
                            mylist.pop (to_no-1)
                            to_no -= 1
                        time.sleep(.5)
                elif x == 3:
                    mylist.clear()
                else :
                    print ("inv input ")
            case 5 :
                os.system ('cls')
                print ("******  WELLCOME TO SEARCH SECREEN ********")
                print ("enter [f] to find job by name  : \n\n")
                print ("enter [c] to count un do jobs : \n\n")
                print ("enter [m] to find job by locaton \n\n")       
                entry4 = input ("enter your chois :    ")
                
                match entry4.lower() :
                    case  'f' :
                        x = input ("Enter your job name : ") 
                        count_ = len(mylist)
                        while count_ > 0 : 
                            temp =  str (mylist[count_-1][1])
                            if temp == x :
                                print ("we find this item : ")
                                print (mylist[count_-1])
                                time.sleep(5)
                            count_ -=1
                    case 'c' :
                        count_ = len(mylist)
                        while count_ > 0 :                   
                            if mylist[count_ - 1][3] == 0 :
                                print (mylist[count_-1])
                                time.sleep(.5)
                            count_ -=1
                        os.system("cls")
                        x = input (" Do you want to display the compleat job : [y or n ]")
                        if x == 'y':
                            count_ = len(mylist)
                            while count_ > 0 :                   
                                if mylist[count_ - 1][3] == 1 :
                                    print (mylist[count_-1])
                                    time.sleep(.5)
                                count_ -=1
                        else: 
                            break
                        time.sleep(2)
                    case 'm' :
                        print ('m')
                        x =int ( input ("Enter your job location  : "))
                        print (mylist[x-1]) 
                        time.sleep(2)
                    case _ :
                        print ("else")
                        time.sleep(2)
                
            case 6 :
                os.system ('cls')
                print ("******  WELLCOME TO EIXT SECREEN ********")
                time.sleep(.5)
                print ("goodbye my frind")
                #print (mylist)
                exit()
            case _ :
                print ("your entry is not valid ")
                time.sleep(1)
    i = 0