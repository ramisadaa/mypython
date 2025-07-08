import os
os.system('cls')

# مثال على الاستخدام:
print ("*********************************************************************\n\n")
import random
import math 
x = int (random.uniform(0, 52))
print ("***********************        Your choise is        ****************\n\n")

print ("\t\t\t\t     ", x,"\n\n")

if x == 1:      #جتا الزاوية تأخد (-1 وحتى 1 ) 
    print (" the func is cos (n)")
    n = int ( input ("Enter the number :  (-1:1)    ") )
    o = float( math.acos(n) )
    print (f"cos {n} is {o}")

if x == 2:      ##جتا~ الزاوية تأخد (أكبر من أو يساوي 1 ) 
    print (" the func is cosh (n)")
    n = int ( input ("Enter the number :  (x>=1)    ") )
    o = float( math.acosh(n) )
    print (f"cosh {n} is {o}")

if x == 3:      ##جا الزاوية تأخد (-1 وحتى 1  ) 
    print (" the func is sin (n)")
    n = int ( input ("Enter the number :  (-1:1)    ") )
    o = float( math.asin(n) )
    print (f" sin {n} is {o}")

if x == 4:      ##جا~ الزاوية تأخد (-1 وحتى 1  ) 
    print (" the func is sinh (n)")
    n = int ( input ("Enter the number :  ( any)    ") )
    o = float( math.asinh(n) )
    print (f" sinh {n} is {o}")

if x == 8:
    print (" the func is ceil (n)") # ]دالة تقرب العدد الصحيح لمن هو أكبر منه 
    n =  float ( input ("Enter the number :  ( any )    " )) 
    o = float  ( math.ceil(n) )
    print (f" ceil {n} is {o:.3f}")

if x == 9: # توافق في الرياضيات تحتاج قراءة 
    print (" the func is comb (n)")
    n =  int ( input ("Enter the 1st number :  ( any )    " )) 
    n2 = int ( input ("Enter the 2nd number :  ( any )    " )) 
    o = float  ( math.comb(n , n2) )
    print (f" comb {n} is {o:.3f}")

if x == 10: # هي داله تأخذ اشارة الرقم الثاني وترجعها للاول  
    print (" the func is copysign (n)")
    n =  int ( input ("Enter the 1st number :  ( any )    " )) 
    n2 = int ( input ("Enter the 2nd number :  ( +1 ، -1 )    " )) 
    o = float  ( math.copysign(n , n2) )
    print (f" copysign {n} is {o}")


if x == 20:
    print (" the func is factorial (n)") # يعيد مضروب العدد !
    n =  int ( input ("Enter the number :  ( any )    " )) 
    o = float  ( math.factorial(n) )
    print (f" floor {n} is {o}")

if x == 22:
    print (" the func is fmod (n)") # دالة تعيد باقي القسمة  
    n =  float ( input ("Enter the number :  ( any )    " )) 
    n2 = int ( input ("Enter the 2nd number :  ( any )    " )) 
    o = float  ( math.fmod(n , n2) )
    print (f" fmod {n} / {n2} is {o}")

if x == 33:
    print (" the func is clm (n)") # تعيد المضاعف المشترك الاصغر 
    n =  int ( input ("Enter the number :  ( any )    " )) 
    n2 = int ( input ("Enter the 2nd number :  ( any )    " )) 
    o = float  ( math.lcm(n , n2) )
    print (f" lmc {n} ، {n2} is {o}")


if x == 40:
    print (" the func is modf (n)") # تحلل العدد الي صحيح وعشري  
    n =float ( input ("Enter the number :  ( float only )    ") )
    o =  math.modf(n)
    print (f" modf {n}  is {o}")


