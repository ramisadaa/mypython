#lets go 
import os 
os.system('cls')
import time 

st_list = [[1 , 'admad' , False , 0]]
l_no = 1 
while True :
    os.system('cls')
    ## المنيو 
    print ("*"*10 , "welcom to my project ", "*"*10, "\n\n")
    print (" [1] Student \n")
    print (" [2]  Book \n")
    print (" [3] Order \n")
    print (" [4] Query \n")
    print (" [5] Eixt \n")
    # فحص الادخال 
    x = input ("enter your chowis [1  >>  5] : ")
    if x.isdigit()== True :
        print ("welc")
        match x:
            case '1' :
                while True :
                    os.system ('cls')
                    print ("*"*10 , "welcom to studant page ", "*"*10, "\n\n")
                    print (" [1] Add Student \n")
                    print (" [2] View Student \n")
                    print (" [3] DEl Student \n")
                    print (" [4] Modefy Student \n")
                    print (" [5] Eixt \n")
                    sx = input ("enter your chowis [1  >>  5] : ")
                    if sx.isdigit() == True and int(sx) >=1 and int (sx) <=5:
                        os.system ('cls')
                        match sx:
                            case '1' :
                                l_name = input ("enter your name : ")
                                l_no += 1 
                                st_list.append([l_no , l_name , False , 0])
                                print ("you add new student : ", st_list[-1])
                                input ("Press any key to cont.....")
                            case '2' :
                                print (f"your have {len(st_list)}  student : ")
                                for i in st_list :
                                    print (i)
                                input ("Press any key to cont.....")
                            case '3' :
                                print ("you can del student by number or name \n\n ")
                                print ( " priss [n] to del by Number \n")
                                print ( " priss [m] to del by naMe \n")
                                del_choice = input ("enter your choice : ")
                                if del_choice == 'n' :
                                    del_no = int (input ("enter student number : "))
                                    i = len(st_list)
                                    
                                    while  i >0 :
                                        i -= 1
                                        if st_list[i][0] == del_no :
                                            st_list.pop(i)
                                            print ("you del student : ", del_no)
                                            break
                                    else:
                                        print ("student not found")
                                        input ("Press any key to cont.....")
          
                                elif del_choice == 'm' :        
                                    del_name = input ("enter student name : ")  
                                    found = False
                                    for i in range(len(st_list)):
                                        if st_list[i][1] == del_name:
                                            found = True
                                            st_list.pop(i)
                                            print ("you del student : ", del_name)
                                            break
                                else :
                                    print ("bad input ")
                                    input ("Press any key to cont.....")

                    else : 
                        print ("bad input ")
                        input ("Press any key to cont.....")
            case '2' :
                print ("2")
            case '3' :
                print ("3")
            case '4' :
                print ("4")
            case '5' :
                print ("5")
                break
            case _ :
                print (" No No No ")
        input ("Press any key to cont.....")
    elif x.isalpha() == True :
        print (" char ")
        input ("Press any key to cont.....")
    else : 
        print ("sp char ")
        input ("Press any key to cont.....")




