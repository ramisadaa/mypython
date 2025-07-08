# أهلا وسهلا بكم في الكود البرمجي  
"""
هذا الملف يحتوي على العديد من الامثلة الخاصة بلغة بايثون 
والتي تم تصميمها اعتمادا على فيديوهات راكوان 
وبعض الفيديوهات الاخرى 
مع تطوير بعض البرامج بما يناسب حالتي التعليمية 

"""

from pystyle import *
import time
import os
import sys
import getpass
import bank
import spinning
import tashfer
import kalemat
import winning

os.system("cls")
sys.stdout.write('\033[0m')
class res():
    @staticmethod
    def clar_res():
        os.system("cls")
        sys.stdout.write('\033[0m')
        formatted_time = time.strftime("%d/%m/%Y - %I:%M:%S %p")
        print("*" * 20, formatted_time, "*" * 20)

class Town():
    coun = 0

    def __init__(self,country, town,longitude ,latitude):
        self.country = country
        self.town = town
        self.longitude = longitude
        self.latitude = latitude
        Town.coun +=1


def load():
    Write.Print("\t\t\t\t loading", Colors.black , interval=.01)
    print()
    Write.Print("          █████████████████████████████████████████████████       ", Colors.blue_to_purple, interval=.1)
    print()
    res.clar_res()

def arab(text):# الكتابة باللغة العربية في التيرمنال  
    import arabic_reshaper
    from bidi.algorithm import get_display
    text1 =  arabic_reshaper.reshape (text)
    text1 = get_display (text1)
    return(text1)

def sign_in_1():
    res.clar_res()
    print (Box.DoubleCube ('Example [1] ') )
    print (Box.Lines (' [+] sing in program username & password ') )
    Write.Print ('[-] this program for login page \n', Colors.purple_to_red, interval=0.1)
    Write.Print ('[-] write username and password \n\n', Colors.purple_to_red, interval=0.1)
    
    while True :
        username = Write. Input ('- write username : ', Colors.blue_to_green, interval=0.1)
        # password = Write. Input ('- write password : ', Colors.blue_to_green, interval=0.1)
        password = getpass.getpass("enter pass :" ) # هذا الكود لاخفاء ادخال المستخدمين  

        if username.lower() == 'rami' and password == '123456' :
            Write.Print (' [+] Welcome admin \n',Colors.green, interval=0.2)
            input ('press any key to exit ... ')
            break
        else :
            Write.Print (' [-] Error Try Again \n\n',Colors.red, interval=0.2)

def calculator_2():
    res.clar_res()
    print (Box.DoubleCube ('Example [2] ') )
    print (Box.Lines (' [+] calculator program  ') )
    Write.Print ('[-] this program for calculator numbers  \n', Colors.purple_to_red, interval=0.1)
    while True:

        number1 = int (Write.Input("[+]Enter the 1st number : ", Colors.blue_to_green, interval=0.1))
        opration =  Write.Input("Enter the opration : ", Colors.black_to_white, interval= 0.2)
        number2 = int (Write.Input("[+]Enter the 2nd number : ", Colors.blue_to_green, interval=0.1))
        if opration == '+' :
            total = number1 + number2
            print (f"{number1}{opration}{number2} = {total}")
        elif opration == '-' :
            total = number1 - number2
            print (f"{number1}{opration}{number2} = {total}")
        elif opration == '*' :
            total = number1 * number2
            print (f"{number1}{opration}{number2} = {total}")
        elif opration == '/' :
            total = number1 / number2
            print (f"{number1}{opration}{number2} = {total}")
        elif opration == '!' :
            break
        else :
            Write.Print ('unkown oppartion \n',Colors.blue_to_green ,interval=0.1)
        input("press any key ..... ")
        calculator_2()
    print ("thank you good bye")

