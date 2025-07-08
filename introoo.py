import os



# # انشاء الملف 
# os.system ('cls')
# f = open("mmm.txt", 'x')
# filepath = os.path.abspath('mmm.txt')
# print (filepath)


# #قراءة الملف 
# print ("*"*10)

# f2 = open("mmm.txt", 'r')
# print (f2) # هنا القراءة للبيانات وليس للمحتويات
# # المحتويات تشمل التالي 
# print(f2.name)
# print (f2.mode)
# print (f2.encoding)


# # الطريقة الثانية لقراءة الملف 
# with open ("f_test.txt",'r') as f:
#     print (f.read ()) # 


# os.chdir('D:\python')  
# # # استبدل 'D:\python' بالمسار الذي تريده

# print ("*"*20)
# from pathlib import Path
# print (Path.cwd())

# f3 = open("rrr.txt", 'r')
# print (f3.name)

# طريقة الكتابة من خلال write
# f3 = open("rrr.txt", 'w')
# f3.write (" 44444444  ")
# with open ("rrr.txt") as ff:
#     print (ff.read())

# f2 = open ("mmm.txt", 'a')
# f2.write("hi hi hi mr rami ")
# with open ("mmm.txt") as fff:
#     print (fff.read())

# f2 = open ("mmm.txt", 'w')
# L = ["This is Delhi\n  ", "This is Paris\n   ", "\tThis is London\n"]
# f2.writelines(L)
# with open ("mmm.txt") as fff:
#     print (fff.read())

with open ("mmm.txt") as fff:
    for line in fff:
        print (line.strip())
