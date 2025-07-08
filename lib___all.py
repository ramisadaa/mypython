#lets go 
import os 
os.system('cls')
import time 
st_list = [[1 , 'admad' , False , 0]]
booktuple = tuple()
l_no = 1 
xorder = 0
order_dict = { 
    "order_dict[1]" : {     "stname ":"rami fasil abu sadaa ", 
                            "st_no"  : 1, 
                            "db_name" : "c++", 
                            "db_no " : 150, 
                            "order_time" :"1/1/2000"}
             }
order_library = {}
order__ = 0
def dis_order ():
    os.system ('cls')
    for mk , mv in order_library.items():
        for sk , sv in order_library[mk].items():
            print (sk , "=====>>>" , sv )
        print ("="*30)
def mnue ():
    os.system('cls')
    ## المنيو 
    print ("*"*10 , "welcom to my project ", "*"*10, "\n\n")
    print (" [1] Student \n")
    print (" [2]  Book \n")
    print (" [3] Order \n")
    print (" [4] Query \n")
    print (" [5] Eixt \n")
    # فحص الادخال 
    return()
def main():
    while True :
        mnue()
        x = input ("enter your chowis [1  >>  5] : ")
        if x.isdigit()== True and int(x) >= 1 and int (x) <=5:
            match x:
                case '1' :       # student list 
                    while True :
                        os.system ('cls')
                        print ("*"*10 , "welcom to studant page ", "*"*10, "\n\n")
                        print (" [1] Add Student \n")
                        print (" [2] View Student \n")
                        print (" [3] DEl Student \n")
                        print (" [4] Modefy Student \n")
                        print (" [5] Main \n")
                        sx = input ("enter your chowis [1  >>  5] : ")
                        if sx.isdigit() == True and int(sx) >=1 and int (sx) <=5:
                            os.system ('cls')
                            match sx:
                                case '1' :
                                    l_name = input ("enter your name : ")
                                    if l_name.isalpha()== False  or l_name.isspace() :
                                        print ("bad input ")
                                        input ("Press any key to cont.....")
                                        continue
                                    else :
                                        global l_no
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
                                            else :
                                                print (f" {del_no} name not found in database ")
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
                                case '4':
                                    pass
                                case '5' :
                                    main ()
                
                        else : 
                            print ("bad input ")
                            input ("Press any key to cont.....")
                case '2' :       # book tuple 
                
                    b_no = 1
                    while True :
                        os.system ('cls')
                        print ("*"*10 , "welcom to Books page ", "*"*10, "\n\n")
                        print (" [1] Add Book \n")
                        print (" [2] View Book \n")
                        print (" [3] DEl Book \n")
                        print (" [4] Modefy Book \n")
                        print (" [5] Main  \n")
                        bx = input ("enter your chowis [1  >>  5] : ")
                        if bx.isdigit() == True and int(bx) >= 1 and int (bx) <=5:                      
                            match bx:
                                case '1' :
                                    b_name = input ("enter book name : ")
                                    b_arthor = input ("enter book author : ")
                                    b_date = input ("enter book  date : ")  
                                    booktuple += (b_no , b_name,b_arthor,b_date,)
                                    b_no +=1
                                    print (f"you add : [ {b_no-1} , {b_name} , {b_arthor} , {b_date} ] ")
                                    input ("Press any key to cont.....")
                                case '2' :
                                    counter = 0 
                                    for item in booktuple:
                                        print (item, end= "        ")
                                        counter +=1
                                        if counter%4==0:
                                            print ()
                                    print ()
                                    input ("Press any key to cont.....")
                                case '3' :
                                    s_del = input (" enter book no : ")
                                    for item in booktuple:
                                        if item == s_del:
                                            pass
                                            # ******** كيف نحذف عنصر من التوابل 
                                    print ("3")
                                    input ("Press any key to cont.....")
                                case '4' :
                                    print ("4")
                                    input ("Press any key to cont.....")
                                case '5' :
                                    main()
                        else :
                            print ("bad input ")
                            input ("Press any key to cont.....")
                            continue    
                case '3' :       # order dict
                    
                    while True :
                        os.system('cls')
                        print ('='*10, " wellcome to order screen ", '='*10)
                        more = input  ("do you want add order[Y - N ] or : \n\[5] back to main screen\n\t")
                        if more.lower()=='5': 
                            main ()
                        elif more.lower() == 'n':
                            dis_order ()
                            break 
                        elif more.lower() == 'y':
                            os.system("cls")
                            order__ += 1
                            stname = input ("enter student name : ")
                            st_no = input ("enter student number :  ")
                            db_name = input ("enter book name :  ")
                            db_no = input ("enter book number :  ")
                            order_time = input ("enter the order date  :  ")
                            order_library[order__] ={
                                        "no" : order__  , 
                                        "sname": stname,
                                        "sno": st_no,
                                        "bname": db_name ,
                                        "bno": db_no , 
                                        "odate" : order_time 
                                }
                            os.system ("cls")
                            continue
                        else :
                            print ("bad input ")
                case '4' :
                    print ("4")
                case '5' :
                    print ("you want to exit >>>")
                    print ("bye bye >>>>>")
                    exit () 
                case _ :
                    print (" No No No ")
                    input ("Press any key to cont.....")
        elif x.isalpha() == True :
            print (" char ")
            input ("Press any key to cont.....")
        else : 
            print ("sp char ")
            input ("Press any key to cont.....")

main()



    