def mult_3():
    res.clar_res()
    print (Box.DoubleCube ('Example [3] ') )
    print (Box.Lines (' [+] mult table program  ') )
    Write.Print ('[-] this program for mult table numbers  \n', Colors.purple_to_red, interval=0.1)
    Write.Print ('[1] all multiplcation tabels  \n', Colors.purple_to_red, interval=0.1)
    Write.Print ('[2] one table  \n', Colors.purple_to_red, interval=0.1)
    Write.Print ('[3] mini tuble  \n', Colors.purple_to_red, interval=0.1)
    Write.Print ('[4] exit  \n', Colors.purple_to_red, interval=0.1)

    number = int (Write.Input("\n\n[+]Enter the number : ", Colors.blue_to_green, interval=0.1))
    match number:
        case 1:
            for i in range(1, 13):
                for j in range(1, 13):
                    total = i * j
                    print(f"{i} * {j} = {total}")
                print ("-" * 20)
        case 2:
            number = int (Write.Input("\n[+]Enter the number : ", Colors.blue_to_green, interval=0.1))
            for i in range(1, 13):
                total = number * i
                print(f"{number} * {i} = {total}")
        case 3:
            counter = 1 
            for i in range(1, 11):
                for j in range(i, 13):
                    print (f"{counter} >>>   {i} * {j} = {i * j}")
                    counter += 1    

        case 4:
            sys.exit()
        case _:
            Write.Print ('[-] Error: Invalid choice \n', Colors.red, interval=0.2)
    input("press any key ..... ")

def short_url_4(): # تقصير الروابط  ويجب توفر انترنت 
    res.clar_res()
    import pyshorteners as pyshort
    print (Box.DoubleCube ('Example [4] ') )
    print (Box.Lines (' [+] short Url  ') )
    Write.Print ('[-] this program for make short url \n', Colors.purple_to_red, interval=0.1)
    url = Write. Input ('- write url : ', Colors.blue_to_green, interval=0.1)
    sh = pyshort.Shortener()
    print (sh.tinyurl.short(url))
    input ('\npress any key to exit ... ')

def speed_test_5(): # فحص سرعة الانترنت ويجب توفر انترنت
    res.clar_res()

    # pip install speedtest-cli
    import speedtest
    print (Box. DoubleCube ('Example [5] ') )
    print (Box. Lines ('[+]speed test ') )
    Write. Print ('[-] this program for speed net \n', Colors.purple_to_red, interval = 0.1)

    st = speedtest.Speedtest ()
    dst = st.download ()
    ust = st.upload ()
    d = round (dst / (10 ** 3),2)
    u = round (ust / (10 ** 3),2)
    st_ = round (st / (10 ** 3),2 )
    print (f"[-] Download speed is : {d} Kbit/s" )
    print (f"[-] Upload speed is : {u} Kbit/s" )

    Write. Print(' [-] Genral net speed is : \n',Colors.green, interval=0.1)
    print (f"[-] Genral net speed is : {st_} Kbit/s" )

