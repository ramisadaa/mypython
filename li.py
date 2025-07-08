import os 
import keyboard
os.system('cls')

listcolor = ["red", "green", "blue", "yellow", "black", "white"]
listfruit = ["apple", "banana", "orange", "grape", "mango", "kiwi" , "peach" , "pear" , "plum" , "cherry"]
listname = ["ahmed", "mohamed", "ali", "sayed", "hassan", "khaled" , "sherif" , "yasser" , "mostafa" , "mohsen"]        
listnumber = [1, 2, 3, 4, 11, 6, 7, 8, 9, 10]
listbool = [True, False]
listnone = [None]
listfloat = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
empty_list = []
l_in_l = [1 , 'rami' , 40.5 , 'teacher' , True , [60 , 70 , 80 ,90]]


#PRINT ALL LISTS

# print ("listcolor",listcolor)
# print ("listfruit",listfruit)
# print ("listnumbe",listnumber)
# print ("listname",listname)
# print ("listbool",listbool)
# print ("listnone",listnone)
# print ("listfloat",listfloat)   
# print ("empty_list",empty_list)
# print ("l_in_l",l_in_l)         

print (listnumber.sort(reverse=True))

# while True:  ### كنتول + حرف الظاء تعطي الرمز //
#     if keyboard.is_pressed('esc'):
#         print("you pressed esc")
#         break
#     else:
#         l_in_l = int(input("enter your value : "))
#         empty_list.append(l_in_l)  # استخدم 


# #  list in list  ليست في ليست مع بيانات متعددة ودراسة نوعها 
# print (type(l_in_l))
# print (l_in_l)
# print("**************\n\n")
# for item in l_in_l :
#     print(item)
#     print (type(item))
#     print("**************\n")


# print (empty_list)
# number_index =int( len(empty_list) )
# print (number_index)
# n_list = 'ahmmed'
# # تضيف عنصرًا جديدًا في موقع محدد داخل القائمة (حسب الفه
# empty_list.insert(number_index, n_list) # add item to the speacific inin
# # print (empty_list) # تضيف عنصرًا جديدًا في موقع محدد داخل القائمة (حسب الفهرس).
# print (type(n_list))

print ("**************** additon item from list ***************")



# print (listcolor) # تضيف عنصرًا جديدًا إلى نهاية القائمة.
# listcolor.append("pink") # add item to the end of the list
# print (listcolor)

# print (listfruit) #تضيف عنصرًا جديدًا في موقع محدد داخل القائمة (حسب الفهرس).
# listfruit.insert(0, "strawberry") # add item to the   speacific inin
# print (listfruit)

# print (listnumber) # تضيف عناصر متعددة (من قائمة أو مجموعة أخرى) إلى نهاية القائمة الأصلية.

# listnumber.extend([11 , 12 , 13 ]) # add item to the end of the list
# print (listnumber)

# listname += ['samer']
# print (listname)

# listname += ['rami']*5
# print (listname)

# listname  = listname + ['rami']*10
# print (listname)

# i = input ("enter the value of array : ")
# empty_list = empty_list + [i]*20
# print (empty_list)

# empty_list [0:2] = ['55' , '66' , '77' ]
# print (empty_list)
# print (empty_list[0:2])  #  في التغيير مشمول في الطباعة غير مشمول   ئ




# delete item from list : 
# print ("**************** delete item from list ***************")


# listcolor.remove("red")
# print ("listcolor",listcolor) # remove item from list  by value 

# listfruit.pop(3) # remove item from list  by index
# print ("listfruit",listfruit) 

# listnumber.pop() # remove the last item from the list 
# print ("listnumber", listnumber)

# del listfloat[0:2] # remove item from list  by index
# print ("listfloat",listfloat)

# listbool.clear() # remove all item from list
# print ("listbool",listbool) 

# # DELEDT ITEM IL LIST FROM LIST 

# del l_in_l[2:4]
# print ("l_in_l",l_in_l) # remove item from list  by value









# # listbool = [True , False , True ] # تعديل  وكأنها اضافة جديدة
# # print (listbool) 
# # listbool +=[False] # add item to the end of the list
# # print (listbool) 
# # listbool += [True]*3 # add item  * 3 times 
# # print (listbool) 

# # listfloat2 =[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
# # print (listfloat2)
# # print (listfloat)
# # listfloat = listfloat + listfloat2 # add list to list  # in the end
# # print (listfloat) # the list  قابلة للتغيير 


