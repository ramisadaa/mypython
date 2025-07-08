
# list :::
import json
# print(Box.Lines('Learn Python')) # البوكي الاجمل لعمل القواءم 

import os 
os.system ("cls") 
"""
السلام عليكم 

"""

# # # القائمة المراد حفظها
# # data1 = [1, 2, 3, 4, 5]

# # # حفظ القائمة في ملف txt
# # with open("data1.json", "w") as f:
# #     json.dump(data1, f)

# # # قراءة القائمة من نفس الملف
# # with open("data1.json","r") as f:
# #     data_read1 = json.load(f)

# # # طباعة النتيجة للتأكيد
# # print(data_read1)

# # # dict :::
# # # Writing to a JSON file
# # import json
# # data2 = {"name": "John", "age": 30, "city": "New York"}
# # with open("data2.json", "w") as ff:
# #     json.dump(data2, ff)

# # # Reading from a JSON file
# # with open("data2.json", "r") as ff:
# #     data_read2 = json.load(ff)

# # print(data_read2)

# myfam =  ["rami" , "admad ", "mohamaad" , "hussen" , "ali\n"]
# with open ("fam1.json " , "w" ) as f :
#     json.dump (myfam , f)

# with open ("fam1.json","r" ) as f :
#     famdata = json.load(f)

# print (famdata) # القاءمة الاصلية 

# myfam_udate   =  ["r" , "a ", "m" , "h" , "l\n"]

# with open ("fam1.json " , "a" ) as f :
#     json.dump (myfam_udate , f)

    
# with open ("fam1.json " , "r" ) as f :
#     print (f.read()) # القائمة المحدثة 


# try:
#    with  open(r"C:\python program\.vscode\python\filesys\ss.txt") as f :
#     print(f.read())
# except:
#     print("The file you want to read doesn't exist")
#     f = None  # Set f to None if file open fails
# finally:
#     f.close()
import arabic_reshaper
from bidi.algorithm import get_display

text =  " بسم الله الرحمن الرحيم  "
text1 =  arabic_reshaper.reshape (text)
text1 = get_display (text1)
print (text1)


print (get_display (arabic_reshaper.reshape (f"**** {text} **** "))) # الكود المختصر للكتابة بالغة العربية بشكل صحيح 

input ("press any key to cont.....")
os.system('cls')

from pystyle import *
print(Box.Arrow('1'))
print(Box.SimpleCube('Rakwan'))
print(Box.Lines('Learn Python')) # البوكي الاجمل لعمل القواءم 
print(Box.DoubleCube('Rakwan'))

input ("press any key to cont.....")
os.system('cls')

import emoji 
print ("😊❤️😂🤣😁(●'◡'●)🖤💜🤍✅")
# الايموجي تظهر من زر الوندوز و حرف الزاي باللغة العربية 

print (emoji.emojize(":red_heart:"))

input ("press any key to cont.....")
os.system('cls')


# التعامل مع الحروف 

import string as S

print (S.ascii_lowercase)
print (S.ascii_uppercase)

print (S.ascii_letters)

for letter in (S.ascii_lowercase) :
    print (letter , end = "     ")

print ()
print (S.octdigits) # الارقام من صفر لسبعة 

print ("=========================")
for sample in (S.punctuation) :
    print (sample , end= "     " )
print ()

print ("=========================")
for all in (S.printable) :
    print (all, end= "     ")
print ()

input ("press any key to cont.....")
os.system('cls')


top = 30
os.system ("cls")
import time

while True : 
    print ("\n" * top)
    print ('             /\              ')
    print ('             ||              ')
    print ('             ||              ')
    print ('             ||              ')
    print ('             ||              ')
    print ('            /||\             ')
    time.sleep (0.05)
    top -=1 
    os.system ("cls")
    if top <=0 :
        top = 30
    