def distance_6(): # حساب المسفات بين المدن 
    # pip install geopy
    res.clar_res()
    gaza_ = Town("palestine", "gaza", 34.4560, 31.5033)
    khan_yunis_= Town("palestine", "khan_yunis", 34.3040, 31.3400)
    rafah_ = Town("palestine", "rafah", 34.2400, 31.2870)
    deir_al_balah_ = Town("palestine", "deir_al_balah"  , 34.3500, 31.4170)
    jabalia_ = Town("palestine", "jabalia", 34.4830, 31.5380)
    nablus_ = Town("palestine", "nablus" , 35.2610, 32.2220)
    ramallah_ = Town("palestine", "ramallah", 35.2050, 31.8996)
    jericho_ = Town("palestine", "jericho", 35.4599, 31.8530)
    jerusalem_ = Town("palestine", "jerusalem", 35.2200, 31.7784)
    hebron_ = Town("palestine", "hebron", 35.0950, 31.5326)
    bethlehem_ = Town("palestine", "bethlehem", 35.2043, 31.7054)
    qalqilya_ = Town("palestine", "qalqilya", 34.9722, 32.1897)
    tulkarm_ = Town("palestine", "tulkarm", 35.0150, 32.3116)
    jenin_ = Town("palestine", "jenin", 35.2995, 32.4637)
    salfit_ = Town("palestine", "salfit", 35.1722, 32.0791)
    tubas_ = Town("palestine", "tubas", 35.5503, 32.3202)
    
    # تعريف مدن أمريكية مع بيانات خطوط الطول والعرض
    cairo_ = Town("egypt", "cairo", 31.2357, 30.0444)
    alexandria_ = Town("egypt", "alexandria", 29.9187, 31.2001)
    giza_ = Town("egypt", "giza", 31.1313, 30.0131)
    port_said_ = Town("egypt", "port_said", 32.3100, 31.2653)
    suez_ = Town("egypt", "suez", 32.5530, 29.9737)
    ismailia_ = Town("egypt", "ismailia", 32.2715, 30.5852)
    mansoura_ = Town("egypt", "mansoura", 31.3795, 31.0419)
    tanta_ = Town("egypt", "tanta", 30.9990, 30.7865)
    zagazig_ =Town("egypt", "zagazig", 31.5020, 30.5877)
    asyut_ = Town("egypt", "asyut", 31.1809, 27.1809)
    sohag_ = Town("egypt", "sohag", 31.7000, 26.5500)
    qena_=Town("egypt", "qena", 32.7160, 26.1550)
    luxor_ = Town("egypt", "luxor", 32.6396, 25.6872)
    aswan_ = Town("egypt", "aswan", 32.8998, 24.0889)
    fayoum_=Town("egypt", "fayoum", 30.8500, 29.3084)
    beni_suef_= Town("egypt", "beni_suef", 31.1000, 29.0661)
    minya_ =Town ("egypt", "minya", 30.7503, 28.1099)
    
    # تعريف مدن أمريكية مع بيانات خطوط الطول والعرض
    new_york_ = Town("usa", "new_york", 74.0060, 40.7128)
    los_angeles_ = Town("usa", "los_angeles", 118.2437, 34.0522)
    chicago_ = Town("usa", "chicago", 87.6298, 41.8781)
    houston_ = Town("usa", "houston", 95.3698, 29.7604)
    phoenix_ = Town("usa", "phoenix", 112.0740, 33.4484)
    philadelphia_ = Town("usa", "philadelphia", 75.1652, 39.9526)
    san_antonio_ = Town("usa", "san_antonio", 98.4936, 29.4241)
    san_diego_ = Town("usa", "san_diego", 117.1611, 32.7157)
    dallas_ = Town("usa", "dallas", 96.7970, 32.7767)
    san_jose_ = Town("usa", "san_jose", 121.8863, 37.3382)
    print("-"*70)
    from geopy.distance import geodesic

    print (Box.DoubleCube ('Example [6] ') )
    print (Box.Lines (' [+] Distance ') )
    Write.Print ('[-] this program for calc the distance between cities \n', Colors.purple_to_red, interval=0.1)
    Write.Print (f'[-] you have {Town.coun} \n\n', Colors.purple_to_red, interval=0.1)
    Write.Print ('[+] country list....... \n\n', Colors.purple_to_red, interval=0.1)
    Write.Print ('   [-] Palestine  \n\n', Colors.purple_to_red, interval=0.1)
    Write.Print ('   [-] Eygpt \n\n', Colors.purple_to_red, interval=0.1)
    Write.Print ('   [-] USA \n\n', Colors.purple_to_red, interval=0.1)
    c_input =input("enter the country : [P / E / USA] :  ")

    is_running = True
    res.clar_res()
    match c_input :
        case 'p' :
            while is_running :
                res.clar_res()
                print ("-"*70)
                print ("[1]: gaza ")
                print ("[2]: khan_yunis ")
                print ("[3]: rafah ")
                print ("[4]: deir_al_balah ")
                print ("[5]: jabalia ")
                print ("[6]: nablus ")
                print ("[7]: ramallah ")
                print ("[8]: jericho ")
                print ("[9]: jerusalem ")
                print ("[10]: hebron ")
                print ("[11]: bethlehem ")
                print ("[12]: qalqilya ")
                print ("[13]: tulkarm ")
                print ("[14]: jenin ")
                print ("[15]: salfit ")
                print ("[16]: tubas ")

                print ("-"*70)
                first_choice = int (Write.Input("Enter the first city number  : ", Colors.blue_to_green, interval=0.1))
                second_choice =int (Write.Input("Enter the second city number : ", Colors.blue_to_green, interval=0.1))
                if first_choice == second_choice :
                    print ("you must choise deferant citeis ")
                else :
                    if first_choice == 1:
                        first_place = (gaza_.longitude , gaza_.latitude)
                        first_town =  gaza_.town
                    elif first_choice == 2:
                        first_place = (khan_yunis_.longitude , khan_yunis_.latitude)
                        first_town =  khan_yunis_.town
                    elif first_choice == 3:
                        first_place = (rafah_.longitude , rafah_.latitude)
                        first_town =  rafah_.town
                    elif first_choice == 4:
                        first_place = (deir_al_balah_.longitude , deir_al_balah_.latitude)
                        first_town =  deir_al_balah_.town
                    elif first_choice == 5:
                        first_place = (jabalia_.longitude , jabalia_.latitude)
                        first_town =  jabalia_.town
                    elif first_choice == 6:
                        first_place = (nablus_.longitude , nablus_.latitude)
                        first_town =  nablus_.town
                    elif first_choice == 7:
                        first_place = (ramallah_.longitude , ramallah_.latitude)
                        first_town =  ramallah_.town
                    elif first_choice == 8:
                        first_place = (jericho_.longitude , jericho_.latitude)
                        first_town =  jericho_.town
                    elif first_choice == 9:
                        first_place = (jerusalem_.longitude , jerusalem_.latitude)
                        first_town =  jerusalem_.town
                    elif first_choice == 10:
                        first_place = (hebron_.longitude , hebron_.latitude)
                        first_town =  hebron_.town
                    elif first_choice == 11:
                        first_place = (bethlehem_.longitude , bethlehem_.latitude)
                    elif first_choice ==12:
                        first_place = (qalqilya_.longitude , qalqilya_.latitude)
                        first_town =  qalqilya_.town
                    elif first_choice == 13:
                        first_place = (tulkarm_.longitude , tulkarm_.latitude)
                        first_town =  tulkarm_.town
                    elif first_choice == 14:
                        first_place = (jenin_.longitude , jenin_.latitude)
                        first_town =  jenin_.town
                    elif first_choice == 15:
                        first_place = (salfit_.longitude , salfit_.latitude)
                        first_town =  salfit_.town
                    elif first_choice == 16:
                        first_place = (tubas_.longitude , tubas_.latitude)
                        first_town =  tubas_.town
                    else:
                        Write.Print ('[-] Error: Invalid choice \n', Colors.red, interval=0.2)

                    if second_choice == 1:
                        second_place = (gaza_.longitude , gaza_.latitude)
                        second_town =  gaza_.town
                    elif second_choice == 2:
                        second_place = (khan_yunis_.longitude , khan_yunis_.latitude)
                        second_town = khan_yunis_.town
                    elif second_choice == 3:
                        second_place = (rafah_.longitude , rafah_.latitude)
                        second_town = rafah_.town
                    elif second_choice == 4:
                        second_place = (deir_al_balah_.longitude , deir_al_balah_.latitude)
                        second_town = deir_al_balah_.town
                    elif second_choice == 5:
                        second_place = (jabalia_.longitude , jabalia_.latitude)
                        second_town = jabalia_.town
                    elif second_choice == 6:
                        second_place = (nablus_.longitude , nablus_.latitude)
                        second_town = nablus_.town
                    elif second_choice == 7:
                        second_place = (ramallah_.longitude , ramallah_.latitude)
                        second_town = ramallah_.town
                    elif second_choice == 8:
                        second_place = (jericho_.longitude , jericho_.latitude)
                        second_town = jericho_.town
                    elif second_choice == 9:
                        second_place = (jerusalem_.longitude , jerusalem_.latitude)
                        second_town = jerusalem_.town
                    elif second_choice == 10:
                        second_place = (hebron_.longitude , hebron_.latitude)
                        second_town = hebron_.town
                    elif second_choice == 11:
                        second_place = (bethlehem_.longitude , bethlehem_.latitude)
                        second_town = bethlehem_.town
                    elif second_choice ==12:
                        second_place = (qalqilya_.longitude , qalqilya_.latitude)
                        second_town = qalqilya_.town
                    elif second_choice == 13:
                        second_place = (tulkarm_.longitude , tulkarm_.latitude)
                        second_town = tulkarm_.town
                    elif second_choice == 14:
                        second_place = (jenin_.longitude , jenin_.latitude)
                        second_town =  jenin_.town
                    elif second_choice == 15:
                        second_place = (salfit_.longitude , salfit_.latitude)
                        second_town =  salfit_.town
                    elif second_choice == 16:
                        second_place = (tubas_.longitude , tubas_.latitude)
                        second_town =  tubas_.town
                    else:
                        Write.Print ('[-] Error: Invalid choice \n', Colors.red, interval=0.2)
                    print ("-"*70)
                    print ("-"*70)
                    sys.stdout.write('\033[0m')

                    dis = int (geodesic(first_place, second_place) .km)
                    print ("The first city is  : " , first_town)
                    print ("The second city is : ", second_town)
                    print(f"The distance between {first_town} and {second_town} >>>   {dis}  km")
                    
                    
                    print ("-"*70)
                con= (Write.Input("        Do you want to continue ? [y/n] ", Colors.blue_to_green, interval=0.1))
                if con == 'n':
                    is_running = False
                    print("good bye....")
                elif con == 'y':
                    is_running = True
                else :
                    print ("bad input")
                    time.sleep(3)
        case 'e':    
            while is_running:
                res.clar_res()
                print("-" * 70)
                print("[1]: cairo ")
                print("[2]: alexandria ")
                print("[3]: giza ")
                print("[4]: port_said ")
                print("[5]: suez ")
                print("[6]: ismailia ")
                print("[7]: mansoura ")
                print("[8]: tanta ")
                print("[9]: zagazig ")
                print("[10]: asyut ")
                print("[11]: sohag ")
                print("[12]: qena ")
                print("[13]: luxor ")
                print("[14]: aswan ")
                print("[15]: fayoum ")
                print("[16]: beni_suef ")
                print("[17]: minya ")
                print("-" * 70)
                first_choice = int(Write.Input("Enter the first city number  : ", Colors.blue_to_green, interval=0.1))
                second_choice = int(Write.Input("Enter the second city number : ", Colors.blue_to_green, interval=0.1))
                if first_choice == second_choice:
                    print("you must choise deferant citeis ")
                else:
                    if first_choice == 1:
                        first_place = (cairo_.longitude, cairo_.latitude)
                        first_town = cairo_.town
                    elif first_choice == 2:
                        first_place = (alexandria_.longitude, alexandria_.latitude)
                        first_town = alexandria_.town
                    elif first_choice == 3:
                        first_place = (giza_.longitude, giza_.latitude)
                        first_town = giza_.town
                    elif first_choice == 4:
                        first_place = (port_said_.longitude, port_said_.latitude)
                        first_town = port_said_.town
                    elif first_choice == 5:
                        first_place = (suez_.longitude, suez_.latitude)
                        first_town = suez_.town
                    elif first_choice == 6:
                        first_place = (ismailia_.longitude, ismailia_.latitude)
                        first_town = ismailia_.town
                    elif first_choice == 7:
                        first_place = (mansoura_.longitude, mansoura_.latitude)
                        first_town = mansoura_.town
                    elif first_choice == 8:
                        first_place = (tanta_.longitude, tanta_.latitude)
                        first_town = tanta_.town
                    elif first_choice == 9:
                        first_place = (zagazig_.longitude, zagazig_.latitude)
                        first_town = zagazig_.town
                    elif first_choice == 10:
                        first_place = (asyut_.longitude, asyut_.latitude)
                        first_town = asyut_.town
                    elif first_choice == 11:
                        first_place = (sohag_.longitude, sohag_.latitude)
                        first_town = sohag_.town
                    elif first_choice == 12:
                        first_place = (qena_.longitude, qena_.latitude)
                        first_town = qena_.town
                    elif first_choice == 13:
                        first_place = (luxor_.longitude, luxor_.latitude)
                        first_town = luxor_.town
                    elif first_choice == 14:
                        first_place = (aswan_.longitude, aswan_.latitude)
                        first_town = aswan_.town
                    elif first_choice == 15:
                        first_place = (fayoum_.longitude, fayoum_.latitude)
                        first_town = fayoum_.town
                    elif first_choice == 16:
                        first_place = (beni_suef_.longitude, beni_suef_.latitude)
                        first_town = beni_suef_.town
                    elif first_choice == 17:
                        first_place = (minya_.longitude, minya_.latitude)
                        first_town = minya_.town
                    else:
                        Write.Print('[-] Error: Invalid choice \n', Colors.red, interval=0.2)

                    if second_choice == 1:
                        second_place = (cairo_.longitude, cairo_.latitude)
                        second_town = cairo_.town
                    elif second_choice == 2:
                        second_place = (alexandria_.longitude, alexandria_.latitude)
                        second_town = alexandria_.town
                    elif second_choice == 3:
                        second_place = (giza_.longitude, giza_.latitude)
                        second_town = giza_.town
                    elif second_choice == 4:
                        second_place = (port_said_.longitude, port_said_.latitude)
                        second_town = port_said_.town
                    elif second_choice == 5:
                        second_place = (suez_.longitude, suez_.latitude)
                        second_town = suez_.town
                    elif second_choice == 6:
                        second_place = (ismailia_.longitude, ismailia_.latitude)
                        second_town = ismailia_.town
                    elif second_choice == 7:
                        second_place = (mansoura_.longitude, mansoura_.latitude)
                        second_town = mansoura_.town
                    elif second_choice == 8:
                        second_place = (tanta_.longitude, tanta_.latitude)
                        second_town = tanta_.town
                    elif second_choice == 9:
                        second_place = (zagazig_.longitude, zagazig_.latitude)
                        second_town = zagazig_.town
                    elif second_choice == 10:
                        second_place = (asyut_.longitude, asyut_.latitude)
                        second_town = asyut_.town
                    elif second_choice == 11:
                        second_place = (sohag_.longitude, sohag_.latitude)
                        second_town = sohag_.town
                    elif second_choice == 12:
                        second_place = (qena_.longitude, qena_.latitude)
                        second_town = qena_.town
                    elif second_choice == 13:
                        second_place = (luxor_.longitude, luxor_.latitude)
                        second_town = luxor_.town
                    elif second_choice == 14:
                        second_place = (aswan_.longitude, aswan_.latitude)
                        second_town = aswan_.town
                    elif second_choice == 15:
                        second_place = (fayoum_.longitude, fayoum_.latitude)
                        second_town = fayoum_.town
                    elif second_choice == 16:
                        second_place = (beni_suef_.longitude, beni_suef_.latitude)
                        second_town = beni_suef_.town
                    elif second_choice == 17:
                        second_place = (minya_.longitude, minya_.latitude)
                        second_town = minya_.town
                    else:
                        Write.Print('[-] Error: Invalid choice \n', Colors.red, interval=0.2)
                    print("-" * 70)
                    print("-" * 70)
                    sys.stdout.write('\033[0m')

                    dis = int (geodesic(first_place, second_place) .km)
                    print ("The first city is  : " , first_town)
                    print ("The second city is : ", second_town)
                    print(f"The distance between {first_town} and {second_town} >>>   {dis}  km")
                con= (Write.Input("        Do you want to continue ? [y/n] ", Colors.blue_to_green, interval=0.1))
                if con == 'n':
                    is_running = False
                    print("good bye....")
                elif con == 'y':
                    is_running = True
                else :
                    print ("bad input")
                    time.sleep(3)
        case 'usa':
            is_running = True
            res.clar_res()
            while is_running:
                res.clar_res()
                print("-" * 70)
                print("[1]: new_york ")
                print("[2]: los_angeles ")
                print("[3]: chicago ")
                print("[4]: houston ")
                print("[5]: phoenix ")
                print("[6]: philadelphia ")
                print("[7]: san_antonio ")
                print("[8]: san_diego ")
                print("[9]: dallas ")
                print("[10]: san_jose ")
                print("-" * 70)
                first_choice = int(Write.Input("Enter the first city number  : ", Colors.blue_to_green, interval=0.1))
                second_choice = int(Write.Input("Enter the second city number : ", Colors.blue_to_green, interval=0.1))
                if first_choice == second_choice:
                    print("you must choise deferant citeis ")
                else:
                    if first_choice == 1:
                        first_place = (new_york_.longitude, new_york_.latitude)
                        first_town = new_york_.town
                    elif first_choice == 2:
                        first_place = (los_angeles_.longitude, los_angeles_.latitude)
                        first_town = los_angeles_.town
                    elif first_choice == 3:
                        first_place = (chicago_.longitude, chicago_.latitude)
                        first_town = chicago_.town
                    elif first_choice == 4:
                        first_place = (houston_.longitude, houston_.latitude)
                        first_town = houston_.town
                    elif first_choice == 5:
                        first_place = (phoenix_.longitude, phoenix_.latitude)
                        first_town = phoenix_.town
                    elif first_choice == 6:
                        first_place = (philadelphia_.longitude, philadelphia_.latitude)
                        first_town = philadelphia_.town
                    elif first_choice == 7:
                        first_place = (san_antonio_.longitude, san_antonio_.latitude)
                        first_town = san_antonio_.town
                    elif first_choice == 8:
                        first_place = (san_diego_.longitude, san_diego_.latitude)
                        first_town = san_diego_.town
                    elif first_choice == 9:
                        first_place = (dallas_.longitude, dallas_.latitude)
                        first_town = dallas_.town
                    elif first_choice == 10:
                        first_place = (san_jose_.longitude, san_jose_.latitude)
                        first_town = san_jose_.town
                    else:
                        Write.Print ('[-] Error: Invalid choice \n', Colors.red, interval=0.2)
                    
                    if second_choice == 1:
                        second_place = (new_york_.longitude, new_york_.latitude)
                        second_town = new_york_.town
                    elif second_choice == 2:
                        second_place = (los_angeles_.longitude, los_angeles_.latitude)
                        second_town = los_angeles_.town
                    elif second_choice == 3:
                        second_place = (chicago_.longitude, chicago_.latitude)
                        second_town = chicago_.town 
                    elif second_choice == 4:
                        second_place = (houston_.longitude, houston_.latitude)
                        second_town = houston_.town
                    elif second_choice == 5:
                        second_place = (phoenix_.longitude, phoenix_.latitude)
                        second_town = phoenix_.town
                    elif second_choice == 6:
                        second_place = (philadelphia_.longitude, philadelphia_.latitude)
                        second_town = philadelphia_.town
                    elif second_choice == 7:
                        second_place = (san_antonio_.longitude, san_antonio_.latitude)
                        second_town = san_antonio_.town
                    elif second_choice == 8:
                        second_place = (san_diego_.longitude, san_diego_.latitude)
                        second_town = san_diego_.town
                    elif second_choice == 9:
                        second_place = (dallas_.longitude, dallas_.latitude)
                        second_town = dallas_.town
                    elif second_choice == 10:
                        second_place = (san_jose_.longitude, san_jose_.latitude)
                        second_town = san_jose_.town
                    else:
                        Write.Print ('[-] Error: Invalid choice \n', Colors.red, interval=0.2)
                    print("-" * 70)
                    print("-" * 70)
                    sys.stdout.write('\033[0m')

                    dis = int (geodesic(first_place, second_place) .km)
                    print ("The first city is  : " , first_town)
                    print ("The second city is : ", second_town)
                    print(f"The distance between {first_town} and {second_town} >>>   {dis}  km")
                con= (Write.Input("        Do you want to continue ? [y/n] ", Colors.blue_to_green, interval=0.1))
                if con == 'n':
                    is_running = False
                    print("good bye....")
                elif con == 'y':
                    is_running = True
                else :
                    print ("bad input")
                    time.sleep(3)
            
