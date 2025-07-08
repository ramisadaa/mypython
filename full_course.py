"""
هذا الملف يعتبر مرجعا في التعلم لكل الامثلة الواردة في ملف كو
في الفيديو التعليمي باللغة الانجليزية 
مع تطابقها مع كتيب المادة الملخص 
"""
import os 
import sys
from pystyle import *
import datas1
import datas2
import randtest
import angel


#lesson 2 :

# variables : 

def load():
    import os 
    import sys
    import time
    i = 0
    while i<=50 :

        bar = "█" * i 
        percent = (i)*2
        
        sys.stdout.write (f"\r{bar} {percent}%")
        i+=1
        time.sleep(.01)

# الدرس الأول 
def l11 ():  # variables strings 
    #  # Strings
    first_name = "Bro"
    food = "pizza"
    email = "Bro123@fake.com"

    print(f"Hello {first_name}")
    print(f"You like {food}")
    print(f"Your email is: {email}")
def l12() : # variables integer  
    # #Integers
    age = 25
    quantity = 3
    num_of_students = 30

    print(f"You are {age} years old")
    print(f"You are buying {quantity} items")
    print(f"Your class has {num_of_students} students")
def l13() : # variables float 
    # Float
    price = 10.99999999999999
    gpa = 3.2
    distance = 5.5

    print(f"The price is ${price:.2f}")
    print(f"Your gpa is: {gpa}")
    print(f"You ran {distance}")
def l14() : # variables integer 
    # Boolean
    # المثال الاول 
    is_student = True
    print(f"Are you a student ?: {is_student}")
    # ولكن النص يجب أن يكون بطريقة اخرى 
    # المثال الثاني
    if is_student :
        print("Are you a student")
    else :
        print("Are you not a student")
    # المثال الثالث 
    for_sale = False
    if for_sale:
        print("That item is for sale")
    else:
        print("That item is NOT availablel")
    # المثال الرابع 
    is_online = True
    if is_online:
        print("You are online")
    else:
        print("You are offline")
# الدرس الثاني 
def l21(): # converte data type 
    # تحويل انواع المتغيرات بين بعضها البعض 
    name = "Bro Code"
    age = 25
    gpa = 3.2
    is_student = True
    print ("int (name)" ,  int (age) , int (gpa) , int  (is_student) , sep= '  ') 
    print ("float (name)",  float (age) , float (gpa) , float (is_student) , sep= '  ') 
    print (str (name)   ,  str (age) , str (gpa) , str  (is_student) , sep= '  ')
    print (bool (name)  , bool (age) , bool (gpa) , bool (is_student) , sep='  ')
# الدرس الثالث 
def l31():
    # input  هي دالة تستخدم لادخال القيم من المستخدم 
    name = input("What is your name ?: ")
    print(f"Hello {name}!")
    input("press any key to enter the ex.... ")
    # تمرين 
    def ex1():
        os.system ("cls")
        w = float (input ("Enter the width  : "))
        l = float (input ("Enter the length : "))
        A = w*l 
        print (f" the area of rectangle [W= {w} , L = {l}] is {A:.2f} cm² ")
    ex1()
    def ex2():
        # Madlibs game
        # word game where you create a story
        # by filling in blanks with random words
        adjective1 = input("Enter an adjective (description): ")
        noun1 = input("Enter a noun (person, place, thing): ")
        adjective2 = input("Enter an adjective (description): ")
        verb1 = input("Enter a verb ending with 'ing'")
        adjective3 = input("Enter an adjective (description): ")

        print(f"Today I went to a {adjective1} zoo.")
        print(f"In an exhibit, I saw a {noun1}")
        print(f"{noun1} was {adjective2} and {verb1}")
        print(f"I was {adjective3}!")
    ex2()
# الدرس الرابع 
def l41(x):
    friends = x
    print ("friends :   ", friends )
    friends = friends + 1
    # friends += 1
    print ("friends += 1 :  ", friends)
    # friends = friends - 2
    friends -= 2
    print ("ffriends -= 2 : ", friends)
    friends = friends * 3
    # friends *= 3
    print ("friends *= 3 :  ", friends)
    friends = friends / 2
    # friends /= 2
    print ("friends /= 2 :  ", friends)
    friends = friends ** 2
    # friends **= 2
    print ("friends **= 2:  ", friends)
    friends  = friends % 3 
    #friends %= 3 
    print ("friends %= 3:   ", friends )      
def l42 (x):
    print (x)
    result = round(x)
    print ("round(x)" , result )
    result = abs(x)
    print ("abs(x)" , result )
    result = pow(x, x+1)
    print (f"pow(x, x+1)  {result:.2f}" )

    result = min(x, 1, 10)
    print ("min(x, 1, 10)" , result )

    result = max(x, 1, 10)
    print ("min(x, 1, 10)" , result )

    result = min(x, 1, 10)
    print ("min(x, 1, 10)" , result )
