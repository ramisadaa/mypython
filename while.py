import random as r
# print ("hello to my prog ")
# # allsum = 0
# # x = int (input ("enter your number "))
# # while x>= 0:
# #     allsum +=x 
# #     x = int (input ("enter your number "))
# # else :
# #     print ("the nsum umber you enter allsum", allsum) 

# # print ("wellcome to list with loop ")
# # namelist = []
# # y = 0
# # x = input ("enter your number ")

# # while x != "qqq":
# #     namelist.append(x)
# #     x = input ("enter your number ")

# # # y = len(namelist)
# # namelist.sort(reverse= True)
# # print (namelist)

# # # while y >0 :
# # #     y -=1
# # #     print (namelist[y])
# # # print ("byebye")

# # # for item in range(len(namelist)):
# # #     print (f"{item+1}   >>>>>>    {namelist[item]}")
# # #     print (item, end=" ")


# # for item in namelist:
# #     print (item)

# print ("*"*50)
# print ( "wellcome to mul :")
# # x = int(input ("enter your number : "))

# # for i in range (11):
# #     print (f"{i} X {x} = {x*i}")
# # print ("bye bye bye ....")

# stu ={ 
#     'r': 95,
#     'z': 45,
#     'n': 51,
#     'o':52,
#     's':99, 
#     't':60,
#     'm':70

# } 
# counter = 0

# for ke, ve in stu.items():
#     print(f"{ke} =====>>> {ve}")


# print ("the pass student is : ")
# for k in stu:
#     if stu[k] >=60:
#         print (stu[k])
#         counter +=1

# print ("the number of pass stu is ", counter )
# # for k in mydict:
# #     print(f"{k}: {mydict[k]}")



# # while i < 6:
# #   i += 1
# #   if i %2 ==1:
# #     continue
# #   print(i)

# for i in range(5):
#   print (i, "===>>>>", r.randint(15,20))

# استخراج الأعداد الأولية من 2 إلى 100 بدون استعمال دوال جاهزة
# for i in range(2, 101):
#   is_prime = True
#   for j in range(2, i):
#     if i % j == 0:
#       is_prime = False
#       break
#   if is_prime:
#     print(i)
# while True:
    
#   num = int(input("Enter the number  "))

#   is_prime = True  # نفترض أن العدد أولي

#   if num < 2:
#       is_prime = False
#   else:
#       for i in range(2, int(num ** 0.5) + 1):
#           if num % i == 0:
#               is_prime = False
#               break

#   if is_prime:
#       print(f"{num}  Is prime number ")
#   else:
#       print(f"{num} Is not prime number ")


# start = int(input("Enter the lower bound: "))
# end = int(input("Enter the upper bound: "))

# for num in range(start, end + 1):
#         for i in range(2, int(num ** 0.5) + 1):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)


# start = int(input("Enter the lower bound: "))
# end = int(input("Enter the upper bound: "))

# for num in range (start,end+1):
#     for i in range( 2, int(num**.5)+1):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)

        # Example: Creating 3 dictionaries inside a main dictionary

import os 
os.system ("cls")
students = {
            "classA": {"Ali": 90, "Sara": 85},
            "classB": {"Omar": 78, "Lina": 92},
            "classC": {"Mona": 88, "Tariq": 80}
        }
print("1 # print all dictionary data :")
print (" print (students):"  , students)

print("2 # print all dictionary data ad adictionary : ")
for class_name, student_scores in students.items():
    print(f"{class_name}: {student_scores}")

print("3 # reatch to every item in dict , sub dict   : ")
for stu_key , stu_val in students.items() :
    for sub_key , sub_val in students[stu_key].items():
        print (type (sub_key) , "======>>", type (sub_val))
        if sub_key == "Omar" and sub_val == 78 :
            print (" condition done ")