def myAge_7():# برنامج لحساب العمر 
    import datetime
    res.clar_res()
    print (Box.DoubleCube ('Example [7] ') )
    print (Box.Lines (' [+] My Age ') )
    Write.Print ('[-] This program for calc an Age  \n', Colors.purple_to_red, interval=0.1)
    s = Write.Input("[-] Enter your birthday [yyyy - m - d] :  " , Colors.purple_to_red, interval = 0.1)
    
    to_d = (str(datetime.datetime.now()).replace(" ","-").replace("/","-").replace(":","-").replace(".","-"))
    to_d = to_d.split('-')
    s = s.split ('-')

    yy_b = int (s[0])
    mm_b = int (s[1])
    dd_b = int (s[2])
    yy_t = int (to_d[0])
    mm_t = int (to_d[1])
    dd_t = int (to_d[2])
    yy_n = 0
    mm_n = 0
    dd_n = 0

    Write.Print ( f"\n\nToday Is >>>>          {dd_t}  / {mm_t}  /  {yy_t}\n\n" , Colors.purple_to_red, interval=0.1)
    Write.Print ( f"Yours birthday Is >>>  {dd_b}  / {mm_b}  /  {yy_b}\n\n" , Colors.purple_to_red, interval=0.1)

    Write.Print ("------------------------------------------\n", Colors.purple_to_red, interval=0.1)
    print ()
    if (yy_b> yy_t):
        print ("wrong date ")
    elif (yy_b == yy_t) & (mm_b > mm_t):
        print ("wrong date ")
    elif ( mm_b == mm_t) & (dd_b > dd_t):
        print ("wrong date ")
    else :
        if (dd_t>= dd_b) :
            dd_n = dd_t - dd_b
        else :
            dd_n =  (dd_t+30 ) - dd_b
            mm_t-=1 
        if (mm_t>= mm_b) :
            mm_n = mm_t - mm_b
        else :
            mm_n = (mm_t+12) -mm_b
            yy_t -=1
        
        yy_n = yy_t - yy_b 
        # print (f"{dd_n}   {mm_n}   {yy_n}")
        print (f"your age is {yy_n} years , {mm_n} month and {dd_n} days \n\n\n")

