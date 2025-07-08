# data stracter 
"""
هذا الملف يعتبر مرجعا في طرق التعامل مع الداتا ستركتشر لكل من 
list , array , np array , dict , tuple , set 
لكل من العمليات الاساسية 
الوصول - الاضافة - الحذف - التعديل - التحويل - عمليات خاصة 
تم تصميم هذا الملف بواسطة الذكاء الاصطناعي 

"""
from array import array
import numpy as np
import os
os.system ('cls')

def ma():
    print ("************************************************************************")
    print ("*"*20, " Defining variables for data  " , "*"*20)
    
    # list  
    listcolor = ["red", "green", "blue", "yellow", "black", "white"]
    listinlist =[ ['a' , 'b' , 'c'] , [1 , 2, 3 , 4 ] ,  [True , False ]] 
    
    # array 
    s_array = array ('i',[1,2,3,4,5,6,7,8,9])
    
    #numpy 
    np_array = np.array([1,2,3,4,5])
    np_2d = np.array([[1, 2, 3], [4, 5, 6]])
    np_3d = np.array([
                            [[1, 2, 3 , 4 ]    , [3, 4, 5 , 6]],
                            [[5, 6, 7 , 8 ]    , [7, 8 , 9 , 10 ]],
                            [[9 , 10 , 11 , 12], [11 , 12 , 13 , 14]]
                     ])
    
    # tuple
    mytuple = ("apple", "banana", "cherry")
    
    # dict
    mydict = {
                "name": "John",
                "age": 30,
                "city": "New York" 
        } 
    dictindict ={}
    dictindict[1] = {'name' : "kfc" , "price" : 50}
    dictindict[2] = {'name' : "pizaa" , "price" : 20}
    dictindict[3] = {'name' : "hartattak" , "price" : 100}

    # set 
    myset = {"rami", "rema", "ruba"}

    # print the data structures
    print ("listcolor :>>>\n", listcolor)
    print ("list in list :>>>\n" , listinlist)
    print  ("s_array:>>>\n", s_array)
    print ("np array:>>> \n", np_array)
    print("2D numpy array:\n", np_2d , np_2d.shape ,"......"  , np_2d.size  )
    #print (np_2d.size,"  ",  np_2d.shape)
    print("3D numpy array:\n", np_3d , np_3d.shape ,"......" , np_3d.size)
    #print (np_3d.size,"  ",  np_3d.shape)
    print ("mytuple:>>>\n", mytuple)
    print ("mydict:>>>\n", mydict)
    print ("dict in dict >>>\n " , dictindict)
    print ("my set : >>>\n", myset)
    input (" press any key to cont...........")
    os.system ("cls")
    
    
    print ("***********************************************")
    print ("*"*20, "index" , "*"*20)
    print ("*"*20, "1 - list " , "*"*20)
    
    # القائمة الأصلية قبل عمليات الاضافة
    print ("listcolor :>>>\n", listcolor, "\n\n")
    # indexing and accessing elements    الوصول للعناصر 
    # الوصول إلى عنصر واحد بالاندكس
    print("1- listcolor[0] ", listcolor[0])  # العنصر الأول
    # الوصول إلى آخر عنصر
    print("2- listcolor[-1]", listcolor[-1])
    # الوصول إلى مجموعة عناصر باستخدام Slicing
    print("3- listcolor[1:4]", listcolor[1:4])  # من  الثاني للرابع (لا يشمل 4)
    # الوصول إلى العناصر من البداية حتى اندكس معين
    print("4- listcolor[:3]",listcolor[:3])  # أول ثلاثة عناصر
    # الوصول إلى العناصر من اندكس معين للنهاية
    print("5- listcolor[2:]",listcolor[2:])  # من العنصر الثالث حتى الأخير
    # الوصول إلى كل عنصرين (تخطي عنصر)
    print("6- listcolor[::2]",listcolor[::2])
    # الوصول إلى العناصر بالعكس
    print("7- listcolor[::-1]",listcolor[::-1])
    # الوصول إلى عنصر باستخدام متغير اندكس
    index = 3
    print("8- listcolor[index]",listcolor[index])
    # الوصول إلى عنصر باستخدام دالة next مع filter
    print ('9- next(filter(lambda x: x == "blue", listcolor), None) ')
    print(next(filter(lambda x: x == "blue", listcolor), None))
    # الوصول إلى عنصر باستخدام دالة index (ترجع موقع العنصر)
    print('10- listcolor[idx] // idx = listcolor.index("green")  ')
    idx = listcolor.index("green")
    print (listcolor[idx])
    # الوصول إلى مجموعة عناصر باستخدام list comprehension
    subset = [color for color in listcolor if "e" in color]
    print('11- subset = [color for color in listcolor if "e" in color] \n',subset)
    
    # new list have include list : 
        # listinlist =[ ['a' , 'b' , 'c'] , [1 , 2, 3 , 4 ] ,  [True , False ]]
    print ("\n12- list in list =  ",listinlist )

    #        للوصول للعنصر          داخل القائمة الداخلية:
   
    print("13- listinlist [2][1] ",listinlist [2][1])  # الناتج: 4
    i = 0 
    for item in listinlist  :
        print ( f" item[{i}] in list " , item)
        i+=1
    for item in listinlist : 
        for subitem in item:
            print (subitem, end='  ...  ')
    print ("\n14- len(listinlist) : ", len(listinlist))

    input ("press any key to cont.........")
    os.system ("cls")
    
    print ("***********************************************")
    ####    ****************************************     ####
    print ("*"*20, "index" , "*"*20)
    print ("*"*20, "2 - array " , "*"*20)
    # المصفوفة الأصلية قبل عمليات التغيير 
    print (s_array)
    # الوصول إلى عنصر واحد بالاندكس
    print("1- s_array[1] : ",s_array[1])  # العنصر الثاني
    # الوصول إلى آخر عنصر
    print("2- s_array[-1] :",s_array[-1])
    # الوصول إلى مجموعة عناصر باستخدام Slicing
    print("3- s_array[2:5] : ",s_array[2:5])  # من العنصر الثالث للخامس (لا يشمل الخامس)
    # الوصول إلى العناصر من البداية حتى اندكس معين
    print("4- s_array[:4] : ",s_array[:4])  # أول أربعة عناصر
    # الوصول إلى العناصر من اندكس معين للنهاية
    print("5- s_array[3:] : ",s_array[3:])  # من العنصر الرابع حتى الأخير
    # الوصول إلى كل عنصرين (تخطي عنصر)
    print("6- s_array[::2] : ",s_array[::2])
    # الوصول إلى العناصر بالعكس
    print("7- s_array[::-1] : ",s_array[::-1])
    # الوصول إلى عنصر باستخدام متغير اندكس
    index = 4
    print("8- s_array[index] : ",s_array[index])
    # الوصول إلى عنصر باستخدام حلقة for
    print("9- all item in array : ")
    for item in s_array:
        print(item, end= '    ')
    print()
    #                الوصول إلى مجموعة عناصر باستخدام شروط معينة           
    subset = [x for x in s_array if x % 2 == 0]
    print("10- [x for x in s_array if x % 2 == 0] : ",subset)
    print (type(subset))

    input ("press any key to cont.........")
    os.system ("cls")
    
    
    print ("***********************************************")
    ####    ****************************************     ####
    print ("*"*20, "index" , "*"*20)
    print("*" * 20, "3 - numpy 2D & 3D array", "*" * 20)
    # إنشاء مصفوفة numpy ثنائية الأبعاد (2D)
    print("1- 2D numpy array:\n", np_2d)
    print("2- Shape of 2D array:", np_2d.shape)
    # إنشاء مصفوفة numpy ثلاثية الأبعاد (3D)
    print("3- 3D numpy array:\n", np_3d)
    print("4- Shape of 3D array: ", np_3d.shape)
    
    # مصفوفة ثنائية الأبعاد (2D)
    print("*" * 20, " numpy 2D  access ", "*" * 20)
    print("1- Element at row 1, column 2:", np_2d[0, 1])  # الصف الأول، العمود الثاني
    print("2- Last row:", np_2d[-1])
    print("3- Last element in last row:", np_2d[-1, -1])
    print("4- Entire column:", np_2d[:, 1])  # كل الصفوف، العمود الثاني
    print("5- Entire row:", np_2d[1, :])    # الصف الثاني، كل الأعمدة
    print("6- Slice of elements:", np_2d[0:2, 1:3])  # من الصف 0 إلى 1، من العمود 1 إلى 2
    # الوصول باستخدام متغيرات اندكس
    row, col = 1, 2
    print("7- Element using index variables:", np_2d[row, col])
    # الوصول باستخدام حلقة for
    print("8-")
    for i in range(np_2d.shape[0]):
        for j in range(np_2d.shape[1]):
            print(f"[{i},{j}] = {np_2d[i,j]}",end = ' ') 
               
    print ()
    print("*" * 20, " numpy 3d  access ", "*" * 20)
    
    # مصفوفة ثلاثية الأبعاد (3D)
    print("1- Element at dimension 0, row 1, column 0:", np_3d[0, 1, 0])
    print("2- Last element:", np_3d[-1, -1, -1])
    print("3- All elements in dimension 1:", np_3d[1])
    print("4- All elements in row 0 of dimension 0:", np_3d[0, 0, :])
    print("5- Slice of elements:", np_3d[:, 0, :])  # كل الأبعاد، الصف 0، كل الأعمدة
    # الوصول باستخدام متغيرات اندكس
    d, r, c = 1, 0, 1
    print("6- Element using index variables:", np_3d[d, r, c])
    # الوصول باستخدام حلقة for ثلاثية الأبعاد
    print("7- all item in array ")
    for i in range(np_3d.shape[0]):
        for j in range(np_3d.shape[1]):
            for k in range(np_3d.shape[2]):
                print(f"{np_3d[i,j,k]} = [{i},{j},{k}]  ",end = ' ')
    print ()
    input ("press any key to cont.........")
    os.system ("cls")

    print ("***********************************************")
    ####    ****************************************     ####
    print ("*"*20, "index" , "*"*20)
    print ("*"*20, "4 - tuple " , "*"*20)
    # التيوب الأصلية قبل عمليات الاضافة
    print ("\n mytuple : ", mytuple , "\n")

    # الوصول إلى عنصر واحد بالاندكس
    print("1- mytuple[1] :  ", mytuple[1])  # العنصر الثاني
    # الوصول إلى آخر عنصر
    print("2- mytuple[-1] : ", mytuple[-1])
    # الوصول إلى مجموعة عناصر باستخدام Slicing
    print("3- mytuple[1:3] : ", mytuple[1:3])  # من العنصر الثاني للثالث (لا يشمل الثالث)
    # الوصول إلى العناصر من البداية حتى اندكس معين
    print("4- mytuple[:2] : ", mytuple[:2])  # أول عنصرين
    # الوصول إلى العناصر من اندكس معين للنهاية
    print("5- mytuple[2:] : ", mytuple[2:])  # من العنصر الثالث حتى الأخير
    # الوصول إلى كل عنصرين (تخطي عنصر)
    print("6- mytuple[::2] : ", mytuple[::2])
    # الوصول إلى العناصر بالعكس
    print("7- mytuple[::-1] : ", mytuple[::-1])
    # الوصول إلى عنصر باستخدام متغير اندكس
    index = 0
    print("8- mytuple[index] : ", mytuple[index])
    # الوصول إلى عنصر باستخدام حلقة for
    print("9- all item in mytuple : ")
    for item in mytuple:
        print(item, end=' ...... ')
    print()
    # الوصول إلى مجموعة عناصر باستخدام tuple comprehension (عن طريق تحويل إلى قائمة مؤقتاً)
    subset = tuple(x for x in mytuple if "a" in x)
    print('10- tuple(x for x in mytuple if "a" in x) ', subset)
    
    input ("press any key to cont ........")
    os.system("cls")
    
    
    print ("***********************************************")
    ####    ****************************************     ####
    print ("*"*20, "index" , "*"*20)
    print ("*"*20, "5 - dict " , "*"*20)
    print ("this is the main dict : ", mydict)
    # الوصول إلى عنصر باستخدام المفتاح مباشرة
    print('1- mydict["age"] : ' , mydict["age"])
    # الوصول إلى عنصر باستخدام get (لا يعطي خطأ إذا لم يوجد المفتاح)
    print('2-mydict.get("city") :', mydict.get("city"))
    print("3-", mydict.get("salary"," NOT FOUND "))
    # الوصول إلى جيمع المفاتيح 
    print("4- list(mydict.keys()) : ", list(mydict.keys())) # هنا أصبحت list 
    # الوصول إلى جميع القيم
    print("5- list(mydict.values()) : ", list(mydict.values())) # هنا أصبحت list 
    # الوصول إلى list(mydict.items()))
    # الوصول إلى عنصر باستخدام متغير مفتاح
    key = "name"
    print("6- mydict[key] : ", mydict[key])
    # الوصول إلى عنصر باستخدام حلقة for على المفاتيح
    print("7- all item in mydict :  ")
    for k in mydict:
        print(f"{k}: {mydict[k]}")
    # الوصول إلى عنصر باستخدام حلقة for على items
    print("8- all item and value in mydict : ")
    for k, v in mydict.items():
        print(f"{k} => {v}")
    # الوصول إلى مجموعة عناصر تحقق شرط معين (dictionary comprehension)
    print("9- {k: v for k, v in mydict.items() if isinstance(v, str)} ")
    subset = {k: v for k, v in mydict.items() if isinstance(v, str)}
    print(subset)
    # الوصول إلى أول عنصر (من Python 3.7+ القواميس مرتبة)
    print("10- ")
    first_key = next(iter(mydict))
    print(f"First key: {first_key}, value: {mydict[first_key]}")
    # الوصول إلى آخر عنصر
    print("11-")
    last_key = list(mydict.keys())[-1]
    print(f"Last key: {last_key}, value: {mydict[last_key]}")
    # إنشاء dict داخل dict
    print("12-")
    mydict["address"] = {
        "street": "5th Avenue",
        "zipcode": "10001",
        "country": "USA"
    }
    print("mydict with nested dict:", mydict)
    # الوصول إلى dict الداخلي مباشرة
    print("13-",mydict["address"])
    # الوصول إلى عنصر داخلي باستخدام تسلسل المفاتيح
    print("14-",mydict["address"]["street"])
    # الوصول إلى عنصر داخلي باستخدام get المتسلسل
    print("15-",mydict.get("address", {}).get("zipcode"))
    # الوصول إلى جميع المفاتيح في dict الداخلي
    print("16-",list(mydict["address"].keys()))
    # الوصول إلى جميع القيم في dict الداخلي
    print("17-",list(mydict["address"].values()))
    # الوصول إلى جميع العناصر (مفتاح وقيمة) في dict الداخلي
    print("18-")
    for k, v in mydict["address"].items():
        print(f"{k}: {v}")
    # الوصول إلى عنصر داخلي باستخدام متغير مفتاح
    key = "country"
    print("19-",mydict["address"][key])
    # هذه قاموس داخل قاموس 
    print ("20- dict in dict : ", dictindict)
    # الوصول إلى كل العناصر في dictindict
    print("21-  all item in dictindict:")
    for key, value in dictindict.items():
        print(f"{key}: {value}")


    input ("press any key to cont ........")
    os.system("cls")
    

    
    print ("***********************************************")
    ####    ****************************************     ####
    print ("*"*20, "index" , "*"*20)
    print ("*"*20, "6 - set " , "*"*20)
    # الوصول إلى عنصر في set
    print (" this is the main set " , myset)
    # لا يمكن الوصول للعناصر في set بالاندكس مباشرة لأنها غير مرتبة
    # لكن يمكن تحويلها إلى قائمة أو استخدام حلقة for
    # 1. تحويل set إلى قائمة للوصول بالاندكس
    set_as_list = list(myset)
    print("1-" , "First element in set (after converting to list):", set_as_list[0])
    # 2. Access the first element using next with iter
    first_item = next(iter(myset))
    print("2-","First element in set using iter:", first_item)
    # 3. Access all elements using a for loop
    for item in myset:
        print("3-","Element in set:", item)
    # 4. Access elements that meet a condition using set comprehension
    subset = {x for x in myset if "a" in x}
    print("4-","Elements containing the letter 'a':", subset)
    input (" press any key to cont...........")
    os.system ("cls")
    """   

    ( اضافة البيانات في هياكل البيانات )   الآن بداية جديدة 

    """
    print ("***********************************************************")
    ####    ****************************************     ####
    print ("*"*20, "add" , "*"*20)
    print ("*"*20, "1- list " , "*"*20)
    # list  
    # Adds a single item to the end of the list
    listcolor.append("silver")
    print("1- After append: 'silver'\n", listcolor)
    # Inserts an item at a specific index
    listcolor.insert(2, "gold")
    print("2- After insert at index 2:\n", listcolor)
    # Extends the list by appending elements from another iterable
    listcolor.extend(["maroon", "olive"])
    print("3- After extend:\n", listcolor)
    # Concatenates another list using +
    listcolor = listcolor + ["navy"]
    print("4- useing + way to add item :\n", listcolor)
    # Adds multiple items using += operator
    listcolor += ["teal", "lime"]
    print("5- useing + way to add list items :\n", listcolor)
    # Inserts multiple items at a specific position using slice assignment
    listcolor[1:1] = ["aqua", "fuchsia"]
    print("6- to add list to list ' as extend ' in Specific location :\n", listcolor)
    # Unpacks another list into the current list at a specific position
    listcolor[3:3] = [*["indigo", "violet"]]
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    ####    ****************************************     ####
    print ("*"*20, "add" , "*"*20)
    print ("*"*20, "2- array " , "*"*20)
    # Using append() to add a single element at the end
    s_array.append(10)
    print("1- After append:\n", s_array)
    # Using extend() to add multiple elements (must be iterable)
    s_array.extend([11, 12])
    print("2- After extend:\n", s_array)
    # Using fromlist() to add elements from a list
    s_array.fromlist([13, 14])
    print("3- After fromlist:\n", s_array)
    # Using insert() to add an element at a specific position
    s_array.insert(0, 0)
    print("4- After insert at index 0:\n", s_array)
    
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    ####    ****************************************     ####
    print ("*"*20, "add" , "*"*20)
    print ("*"*20, "3- numpy array " , "*"*20)

    # 1. Using append() from numpy (returns a new array)
    np_array = np.append(np_array, 6)
    print("1- After np.append (single item):\n", np_array)
    # 2. Using append() to add multiple elements (returns a new array)
    np_array = np.append(np_array, [7, 8])
    print("2- After np.append (multiple items):\n", np_array)
    # 3. Using concatenate() to join arrays
    np_array = np.concatenate((np_array, np.array([9, 10])))
    print("3- After np.concatenate:\n", np_array)
    # 4. Using insert() to add an element at a specific index (returns a new array)
    np_array = np.insert(np_array, 0, 0)
    print("4- After np.insert at index 0:\n", np_array)
    # 5. Using hstack() to add elements horizontally (returns a new array)
    np_array = np.hstack((np_array, [11, 12]))
    print("5- After np.hstack:\n", np_array)
    # 6. Using vstack() to stack as new rows (creates 2D array)
    # يجب التأكد أن طول المصفوفتين متساوي
    row_to_stack = np.array([13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
    # ضبط طول np_array ليطابق طول row_to_stack
    if np_array.shape[0] != row_to_stack.shape[0]:
        np_array = np.resize(np_array, row_to_stack.shape[0])
    np_array_2d = np.vstack((np_array, row_to_stack))
    print("6- After np.vstack (2D array):\n", np_array_2d)
    # 7. Using resize() to increase size and assign new values
    np_array = np.resize(np_array, np_array.size + 2)
    np_array[-2:] = [25, 26]
    print("7- After np.resize and assign:", np_array)
    
    input (" press any key to cont...........")
    os.system ("cls")
    
    print ("************************************************")
    ####    ****************************************     ####
    print ("*"*20, "add" , "*"*20)
    print ("*"*20, "4- tuple " , "*"*20)
    # Tuples are immutable, so you cannot add elements directly.
    # But you can create a new tuple by concatenation:
    # 1. Using + operator to add a single element (as a tuple)
    mytuple = mytuple + ("orange",)
    print("After adding one item:\n", mytuple)
    # 2. Using + operator to add multiple elements (as a tuple)
    mytuple = mytuple + ("grape", "melon")
    print("After adding multiple items:\n", mytuple)
    # 3. Using unpacking to add elements at a specific position
    mytuple = mytuple[:1] + ("kiwi",) + mytuple[1:]
    print("After inserting at index 1:\n", mytuple)
    # 4. Converting to list, adding, then converting back to tuple
    temp = list(mytuple)
    temp.append("pear")
    mytuple = tuple(temp)
    print("After append using list conversion:\n", mytuple)
    # 5. Using tuple unpacking to merge tuples
    mytuple = (*mytuple, "plum")
    print("After unpacking and adding one item:\n", mytuple)
    # 6. Using sum() to concatenate tuples (not common, but possible)
    mytuple = sum([(mytuple), ("mango",)], ())
    print("After using sum to add one item:\n", mytuple)

    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    ####    ****************************************     ####
    print ("*"*20, "add" , "*"*20) 
    print ("*"*20, "5- dict " , "*"*20)

    # 1. Using assignment to add a new key-value pair
    mydict["country"] = "USA"
    print("After assignment:\n", mydict)
    # 2. Using update() to add one or more key-value pairs
    mydict.update({"email": "john@example.com"})
    print("After update with one item:\n", mydict)
    # 3. Using update() with multiple items
    mydict.update({"phone": "123456", "gender": "male"})
    print("After update with multiple items:\n", mydict)
    # 4. Using setdefault() to add a key with a default value if it doesn't exist
    mydict.setdefault("nickname", "Johnny")
    print("After setdefault (new key):\n", mydict)
    # 5. Using dictionary unpacking (Python 3.5+)
    mydict = {**mydict, "hobby": "reading"}
    print("After unpacking:\n", mydict)
    # 6. Using the | operator (Python 3.9+)
    mydict = mydict | {"status": "active"}
    print("After using | operator:\n", mydict)
    
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    ####    ****************************************     ####
    print ("*"*20, "add" , "*"*20) 
    print ("*"*20, "6- set " , "*"*20)
    # 1. Using add() to add a single element
    print (myset)
    myset.add("orange")
    print("After add: ( orange ) \n", myset)
    # 2. Using update() to add multiple elements from an iterable (list, tuple, set)
    myset.update(["grape", "melon"])
    print("After update with list:\n", myset)
    myset.update(("kiwi", "pear"))
    print("After update with tuple:\n", myset)
    myset.update({"plum", "mango"})
    print("After update with another set:\n", myset)
    # 3. Using |= operator to add elements from another set
    myset |= {"papaya", "peach"}
    print("After |= operator:\n", myset)
    # 4. Using union() to create a new set with added elements (does not modify original)
    newset = myset.union(["cherry", "banana"])
    print("After union (original set unchanged):\n", myset)
    print("New set after union:\n", newset)
    # 5. Using unpacking to merge sets (Python 3.5+)
    myset = { *myset, "apricot", "fig" }
    print ("************************************************")
 
    input (" press any key to cont...........")
    os.system ("cls")



    print ("************************************************")
    ####    ****************************************     ####
    print ("*"*20, "remove" , "*"*20)
    print ("*"*20, "1- list " , "*"*20)
    # 1. Using remove() to delete by value (first occurrence)
    listcolor.remove("gold")
    print("1- After remove 'gold':\n", listcolor)
    # 2. Using pop() to delete by index (default last)
    popped = listcolor.pop()
    print("2- After pop (last item):\n", listcolor, " -- popped:", popped)
    # 3. Using pop(index) to delete by specific index
    popped = listcolor.pop(2)
    print("3- After pop at index 2:\n", listcolor, " -- popped:", popped)
    # 4. Using del to delete by index or slice
    del listcolor[0]
    print("4- After del index 0:\n", listcolor)
    del listcolor[1:3]
    print("5- After del slice 1:3:\n", listcolor)
    # 5. Using clear() to remove all items
    temp = listcolor.copy()
    temp.clear()
    print("6- After clear():\n", temp)
    # 6. Using list comprehension to filter items
    filtered = [x for x in listcolor if "a" not in x]
    print("7- After list comprehension (remove items with 'a'):\n", filtered)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "remove" , "*"*20)
    print ("*"*20, "2- array " , "*"*20)
    # 1. Using remove() to delete by value (first occurrence)
    s_array.remove(10)
    print("1- After remove 10:\n", s_array)
    # 2. Using pop() to delete by index (default last)
    popped = s_array.pop()
    print("2- After pop (last item):\n", s_array, " -- popped:", popped)
    # 3. Using pop(index) to delete by specific index
    popped = s_array.pop(0)
    print("3- After pop at index 0:\n", s_array, " -- popped:", popped)
    # 4. Using del to delete by index or slice
    del s_array[1]
    print("4- After del index 1:\n", s_array)
    # 5. Using array slicing to filter items (create new array)
    filtered = array('i', [x for x in s_array if x > 5])
    print("5- After filtering (x > 5):\n", filtered)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "remove" , "*"*20)
    print ("*"*20, "3- numpy array " , "*"*20)
    # 1. Using delete() to remove by index (returns new array)
    np_array = np.delete(np_array, 0)
    print("1- After np.delete index 0:\n", np_array)
    # 2. Using boolean indexing to filter
    np_array = np_array[np_array != 25]
    print("2- After boolean indexing (remove 25):\n", np_array)
    # 3. Using where() to get indices and delete
    idx = np.where(np_array == 26)[0]
    if idx.size > 0:
        np_array = np.delete(np_array, idx)
    print("3- After np.where and delete (remove 26):\n", np_array)
    # 4. Using slicing to remove a range
    np_array = np_array[:-2]
    print("4- After slicing (remove last 2):\n", np_array)
    # 5. Using clear() on numpy array (not available, use resize to 0)
    np_array = np.resize(np_array, 0)
    print("5- After resize to 0 (clear):\n", np_array)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "remove" , "*"*20)
    print ("*"*20, "4- tuple " , "*"*20)
    # Tuples are immutable, so you cannot remove elements directly.
    # 1. Convert to list, remove, then convert back
    temp = list(mytuple)
    temp.remove("orange")
    mytuple = tuple(temp)
    print("1- After remove 'orange' using list conversion:\n", mytuple)
    # 2. Remove by index using list conversion
    temp = list(mytuple)
    del temp[0]
    mytuple = tuple(temp)
    print("2- After del index 0 using list conversion:\n", mytuple)
    # 3. Remove multiple items using list comprehension
    mytuple = tuple(x for x in mytuple if "a" not in x)
    print("3- After tuple comprehension (remove items with 'a'):\n", mytuple)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "remove" , "*"*20)
    print ("*"*20, "5- dict " , "*"*20)
    # 1. Using pop() to remove by key
    mydict.pop("country", None)
    print("1- After pop 'country':\n", mydict)
    # 2. Using del to remove by key
    del mydict["email"]
    print("2- After del 'email':\n", mydict)
    # 3. Using popitem() to remove last inserted item
    popped = mydict.popitem()
    print("3- After popitem (last item):\n", mydict, " -- popped:", popped)
    # 4. Using clear() to remove all items
    temp = mydict.copy()
    temp.clear()
    print("4- After clear():\n", temp)
    # 5. Using dictionary comprehension to filter items
    filtered = {k: v for k, v in mydict.items() if k != "phone"}
    print("5- After dict comprehension (remove 'phone'):\n", filtered)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "remove" , "*"*20)
    print ("*"*20, "6- set " , "*"*20)
    # 1. Using remove() to delete by value
    myset.remove("orange")
    print("1- After remove 'orange':\n", myset)
    # 2. Using discard() to delete by value (no error if not found)
    myset.discard("kiwi")
    print("2- After discard 'kiwi':\n", myset)
    # 3. Using pop() to remove and return an arbitrary element
    popped = myset.pop()
    print("3- After pop (arbitrary item):\n", myset, " -- popped:", popped)
    # 4. Using difference_update() to remove multiple items
    myset.difference_update({"plum", "mango"})
    print("4- After difference_update (remove 'plum', 'mango'):\n", myset)
    # 5. Using clear() to remove all items
    temp = myset.copy()
    temp.clear()
    print("5- After clear():\n", temp)
    # 6. Using set comprehension to filter items
    filtered = {x for x in myset if "a" not in x}
    print("6- After set comprehension (remove items with 'a'):\n", filtered)
    print ("************************************************")

    input (" press any key to cont...........")
    os.system ("cls")


    print ("************************************************")
    ####    ****************************************     ####
    print ("*"*20, "update" , "*"*20)
    print ("*"*20, "1- list " , "*"*20)
    # 1. Update by index
    listcolor[0] = "pink"
    print("1- After update index 0 to 'pink':\n", listcolor)
    # 2. Update a slice
    listcolor[1:3] = ["cyan", "magenta"]
    print("2- After update slice 1:3:\n", listcolor)
    # 3. Update using a loop (replace all 'e' with 'E')
    listcolor = [x.replace('e', 'E') for x in listcolor]
    print("3- After replace 'e' with 'E' in all items:\n", listcolor)
    # 4. Update using list comprehension with condition
    listcolor = [x.upper() if "a" in x else x for x in listcolor]
    print("4- After upper() for items containing 'a':\n", listcolor)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "update" , "*"*20)
    print ("*"*20, "2- array " , "*"*20)
    # 1. Update by index
    s_array[0] = 100
    print("1- After update index 0 to 100:\n", s_array)
    # 2. Update a slice
    s_array[1:3] = array('i', [200, 300])
    print("2- After update slice 1:3:\n", s_array)
    # 3. Update using a loop (multiply all by 2)
    for i in range(len(s_array)):
        s_array[i] *= 2
    print("3- After multiply all items by 2:\n", s_array)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "update" , "*"*20)
    print ("*"*20, "3- numpy array " , "*"*20)
    # reset np_array to a new array for demonstration
    np_array = np.array([1, 2, 3, 4, 5])    

    # 1. Update by index
    np_array[0] = 999
    print("1- After update index 0 to 999:\n", np_array)
    # 2. Update a slice
    np_array[1:3] = [888, 777]
    print("2- After update slice 1:3:\n", np_array)
    # 3. Update using boolean indexing (set all > 500 to 0)
    np_array[np_array > 500] = 0
    print("3- After set all > 500 to 0:\n", np_array)
    # 4. Update using vectorized operation (add 10 to all)
    np_array = np_array + 10
    print("4- After add 10 to all items:\n", np_array)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "update" , "*"*20)
    print ("*"*20, "4- tuple " , "*"*20)
    # Tuples are immutable, so you cannot update elements directly.
    # 1. Convert to list, update, then convert back
    temp = list(mytuple)
    temp[0] = "lemon"
    mytuple = tuple(temp)
    print("1- After update index 0 to 'lemon' using list conversion:\n", mytuple)
    # 2. Update multiple items using list comprehension
    mytuple = tuple(x.upper() if "e" in x else x for x in mytuple)
    print("2- After upper() for items containing 'e':\n", mytuple)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "update" , "*"*20)
    print ("*"*20, "5- dict " , "*"*20)
    # 1. Update value by key
    mydict["name"] = "Alice"
    print("1- After update 'name' to 'Alice':\n", mydict)
    # 2. Update multiple values using update()
    mydict.update({"age": 40, "city": "Los Angeles"})
    print("2- After update age and city:\n", mydict)
    # 3. Update using dictionary comprehension (capitalize all string values)
    mydict = {k: (v.capitalize() if isinstance(v, str) else v) for k, v in mydict.items()}
    print("3- After capitalize all string values:\n", mydict)
    input (" press any key to cont...........")
    os.system ("cls")

    print ("************************************************")
    print ("*"*20, "update" , "*"*20)
    print ("*"*20, "6- set " , "*"*20)
    # Sets are unordered, but you can remove and add to "update" values
    # 1. Remove an item and add a new one
    myset.discard("ruba")
    myset.add("sara")
    print("1- After discard 'ruba' and add 'sara':\n", myset)
    # 2. Update all items (replace all with upper case)
    myset = {x.upper() for x in myset}
    print("2- After upper() for all items:\n", myset)
    # 3. Update using set comprehension (add 'VIP' to all names)
    myset = {x + "_VIP" for x in myset}
    print("3- After add '_VIP' to all items:\n", myset)
    print ("************************************************")

    input (" press any key to cont...........")
    os.system ("cls")



    print ("************************************************")
    ####    ****************************************     ####
    print ("*"*20, "convert" , "*"*20)
    print ("*"*20, "   <->   " , "*"*20)

    # 1. list to array
    arr_from_list = array('u', ''.join(listcolor)) if all(isinstance(x, str) and len(x) == 1 for x in listcolor) else array('u', 'a')  # for demo, array of unicode chars
    print("1- list to array (demo, chars):\n", arr_from_list)

    # 2. list to numpy array
    np_from_list = np.array(listcolor)
    print("2- list to numpy array:\n", np_from_list)

    # 3. list to tuple
    tuple_from_list = tuple(listcolor)
    print("3- list to tuple:\n", tuple_from_list)

    # 4. list to set
    set_from_list = set(listcolor)
    print("4- list to set:\n", set_from_list)

    # 5. array to list
    list_from_array = list(s_array)
    print("5- array to list:\n", list_from_array)

    # 6. array to numpy array
    np_from_array = np.array(s_array)
    print("6- array to numpy array:\n", np_from_array)

    # 7. numpy array to list
    list_from_np = np_array.tolist()
    print("7- numpy array to list:\n", list_from_np)

    # 8. numpy array to tuple
    tuple_from_np = tuple(np_array)
    print("8- numpy array to tuple:\n", tuple_from_np)

    # 9. tuple to list
    list_from_tuple = list(mytuple)
    print("9- tuple to list:\n", list_from_tuple)

    # 10. tuple to set
    set_from_tuple = set(mytuple)
    print("10- tuple to set:\n", set_from_tuple)

    # 11. set to list
    list_from_set = list(myset)
    print("11- set to list:\n", list_from_set)

    # 12. set to tuple
    tuple_from_set = tuple(myset)
    print("12- set to tuple:\n", tuple_from_set)

    # 13. dict to list of keys
    keys_list = list(mydict.keys())
    print("13- dict to list of keys:\n", keys_list)

    # 14. dict to list of values
    values_list = list(mydict.values())
    print("14- dict to list of values:\n", values_list)

    # 15. dict to list of items (tuples)
    items_list = list(mydict.items())
    print("15- dict to list of items:\n", items_list)

    # 16. list of tuples to dict
    dict_from_items = dict(items_list)
    print("16- list of tuples to dict:\n", dict_from_items)

    # 17. list of pairs to dict (if possible)
    pairs = [("a", 1), ("b", 2)]
    dict_from_pairs = dict(pairs)
    print("17- list of pairs to dict:\n", dict_from_pairs)

    # 18. set to numpy array
    np_from_set = np.array(list(myset))
    print("18- set to numpy array:\n", np_from_set)

    # 19. numpy array to set
    set_from_np = set(np_array)
    print("19- numpy array to set:\n", set_from_np)

    # 20. list to dict (using enumerate)
    dict_from_list = dict(enumerate(listcolor))
    print("20- list to dict (index as key):\n", dict_from_list)


    input (" press any key to cont...........")
    os.system ("cls")
    
    print ("*"*20, "check data type " , "*"*20)

    # 1. استخدام isinstance للفحص مع شرط
    print("7- isinstance(listcolor, list):", isinstance(listcolor, list))
    print("8- isinstance(s_array, array):", isinstance(s_array, array))
    print("9- isinstance(np_array, np.ndarray):", isinstance(np_array, np.ndarray))
    print("10- isinstance(mytuple, tuple):", isinstance(mytuple, tuple))
    print("11- isinstance(mydict, dict):", isinstance(mydict, dict))
    print("12- isinstance(myset, set):", isinstance(myset, set))

    # 2. فحص نوع متغير عام
    variable = (1,2,3)
    print("13- type(variable):", type(variable))
    if isinstance(variable, tuple):
        print("14- variable is a tuple")
    else : 
        print ("14 variable is not a tuple")


