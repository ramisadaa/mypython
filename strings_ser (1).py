import os
os.system('clear')


print ("*********************************************************\n\n")
name = input ("Enter Your F.name and L.Name : " )

from pystyle import *
print(Box.Lines(f'{name}')) # البوكي الاجمل لعمل القواءم 
print ( "***********************************************************")


print ( "All small letter is       : ", name.lower())
#هذا الكود يقوم بارجاع المدخل على شكل حروف صغيرة 
print ( "All captel letter is      : ", name.upper())
#هذا الكود يقوم بارجاع المدخل على شكل حروف كبيرة 
print ( "farst letter is captel is : ", name.capitalize() )
#هذا الكود يقوم بكتابة الحرف الاول فقط كبير 
print ( "the first name is captel  : ", name.title())
#هذا الكود يقوم بكتابة الحرف الاول كبير في كل كلمة 
print ( "without space (after and befoor ) is          : ", name.strip())
#هذا الكود يقوم بحذف الفراغات في الاول والاخر  
print ( " the name is spilet is    : ", name.split())
#هذا الكود يقوم بتقسيم الكلمات المكتوبة (الي بينها فراغات ) 
print ( "Is alpha letter           : ", name.isalpha())
#هذا الكود يختبر المدخل هل هو حروف 
print ( "IS digits is              : ", name.isdigit())
#هذا الكود يختبر هل هو أرقام 
inv_name = name[::-1]
print ( "your inverse name is      : ", inv_name)
#هذا الكود يعكس اسمك مباشرة 
i = 0
x = " "
print ( f"the number of space  in {name} is {name.count(x)}")
char = len (name)- name.count(x)

print ( f"the length of char in {name} is  :  {char}")
 # هذا يرجع عدد الحرف المطلوب


m = len((name.split()))
F_world = name.split()[0]
L_world = name.split()[1]
print ("\n\n *******   first letter in first word : ", F_world[0].capitalize())
print ("\n *******   last letter in secand word : ", L_world[0].capitalize())
print ( "\n***********************************************************")
print ( "***********************************************************")

x = input ( " We serch for : \n\t")
for letter in name: 
    if letter == x :
       # print("we found   : ", letter)
        i= i+1
ans = bool(name.find(x))

print (f"Is the { name } has {x} : {ans}") # هذا يرجع  0،1 فقط في الكود 

print ( f"the number of {x} in {name} is {name.count(x)}") # هذا يرجع عدد الحرف المطلوب

#print ("the number of  ", x , " is : " , i)   هذا النص بديل التالي 

message = f"THE NUMBER OF {x} is {i} in the : {name}"
print (message)