def l43 () : #math.function

    #  هذه المكتبة المتكاملة لكل مكتبة  ماث 
    import os
    import time 
    os.system('cls')
    print ("************************************************************\n\n")
    import random
    import math
    while True :
        os.system('cls')
        x = int(input ("enter the number [1 ... 52 ]"))
        x-=1
        
        print("****************     Random calcalator      ****************\n\n")
        print("\t\t\t\t     ", x, "\n\n")

        if x == 0:
            print("Function is :  acos(n) ----> [take n ( -1 : 1 )]")
            print ("\t Returns the arc cosine of a number")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.acos(n))

        elif x == 1:
            print("function is :  acosh(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.acosh(n))

        elif x == 2:
            print("function is :  asin(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.asin(n))

        elif x == 3:
            print("function is :  asinh(n)----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.asinh(n))

        elif x == 4:
            print("function is :  atan(n)----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.atan(n))

        elif x == 5:
            print("function is :  atan2(y, x)----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            y = float(input("Enter the 1st number :   "))

            x = float(input("Enter the 2nd number :   "))

            print("The result :", math.atan2(y, x))

        elif x == 6:
            print("function is :  atanh(n)----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.atanh(n))

        elif x == 7:
            print("function is :  ceil(n)----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.ceil(n))

        elif x == 8:
            print("function is :  comb(n, k)----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = int(input("Enter the number :   "))

            k = int ("Enter the number :   ")
            print("The result :", math.comb(n, k))

        elif x == 9:
            print("function is :  copysign(x, y) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            x =float(input("Enter the number :   "))

            y =float(input("Enter the number :   "))

            print("The result :", math.copysign(x, y))

        elif x == 10:
            print("function is :  cos(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.cos(n))

        elif x == 11:
            print("function is :  cosh(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.cosh(n))

        elif x == 12:
            print("function is :  degrees(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.degrees(n))

        elif x == 13:
            print("function is :  dist(p, q) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            p = [float(input("Enter the p1 number :   ")), float(input("Enter the p2 number :   "))]
            q = [float(input("Enter the q1 number :   ")), float(input("Enter the q2 number :   "))]
            print("The result :", math.dist(p, q))

        elif x == 14:
            print("function is :  erf(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.erf(n))

        elif x == 15:
            print("function is :  erfc(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.erfc(n))

        elif x == 16:
            print("function is :  exp(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.exp(n))

        elif x == 17:
            print("function is :  expm1(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.expm1(n))

        elif x == 18:
            print("function is :  fabs(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.fabs(n))

        elif x == 19:
            print("function is :  factorial(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = int(input("Enter the number :   "))
            print("The result :", math.factorial(n))

        elif x == 20:
            print("function is :  floor(n)----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.floor(n))

        elif x == 21:
            print("function is :  fmod(x, y) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            x = float(input("Enter the 1st number :   "))
            y = float(input("Enter the 2nd number :   "))
            print("The result :", math.fmod(x, y))

        elif x == 22:
            print("function is :  frexp(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.frexp(n))

        elif x == 23:
            print("function is :  fsum(iterable) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            iterable = list(map(float, input("Enter the number :   ").split()))
            print("The result :", math.fsum(iterable))

        elif x == 24:
            print("function is :  gamma(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.gamma(n))

        elif x == 25:
            print("function is :  gcd(a, b) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            a = int(input("Enter the 1st number :   "))
            b = int(input("Enter the 2nd number :   "))
            print("The result :", math.gcd(a, b))

        elif x == 26:
            print("function is :  hypot(x, y) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            x = float(input("Enter the 1st number :   "))
            y = float(input("Enter the 2nd number :   "))
            print("The result :", math.hypot(x, y))

        elif x == 27:
            print("function is :  isclose(a, b) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            a = float(input("Enter the 1st number :   "))
            b = float(input("Enter the 2nd number :   "))
            print("The result :", math.isclose(a, b))

        elif x == 28:
            print("function is :  isfinite(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.isfinite(n))

        elif x == 29:
            print("function is :  isinf(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.isinf(n))

        elif x == 30:
            print("function is :  isnan(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.isnan(n))

        elif x == 31:
            print("function is :  isqrt(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = int(input("Enter the number :   "))
            print("The result :", math.isqrt(n))

        elif x == 32:
            print("function is :  ldexp(x, i) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            x = float(input("Enter the number :   "))

            i = int(input("Enter the number :   "))
            print("The result :", math.ldexp(x, i))

        elif x == 33:
            print("function is :  lgamma(n) ----> [take n ( >=1 )]")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.lgamma(n))

        elif x == 34:
            print("function is :  log(n, base) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            base = float(input("Enter the base number :   "))
            print("The result :", math.log(n, base))

        elif x == 35:
            print("function is :  log10(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.log10(n))

        elif x == 36:
            print("function is :  log1p(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.log1p(n))

        elif x == 37:
            print("function is :  log2(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.log2(n))

        elif x == 38:
            print("function is :  modf(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.modf(n))

        elif x == 39:
            print("function is :  nextafter(x, y) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            x = float(input("Enter the 1st number :   "))
            y = float(input("Enter the 2nd number :   "))
            print("The result :", math.nextafter(x, y))

        elif x == 40:
            print("function is :  perm(n, k) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = int(input("Enter the 1st number :   "))
            k = int(input("Enter the 2nd number :   "))
            print("The result :", math.perm(n, k))

        elif x == 41:
            print("function is :  pow(x, y) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            x =float(input("Enter the number :   "))

            y =float(input("Enter the number :   "))

            print("The result :", math.pow(x, y))

        elif x == 42:
            print("function is :  prod(iterable) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            iterable = list(map(float, input("Enter the number with space :   ").split()))
            print("The result :", math.prod(iterable))

        elif x == 43:
            print("function is :  radians(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.radians(n))

        elif x == 44:
            print("function is :  remainder(x, y =) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            x = float(input("Enter the 1st number :   "))
            y = float(input("Enter the 2nd number :   "))
            print("The result :", math.remainder(x, y))

        elif x == 45:
            print("function is :  sin(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.sin(n))

        elif x == 46:
            print("function is :  sinh(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.sinh(n))

        elif x == 47:
            print("function is :  sqrt(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.sqrt(n))

        elif x == 48:
            print("function is :  tan(n) ----> [take n ( >=1 )") 
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.tan(n))

        elif x == 49:
            print("function is :  tanh(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.tanh(n))

        elif x == 50:
            print("function is :  trunc(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.trunc(n))

        elif x == 51:
            print("function is :  ulp(n) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = float(input("Enter the number :   "))
            print("The result :", math.ulp(n))

        elif x == 52:
            print("function is :  comb(n, k) ----> [take n ( >=1 )")
            print ("\t ")
            print ("*******************************************\n\n")
            n = int(input("Enter the 1st number :   "))
            k = int(input("Enter the 2nd number :   "))
            print("The result :", math.comb(n, k))

        x= input ("\n\n Do you want to calc agine :  [ Y , N ] ")
        if x == 'y':
            print ("wellcom balck")
        elif x == 'n':
            print ('bye bye ')
            break
        else :
            print ('wrong char ')
            time.sleep(2)
def l44 () : # example على المسائل الرياضية 
    def ex1():
        import math 
        radius = float(input('Enter the radius of a circle: '))
        
        circumference = 2 * math.pi * radius  # المحيد 
        print(f"The circumference is: {round(circumference, 2)}")

        print(f"The area of the circle is: {area:.2f}cm²")
        area = math.pi * pow(radius, 2)  # حساب المساحة للدائرة 
    ex1()
    def ex2() :
        os.system ("cls")
        a = float(input("Enter side A: "))
        b = float(input("Enter side B: "))
        c = math.sqrt(pow(a,2)+pow(b,2))
        print(f"Side C = {c}")
    ex2() 
def l45():
    import math11
    math11.display()
# الدرس الخامس 
def l51():
    age = int(input("Enter your age:"))
    if age >= 100:
        print("You are too old to sign up")
    elif age >= 18:
        print("You are now signed up!")
    elif age < 0:
        print("You haven't been born yet!")
    else:
        print("You must be 18+ to sign up")
    
    name = input("Enter your name: ")
    if name == "":
        print("You did not type in your name!")
    else:
        print(f"Hello {name}")
    
    
    response = input("Would you like food? (Y/N): ")

    if response == "y": # انتبه في هذا المثال لحالة الحروف الكبيرة والصغيرة  
        print("Have some food!")
    else:
        print("No food for you!")
def l52(): # استعمال الجمل المنطقية مع if 
    for_sale = False
    if for_sale:
        print("This item is for sale")
    else:
        print("This item is NOT for sale")

    online = True
    if online:
        print("The user is online")
    else:
        print("The user is offline")
def l53(): # تمرين الالة الحاسبة 
    operator = input("Enter an operator (+ - * /): ")
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/":
        result = num1 / num2
        print(round(result, 3))
    else:
        print ("the operation  {operator}  is not vild")
def l54(): # تمرين محول الاوزان 
    weight = float (input("Enter your weight : "))
    unit = input("Kilograms or Pounds? (K or L): ")
    if unit == "K" or unit == "k":
        weight = weight * 2.205 
        unit = "Lbs."
    elif unit == "L" or unit == "l":
        weight = weight / 2.205
        unit = "Kgs."
    else:
        print(f"{unit} was not valid")
        pass
    print(f"Your weight is: {weight} {unit}")
def l55(): #  تمرين محول الحرارة 
    unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
    temp = float(input("Enter the temperature: "))

    if unit == "C" or unit == "c":
        temp = round((9* temp) / 5 +32, 1)
        print(f"The temperature in Fahrenheit is: {temp}°F")
    elif unit == "F" or unit == "f":
        temp = round((temp -32) *5 /9,1)
        print(f"The temperature in Celsius is: {temp}C")
    else:
        print(f"{unit} is an invalid unit of measurement")
def l56(): # الطقس والحالة الجوية  
    temp =-10
    is_sunny = 0
    if temp >= 28 and is_sunny:
        print("It is HOT outside 🥵")
        print("It is SUNNY ☀️")
    elif temp <= 0 and is_sunny:
        print("It is COLD outside 🥶:")
        print("It is SUNNY ☀️")
    elif 28 > temp > 0 and is_sunny:
        print("It is WARM outside 😊")
        print("It is SUNNY ☀️")
    elif temp >= 28 and not is_sunny:
        print("It is HOT outside 🥵")
        print("It is cloudy ☁️")
    elif temp <= 0 and not is_sunny:
        print("It is COLD outside 🥶:")
        print("It is cloudy ☁️")
    elif 28 > temp > 0 and not is_sunny:
        print("It is WARM outside 😊")
        print("It is cloudy ☁️")
def l57(): # الجمل الشرطية المختصرة 
    num = 5
    a = 6
    b = 7
    age = 13
    temperature = 20
    user_role = "guest"

    print("Positive" if num > 0 else "Negative")
    result = "EVEN" if num % 2 == 0 else "COD"
    max_num = a if a > b else b
    min_num = a if a < b else b
    status = "Adult" if age >= 18 else "Child"
    weather = "HOT" if temperature > 20 else "COLD"
    access_level = "Full Access" if user_role == "admin" else "Limited Access"
    print ("result odd / even >> " , result)
    print ("max_num",max_num)
    print ("min_num",min_num)
    print ("status",status)
    print ("weather",weather)
    print ("access_level",access_level)
# الدرس السادس / السلاسل النصية 
def l61 ():
    os.system('cls')
    #print (help (str))
    
    print ("*********************************************************\n\n")
    name = input ("Enter Your F.name and L.Name : " )
    char = len(name)
    # هذا الكود يرجع طول النص 
    print(Box.Lines(f'{name}')) # البوكي الاجمل لعمل القواءم 
    print ( "***********************************************************")

    print ( f"the length of char  in {name} is  :  {char}")
    # هذا الكود يقوم بحساب طول الكلمة 
    print ( "All small letter is                  : ", name.lower())
    #هذا الكود يقوم بارجاع المدخل على شكل حروف صغيرة 
    print ( "All captel letter is                 : ", name.upper())
    #هذا الكود يقوم بارجاع المدخل على شكل حروف كبيرة 
    print ( "farst letter is captel is            : ", name.capitalize() )
    #هذا الكود يقوم بكتابة الحرف الاول فقط كبير 
    print ( "the first name is captel             : ", name.title())
    #هذا الكود يقوم بكتابة الحرف الاول كبير في كل كلمة 
    print ( "without space (after and befoor ) is : ", name.strip())
    #هذا الكود يقوم بحذف الفراغات في الاول والاخر  
    print ( " the name is spilet is               : ", name.split())
    #هذا الكود يقوم بتقسيم الكلمات المكتوبة (الي بينها فراغات ) 
    print ( "Is alpha letter                      : ", name.isalpha())
    #هذا الكود يختبر المدخل هل هو حروف 
    print ( "IS digits is                         : ", name.isdigit())
    #هذا الكود يختبر هل هو أرقام 
    print ( "swapcase :                           : ", name.swapcase())
    # هذا الكود يقلب الحرف الصغير كبير والكبير صغير 
    inv_name = name[::-1]
    print ( "your inverse name is                 : ", inv_name)
    #هذا الكود يعكس اسمك مباشرة 
    
    i = 0
    x = input ("Enter the char to search : ")
    print ( f"the number of [ {x} ] in {name} is : {name.count(x)}") # عدد مرات ظهور الحرف 
    print (f"the location  of first [ {x} ] in {name} is : {name.find(x)}")
    #  هذا الكود يبحث عن عنصر من البداية للنهاية 
    print (f"the location  of last  [ {x} ] in {name} is : {name.rfind(x)}")   
    #  هذا الكود يبحث عن عنصر من النهاية للبداية
def l62(): # الوصول لكل العناصر في القائمة 
    name = input ("enter any name : ")

    print ("name [0] ", name[0])
    print ("name [-1] " , name [-1])
    
    print ("name [:5] ", name [:5])
    print ("name [2:] ",name [2:])
    
    print ("name [::2] ",name [::2])
    print ("name [::-1] ",name [::-1])

    # لتقسيم النص بناء على معلومات معينة 
    name = "stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
    print (name)
    x = name.find('@')
    nn = name [:x]
    y = name.find(' ')
    ee = name [x+1:y]
    print (nn)
    print (ee)
    name2 =  'rami'
    print (name2+ ' ' + name2)
    print (name2 * 5)
    print ("T" if 'r' in name2 else "F")   
def l63(): #

    name = input ( " ENTER NAME : ")   # الوصول لكل حرف في الاسم

    #print (name.index(x, i)) # تحتاج المزيد من الشرح 
    
    for i in range(0 , len(name)):
        print ("[", i  , " : ", name[i] ,"]", end = "   ")
    print()

    x = input ( "Enter char to replace  : ")
    y = input ( "Enter new char    : ")
    # انتبه بأن اصل الاسم لا يجدث له تغيير وانما عرض واسناد
    print (f"In {name} you want to replace {x} with {y}  ")
    print ("The new name is ", name.replace(x,y))
    
    # انتبه دالة الاستبدال تستبدل جميع الحروف بالحرف الجديد 
    print ("The main is : ", name )
    
    x = input ( "Enter char (TO detect location )  : ")
    print (x, end= "")
    print ("  in location  : ", end= "")
    i = -1

    for letter in name:   # ومعرفة موقعه في السلسلة 
        i+=1
        if letter == x :
            print (i , end= "   ")
    print ()

    if len((name.split())) >1 : # الوصول لكل جزء في الاسم 
        for part in name.split():
            print (part.capitalize())
def l64 (): # تمرين التحقق من اسم المستخدم 
    print (Box.Lines('enter your nmame: ') )
    name = input(" "*49)
    if name.isalpha () :
        if len(name)>=12 :
            print ("good name ")
    else :
        print ("bad name ")

def l71():
    # format specifiers = {value:flags} format a value based on what
    # flags are inserted
    # .(number)f = round to that many decimal places (fixed point)
    # : (number) = allocate that many spaces
    # :03 = allocate and zero pad that many spaces
    # :< = left justify
    # :> = right justify
    # :^ = center align
    # :+ = use a plus sign to indicate positive value
    # := = place sign to leftmost position
    # : = insert a space before positive numbers
    # :, = comma separator
    pass

def l81(): # الحلقات التكرارية
    # while loop = execute some code WHILE some condition remains true
    name = input("Enter your name: ")
    while name == "":
        print("You did not enter your name")
        name = input("Enter your name: ")
    print(f"Hello {name}")
    
    age = int(input("Enter your age: "))
    while age < 0:
        print("Age can't be negative")
        age = int(input("Enter your age: "))

    print(f"You are {age} years old")
def l82():
    principle = 0
    rate = 0
    time = 0
    while principle <= 0:
        principle = float(input("Enter the principle amount: "))
        if principle <= 0:
            print("Principle can't be less than or equal to zero")
    
    while rate <= 0:
        rate = float(input("Enter the interest rate: "))
        if rate <= 0:
            print("Interest rate can't be less than or equal to zero")

    while time <= 0:
        time = int(input("Enter the time in years: "))
        if time <= 0:
            print("Time can't be less than or equal to zero")

    print(principle)
    print(rate)
    print(time)
    total = principle * pow((1 + rate / 100), time)
    print(f"Balance after {time} year/s: ${total :.2f}")
def l83():
    print("111")
def l84():
    import time
    my_time = int(input("Enter the time in seconds: "))
    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        os.system("cls")
        print (Box.Lines(f"{hours:02}:{minutes:02}:{seconds:02}"))
        time.sleep(1)

    print("TIME'S UP!")
def l85():
    for x in range(3):
        for x in range(1, 10):
            print(x, end=" ")    
    print()

    print ("drow (rec)")
    rows = int(input("Enter the # of rows: "))
    columns = int(input("Enter the # of columns: "))
    symbol = input("Enter a symbol to use: ")

    for x in range(rows):
        for y in range(columns):
            print(symbol, end="")
        print()

def l91(): #colletion 
    fruits = ["apple", "orange", "banana", "coconut"]
    # print(dir(fruits))
    # print(help(fruits))
    for fruit in fruits:
        print(fruit)
def l92(): 
    datas1.ma ()
def l93():
    pass
    # datas2.maa()
def l101():# مكتبة الارقام العشوائية 
    randtest.rean()
def l102(): # حجرة ورقة مقص ( لعبة )
    import random
    options = ("rock", "paper", "scissors")
    running = True

    while running:
        os.system("cls")
        player = None
        computer = random.choice(options)

        while player not in options:
            player = input("Enter a choice (rock, paper, scissors) : ")
        print (f"your choice is {player} VS computer choice : {computer}")
        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")

        if not input("Play again? (y/n):").lower() == "y":
            running = False
            print("Thanks for playing!")
def l103(): # NARD GAME 
   angel.game()

def l111(): #functions 
    # function = A block of reusable code
    # place () after the function name to invoke it
    def happy_birthday(x, y):# تعريف الدالة 
        print(f"Happy birthday to {x}!")
        print(f"You are {y} years old!")
        print("Happy birthday to you!")
        print()

    happy_birthday("Bro", 20)# استدعاء الدالة 
    name = input ("enter your name  : ")
    age = input ("enter your  age : ")

    happy_birthday(name, age)
    happy_birthday("Joe", 40)
def l112(): 
    def display_invoice(username, amount, due_date):
        print(f"Hello {username}")
        print(f"Your bill of ${amount :.2f} is due: {due_date}")

    display_invoice("JoeSchmo", 100.01, "01/02")
def l113 (): #return
    # return = statement used to end a function
    # and send a result back to the caller

    def create_name(first, last):
        first = first.capitalize()
        last = last.capitalize()
        return first + " " + last

    full_name = create_name("bro", "code")

    print(full_name)
def l114(): #return
    # default arguments = A default value for certain parameters
    # default is used when that argument is omitted
    # make your functions more flexible, reduces # of arguments
    # 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

    def net_price(list_price, discount=0, tax=0.05):
        return list_price * (1 - discount) * (1 + tax)

    print("net_price(500) : " ,net_price(500))
    print("net_price(500, 0.1) : ", net_price(500, 0.1))
    print("net_price(500, 0.1, 0): ",net_price(500, 0.1, 0))
    print("net_price(500, tax= 50% ): ",net_price(500, tax= .5))
def l115():
    # keyword arguments = an argument preceded by an identifier
    # helps with readability
    # order of arguments doesn't matter
    # 1. positional 2. default 3. KEYWORD 4. arbitrary

    def hello(greeting, title, first, last):
        print(f"{greeting} {title}{first} {last}")

    hello("Hello", title="Mr.", last="John", first="James")
def l116 (): #tuple and list and set in function 
    # *args
    # ** kwargs = allows you to pass multiple keyword-arguments
    #            unpacking operator
    # 1. positional 2. default 3. keyword 4. ARBITRARY

    def add(*args):
        total = 0
        for arg in args:
            total += arg
        return total

    print(add(1, 2, 3, 4,5))
    mylist = [1,2]
    print (add (*mylist))
def l117 (): # dict in function 
    def print_address( ** kwargs):
        for key, value in kwargs.items():
            print(f"{key} : {value}")


    # print_address(street="123 Fake St.",
    #     apt="100",
    #     city="Detroit",
    #     state="MI",
    #     zip="54321")
    mydict = {
                "name": "John",
                "age": 30,
                "city": "New York" 
    }
    print (mydict)
    print (type(mydict))
    print_address(**mydict)

def l121(): # Iterables
    # Iterables = An object/collection that can return its elements one at a time,
    # allowing it to be iterated over in a loop
    family = ['rami', 'ahlam ', 'ghazal' , 'rema' , 'zina' ,'fasil']
    print (type(family))
    for person in family: 
        print(person, end="  ")
    print()

    numbers = (1, 2, 3, 4, 5)
    print(type(numbers))
    for number in reversed(numbers):
        print(number , end=" - ")
    print()
    
    # for number in range(len(numbers)-1): # مثال اخر للتغلب على الاشارة النهائية 
    #     print(numbers[number] , end=" - ")
    # print(numbers[-1])

    fruits = {"apple", "orange", "banana", "coconut"}
    print(type(fruits))
    for fruit in fruits: # set object is not  reversible >> function give error 
        print(fruit , end="  ")

    name = "rami sadaa"
    print(type(name))
    for character in name:
        print(character, end=" ")
    print()


    my_dictionary = {"A": 1, "B": 2, "C": 3}
    print(type(my_dictionary))
    for key, value in my_dictionary.items():
        print(f"{key} = {value}")

def l131():# 
    # Membership operators = used to test whether a value or variable is found in a sequence
    #                                    (string, list, tuple, set, or dictionary)
    #                                                 in  &  not in
    word = "APPLE"
    letter = input("Guess a letter in the secret word: ")
    if letter in word:
        print(f"There is a {letter}")
    else:
        print(f"{letter} was not found")

    students = {"rami", "rema", "reham"}

    student = input("Enter the name of a student: ")

    if student in students:
        print(f"{student} is a student")
    else: 
        print(f"{student} was not found")

    grades = {"ghazal": "A",
              "zina": "B",
              "rema": "C",
              "fasil": "D"}

    student = input("Enter the name of a student: ")

    if student in grades:
        print(f"{student}'s grade is {grades[student]}")
    else:
        print(f"{student} was not found")
def l132(): # كود فحص صحة الايمال 

    email = input("Enter your email : ")

    if "@" in email and "." in email:
        print("Valid email")
    else:
        print("Invalid email")

def l141():
    # List comprehension = A concise way to create lists in Python
    # Compact and easier to read than traditional loops
    # [expression for value in iterable if condition]

    doubles = []
    for x in range(1, 11):
        doubles.append(x * 2)
    print(doubles)

    doubles2 = [x * 2 for x in range(1, 11)]
    print(doubles2)
    triples = [y * 3 for y in range(1, 11)]
    print(triples)
    squares = [z * z for z in range(1, 11)]
    print(squares)
def l142():
    fruits = ["apple", "orange", "banana", "coconut"]
    fruits = [fruit.upper() for fruit in fruits]
    print(fruits)

    fruits = [fruit.capitalize() for fruit in ["apple", "orange", "banana", "coconut"]]
    print(fruits)

    fruits = [fruit[0].capitalize() for fruit in ["apple", "orange", "banana", "coconut"]]
    print(fruits)
def l143():

    numbers = [1, -2, 3, -4, 5, -6, 8, -7]
    positive_nums = [num for num in numbers if num >= 0]
    negative_nums = [num for num in numbers if num < 0]
    even_nums = [num for num in numbers if num % 2 == 0]
    odd_nums = [num for num in numbers if num % 2 == 1]

    print("positive_nums",positive_nums)
    print("negative_nums",negative_nums)
    print('even_nums',even_nums)
    print('odd_nums',odd_nums)

def l151(): #Match-case statment
    # Match-case statement (switch): An alternative to using many 'elif' statements
    # Execute some code if a value matches a 'case'
    # Benefits: cleaner and syntax is more readable

    def day_of_week(day):
        match day:
            case 1:
                return "It is Sunday"
            case 2:
                return "It is Monday"
            case 3:
                return "It is Tuesday"
            case 4:
                return "It is Wednesday"
            case 5:
                return "It is Thursday"
            case 6:
                return "It is Friday"
            case 7:
                return "It is Saturday"
            case _:
                return "Not a valid day"
    x = day_of_week(int(input("enter the number[1~7] :")))
    print (x)

    def is_weekend(day):
        match day:
            case "Saturday" | "Sunday":
                return True
            case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
                return False
            case _:
                return False

    print(f"is {x} a weekend : { is_weekend(x) }")
def l152():
    print("1 Arabic\n2 English\n3 Frensh")
    choice = int(input("Chooce a number: "))
    match choice :
        case 1 :
            print (arab("مرحبا يا صديقي ")) 
        case 2 :
            print("Hello")
            print("How can we help you ? ")
        case 3 :
            print("Bonjour")
        case _ :
            print("Unsupported language") 

def l161():# mudules  الموديل 
    # module = a file containing code you want to include in your program
    # use 'import' to include a module (built-in or your own)
    # useful to break up a large program reusable separate files

    # print(help("modules"))
    import math
    # import math as m
    # from math import e

    a, b, c, d, e = 1, 2, 3, 4,5

    print(a ** a)
    print(b ** b)
    print(c ** c)

    print (int(math.pow(b,b)))

    print ("Python Module Index")
    url = "https://docs.python.org/3/library/math.html#module-math"
    print (url)
    

def l171(): # variable scope , scope resolution ترتيب المتغيرات 
# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
    pass
def l181():
    def ss():
        print ("ss")
    if __name__ == '___main___':
        ss()
    
def l201(): # Decorator = A function
    print ("lesson 201 : Decorator")

# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

    def add_sprinkles(func):
        def wrapper(*args, ** kwargs):
            print("*You add sprinkles")
            func(*args, ** kwargs)
        return wrapper
    
    def add_fudge(func):
        def wrapper(*args, ** kwargs):
            print("*You add fudge")
            func(*args, ** kwargs)
        return wrapper

    @add_sprinkles
    @add_fudge
    def get_ice_cream(sss):
        print(f"Here is your {sss} ice cream")
    
    get_ice_cream("sss")
def l202(): # تجربة شخصية 
    st=[]
    s_st = []
    def lib_ac(func):
        def wrapper( *args, ** kwargs):
            print ("u have liblary acount ")
            x = int (input("enter 1 or other "))
            if x == 1 :
                print ("number is 1 :")
            else :
                print("number is not 1 ")
            func(*args, ** kwargs)
        return wrapper
    
    def mark_ac(func):
        def wrapper(*args, ** kwargs):
            print ("u have mark acount ")
            func(*args, ** kwargs)
        return wrapper
    @lib_ac
    @mark_ac
    def add_st(id , name , email):
        print (" welcome to add student screen : ")
        st_id = id #input("id :")
        st_name = name #input("name :")
        st_email = email #input("e-mail :")
        s_st = [st_id,st_name,st_email]
        st.append(s_st)
        print (f"u add  {st_id}    {st_name}    {st_email}")
        print (s_st)
        print (st)
    add_st("150" , "rami" , "rami.sadaa@gmail.com")
    

def arab(text):#arabic 
    import arabic_reshaper
    from bidi.algorithm import get_display
    
    text1 = get_display (arabic_reshaper.reshape (text))
    return(text1)

def l9998(): #  ascii الرموز الخاصة والاشكال الخاصة ببايثون 
        for _ in range (1,20): # عندما تكون غير مهتم بتعريف المتغير
        #print (_, end=" ") # ولكن هو فعليا يعتبر متغير مؤقت
            print ( _ , ">>>" , chr(_)) # chr تعطي رمز بدالة الرقم 

        print ("ord('A') : ", ord('A'))
        print (_)
        print (type(_))
        import string as S
        for _ in S.ascii_lowercase:
            print (_ ,"  >>>  ",  ord(_)) # تعطي رقم بدالة الرمز 
        for _ in S.printable: # printable  دالة فيها جميع الرموز 
            print (_ ,"  >>>  ",  ord(_))
        
        c4 ="rami.sadaa@gmail.com"
        print (c4.split('@')) # التقسيم على اساس عنصر في النص 
        url = "www" 
        print (url) # رابط كل الرموز الخاصة مهم جدا بكودها 

def l9999(): #example send email by google dont work
    import os
    import random
    import smtplib

    def automatic_email () :
        user = input ("Enter Your Name >>: ")
        email = input ("Enter Your Email >>: ")
        message = (f"Dear {user}, Welcome to Thecleverprogrammer")
        s = smtplib.SMTP ('smtp.gmail.com', 587)
        s.starttls ()
        s.login ("Your Gmail Account", "Your App Password")
        s.sendmail ('&&&&&&&&&&& ' , email, message)
        print ("Email Sent!")

    automatic_email ()


os.system ("cls")
load()
os.system ("cls")
print (arab( "بسم الله الرحمن الرحيم" ))
print (arab( "أهلا وسهلا بكم في البرنامج التعليمي" ))
#print(dir()) يعرض جميع الدوال في البرنامج 

ls = input (" enter the lesson number  : ")
while not  ls.isdigit() :
    print (" try agine ")
    #os.system('cls')
    ls = input ("\n enter the lesson number  : ")
ls = int (ls)
if   ls == 11 :
    l11()
elif ls == 12:
    l12()
elif ls == 13:
    l13()
elif ls == 14:
    l14()
elif ls == 21 :
    l21()
elif ls == 31:
    l31()
elif ls == 41:
    x= 5
    l41(x)
elif ls == 42 :
    x= 5.5
    l42(x)
elif ls == 43 :
    l43()
elif ls == 44 :
    l44 ()
elif ls == 45 :
    l45()
elif ls == 51 :
    l51()
elif ls == 52 :
    l52()
elif ls == 53 :
    l53()
elif ls == 54:
    l54()
elif ls == 55 :
    l55()
elif ls == 56:
    l56()
elif ls == 57:
    l57()
elif ls == 61 :
    l61()
elif ls == 62 : 
    l62()
elif ls == 63 :
    l63()
elif ls == 64 :
    l64()
elif ls == 71 :
    l71()
elif ls == 81 :
    l81()
elif ls == 82 :
    l82()
elif ls == 83 :
    l83
elif ls == 84 :
    l84 ()
elif ls == 85 :
    l85 ()
elif ls == 91:
    l91()
elif ls == 92 :
    l92()
elif ls == 93 :
    l93 ()
elif ls == 101 :
    l101()
elif ls == 102 :
    l102()
elif ls == 103 :
    l103()
elif ls == 111 :
    l111()
elif ls == 112 :
    l112 ()
elif ls == 113 :
    l113()
elif ls== 114 :
    l114()
elif ls == 115:
    l115()
elif ls == 116:
    l116()
elif ls ==  117:
    l117()
elif ls == 121:
    l121()
elif ls == 131:
    l131()
elif ls == 132:
    l132()
elif ls== 141:
    l141()
elif ls == 142:
    l142()
elif ls == 143:
    l143()    
elif ls == 151:
    l151()
elif ls == 152:
    l152()
elif ls == 161:
    l161()
elif ls == 171:
    l171()
elif ls == 181:
    l181()
elif ls == 201:
    l201()
elif ls == 202:
    l202 ()

elif ls== 9999:
    l9999()
elif ls == 9998:
    l9998()