def Dictinary_8(): # قاموس
    res.clar_res()
    import json
    print (Box.DoubleCube ('Example [8] ') )
    print (Box.Lines (' [+] My Dictinary ') )
    Write.Print ('[-] This program for translate word  ', Colors.purple_to_red, interval=0.1)
    time.sleep(3)
    is_running = True
    while is_running:
        res.clar_res()
        word = Write.Input("[-] Enter The word to translate  :   " , Colors.purple_to_red, interval = 0.1)
        f = open('C:\\python program\\.vscode\\python\\filesys\\english.json','r',encoding='utf-8')
        learn = json.load(f)
        for o in learn :
                if o['english'] == word :
                    tran = arab(o['arabic'])
                    Write.Print (f'[-] the translae is : {tran}  ', Colors.purple_to_red, interval=0.1)
                    break   

    
        input ("\npress any key to cont......")
        while True :

            con= (Write.Input("        Do you want to continue ? [y/n] ", Colors.blue_to_green, interval=0.1))
            if con == 'n':
                is_running = False
                print("thank you for using my program >>>>>   good bye....")
                break
            elif con == 'y':
                is_running = True
                break
            else :
                print ("\t\t\tbad input")
                time.sleep(3)
                continue



def mycalendar():   # التقويم 100
    # calendar هنا قمنا بتضمين كل محتوى الموديول
    import calendar
    res.clar_res()

    x= int (input("Enter the year to review the calender (e.g., 2018): "))
    print (Box.Lines('calendar of the year '+ str(x) + ' '  ))
    calendar.prcal(x)


os.system('cls')
#load()
print ("*"*50)
print ("*"*50)

print ("Example [001] : Sign_in ", arab("تسجيل الدخول"))   
print ("Example [002] : Calculator ", arab("الالة الحاسبة"))   
print ("Example [003] : Multiplication table ", arab("جدول الضرب"))
print ("Example [004] : Short URL ", arab("تقصير الروابط"))
print ("Example [005] : Speed Test ", arab("اختبار سرعة الانترنت"))
print ("Example [006] : Distance between town ", arab("المسافات بين المدن"))
print ("Example [007] : My Age ", arab("برنامج حساب عمر المستخدمين "))
print ("Example [008] : My Dictinary ", arab("المترجم الفوري "))


print ("-"*50)
print ("Examle  [095] :   winning", arab("  alnard ")) 
print ("Examle  [096] : kalemat krash  ", arab(" كلمات كراش ")) 
print ("Examle  [097] : encrypt / decrypt ", arab("تشفير النصوص ")) 
print ("Examle  [098] : start game ", arab(" لعبة الروليت "))
print ("Example [099] : bank        ", arab ("بنك فلسطين "))
print ("Example [100] : My Calendar ", arab("تقويم السنة"))

print("\n\n")
x= int(Write.Input("  Enter the number of your choice: ", Colors.red_to_purple, interval=0.1))
if x== 1 :
    sign_in_1()
elif x == 2:
    calculator_2()
elif x == 3:
    mult_3()  
elif x == 4:   
    short_url_4()
elif x == 5:
    speed_test_5()
elif x == 6:
    distance_6()
elif x== 7 :
    myAge_7()
elif x== 8:
    Dictinary_8()



elif x == 100:
    mycalendar()
elif x == 99:
    res.clar_res()
    bank.main()
elif x == 98:
  res.clar_res()
  spinning.start()
elif x == 97 :
    res.clar_res()
    tashfer.main()
elif x == 96 : # لعبة الحروف 
    res.clar_res()
    kalemat.start()
elif x== 95: # حجر النرد
    res.clar_res()
    winning.game()
       