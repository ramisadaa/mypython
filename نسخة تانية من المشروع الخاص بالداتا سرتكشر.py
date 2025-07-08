with open('file.py', 'r') as f:
    lines = f.readlines()


# tuple
mytuple = ("apple", "banana", "cherry")
# dict
mydict = {
             "name": "John",
             "age": 30,
             "city": "New York" 
      }   
# set 
myset = {"rami", "rema", "ruba"}

# print the data structures
print ("listcolor :>>>\n", listcolor)
print  ("s_array:>>>\n", s_array)
print ("np array:>>> \n", np_array)
print("2D numpy array:\n", np_2d , np_2d.shape ,"......"  , np_2d.size  )
#print (np_2d.size,"  ",  np_2d.shape)
print("3D numpy array:\n", np_3d , np_3d.shape ,"......" , np_3d.size)
#print (np_3d.size,"  ",  np_3d.shape)
print ("mytuple:>>>\n", mytuple)
print ("mydict:>>>\n", mydict)
print ("my set : >>>\n", myset)


input (" press any key to cont...........")
os.system ("cls")


print ("***********************************************")
####    ****************************************     ####
print ("*"*20, "index" , "*"*20)
print ("*"*20, "list " , "*"*20)
# القائمة الأصلية قبل عمليات الاضافة
print ("listcolor :>>>\n", listcolor, "\n\n")

# indexing and accessing elements    الوصول للعناصر 
# الوصول إلى عنصر واحد بالاندكس
print("1-", listcolor[1])  # العنصر الثاني

# الوصول إلى آخر عنصر
print("2-", listcolor[-1])

# الوصول إلى مجموعة عناصر باستخدام Slicing
print("3-", listcolor[1:4])  # من العنصر الثاني للرابع (لا يشمل الرابع)

# الوصول إلى العناصر من البداية حتى اندكس معين
print("4-",listcolor[:3])  # أول ثلاثة عناصر

# الوصول إلى العناصر من اندكس معين للنهاية
print("5-",listcolor[2:])  # من العنصر الثالث حتى الأخير

# الوصول إلى كل عنصرين (تخطي عنصر)
print("6-",listcolor[::2])

# الوصول إلى العناصر بالعكس
print("7-",listcolor[::-1])

# الوصول إلى عنصر باستخدام متغير اندكس
index = 3
print("8-",listcolor[index])

# الوصول إلى عنصر باستخدام دالة next مع filter
print ("9-")
print(next(filter(lambda x: x == "blue", listcolor), None))

# الوصول إلى عنصر باستخدام دالة index (ترجع موقع العنصر)
idx = listcolor.index("green")
print("10-",listcolor[idx])

# الوصول إلى مجموعة عناصر باستخدام list comprehension
subset = [color for color in listcolor if "e" in color]
print("11-",subset)

# new list have include list : 
mylist = [1, 2, [3, 4, 5], 6]
# للوصول للعنصر 4 داخل القائمة الداخلية:
element = mylist[2][1]
print("12-",element)  # الناتج: 4

input ("press any key to cont.........")
os.system ("cls")


print ("***********************************************")
####    ****************************************     ####
print ("*"*20, "index" , "*"*20)
print ("*"*20, "array " , "*"*20)
# المصفوفة الأصلية قبل عمليات التغيير 
print (s_array)

# الوصول إلى عنصر واحد بالاندكس
print("1-",s_array[1])  # العنصر الثاني

# الوصول إلى آخر عنصر
print("2-",s_array[-1])

# الوصول إلى مجموعة عناصر باستخدام Slicing
print("3-",s_array[2:5])  # من العنصر الثالث للخامس (لا يشمل الخامس)

# الوصول إلى العناصر من البداية حتى اندكس معين
print("4-",s_array[:4])  # أول أربعة عناصر

# الوصول إلى العناصر من اندكس معين للنهاية
print("5-",s_array[3:])  # من العنصر الرابع حتى الأخير

# الوصول إلى كل عنصرين (تخطي عنصر)
print("6-",s_array[::2])

# الوصول إلى العناصر بالعكس
print("7-",s_array[::-1])

# الوصول إلى عنصر باستخدام متغير اندكس
index = 4
print("8-",s_array[index])

# الوصول إلى عنصر باستخدام حلقة for
print("9-")
for item in s_array:
    print(item, end= '      ')
print()

# الوصول إلى مجموعة عناصر باستخدام list comprehension
subset = [x for x in s_array if x % 2 == 0]
print("10-",subset)
print (type(subset))


input ("press any key to cont.........")
os.system ("cls")
print ("***********************************************")
####    ****************************************     ####
print ("*"*20, "index" , "*"*20)
print("*" * 20, "numpy 2D & 3D array", "*" * 20)
# إنشاء مصفوفة numpy ثنائية الأبعاد (2D)
print("2D numpy array:\n", np_2d)
print("Shape of 2D array:", np_2d.shape)
# إنشاء مصفوفة numpy ثلاثية الأبعاد (3D)
print("3D numpy array:\n", np_3d)
print("Shape of 3D array:", np_3d.shape)
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
print("7-")
for i in range(np_3d.shape[0]):
    for j in range(np_3d.shape[1]):
        for k in range(np_3d.shape[2]):
            print(f"[{i},{j},{k}] = {np_3d[i,j,k]} ",end = ' ')
print ()
input ("press any key to cont.........")
os.system ("cls")

print ("***********************************************")
####    ****************************************     ####
print ("*"*20, "index" , "*"*20)
print ("*"*20, "tuple " , "*"*20)
# الوصول إلى عنصر واحد بالاندكس
print("1-", mytuple[1])  # العنصر الثاني

# الوصول إلى آخر عنصر
print("2-", mytuple[-1])

# الوصول إلى مجموعة عناصر باستخدام Slicing
print("3-", mytuple[1:3])  # من العنصر الثاني للثالث (لا يشمل الثالث)

# الوصول إلى العناصر من البداية حتى اندكس معين
print("4-", mytuple[:2])  # أول عنصرين

# الوصول إلى العناصر من اندكس معين للنهاية
print("5-", mytuple[2:])  # من العنصر الثالث حتى الأخير

# الوصول إلى كل عنصرين (تخطي عنصر)
print("6-", mytuple[::2])

# الوصول إلى العناصر بالعكس
print("7-", mytuple[::-1])

# الوصول إلى عنصر باستخدام متغير اندكس
index = 0
print("8-", mytuple[index])

# الوصول إلى عنصر باستخدام حلقة for
print("9-")
for item in mytuple:
    print(item, end=' ')
print()

# الوصول إلى مجموعة عناصر باستخدام tuple comprehension (عن طريق تحويل إلى قائمة مؤقتاً)
subset = tuple(x for x in mytuple if "a" in x)
print("10-", subset)

input ("press any key to cont ........")
os.system("cls")













print ("***********************************************")
####    ****************************************     ####
print ("*"*20, "index" , "*"*20)
print ("*"*20, "dict " , "*"*20)

print ("this is the main dict : ", mydict)

# الوصول إلى عنصر باستخدام المفتاح مباشرة
print("1-" , mydict["age"])

# الوصول إلى عنصر باستخدام get (لا يعطي خطأ إذا لم يوجد المفتاح)
print("2-", mydict.get("city"))
print("3-", mydict.get("salary"," NOT FOUND "))
# الوصول إلى جيمع المفاتيح 
print("4-", list(mydict.keys())) # هنا أصبحت list 

# الوصول إلى جميع القيم

print("5-", list(mydict.values())) # هنا أصبحت list 


# الوصول إلى list(mydict.items()))

# الوصول إلى عنصر باستخدام متغير مفتاح
key = "name"
print("6-", mydict[key])

# الوصول إلى عنصر باستخدام حلقة for على المفاتيح
print("7-")
for k in mydict:
    print(f"{k}: {mydict[k]}")

# الوصول إلى عنصر باستخدام حلقة for على items
print("8-")

for k, v in mydict.items():
    print(f"{k} => {v}")

# الوصول إلى مجموعة عناصر تحقق شرط معين (dictionary comprehension)
print("9-")
subset = {k: v for k, v in mydict.items() if isinstance(v, str)}
print(subset)

# الوصول إلى أول عنصر (من Python 3.7+ القواميس مرتبة)
print("10-")
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


input ("press any key to cont ........")
os.system("cls")

print ("***********************************************")
####    ****************************************     ####
print ("*"*20, "index" , "*"*20)
print ("*"*20, "set " , "*"*20)
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
print ("*"*20, "list " , "*"*20)
exit

# list  
# Adds a single item to the end of the list
listcolor.append("silver")
print("After append:", listcolor)

# Inserts an item at a specific index
listcolor.insert(2, "gold")
print("After insert at index 2:", listcolor)

# Extends the list by appending elements from another iterable
listcolor.extend(["maroon", "olive"])
print("After extend:", listcolor)

# Concatenates another list using +
listcolor = listcolor + ["navy"]
print("useing + way to add item :", listcolor)

# Adds multiple items using += operator
listcolor += ["teal", "lime"]
print("useing + way to add list items :", listcolor)

# Inserts multiple items at a specific position using slice assignment
listcolor[1:1] = ["aqua", "fuchsia"]
print("to add list to list ' as extend ' in Specific location :", listcolor)

# Unpacks another list into the current list at a specific position
listcolor[3:3] = [*["indigo", "violet"]]

#array
print ("*"*20, "array " , "*"*20)

# Using append() to add a single element at the end
s_array.append(10)
print("After append:", s_array)

# Using extend() to add multiple elements (must be iterable)
s_array.extend([11, 12])
print("After extend:", s_array)

# Using fromlist() to add elements from a list
s_array.fromlist([13, 14])
print("After fromlist:", s_array)

# Using insert() to add an element at a specific position
s_array.insert(0, 0)
print("After insert at index 0:", s_array)

#np array 
print ("*"*20, "numpy array " , "*"*20)

# 1. Using append() from numpy (returns a new array)
np_array = np.append(np_array, 6)
print("After np.append (single item):", np_array)

# 2. Using append() to add multiple elements (returns a new array)
np_array = np.append(np_array, [7, 8])
print("After np.append (multiple items):", np_array)

# 3. Using concatenate() to join arrays
np_array = np.concatenate((np_array, np.array([9, 10])))
print("After np.concatenate:", np_array)

# 4. Using insert() to add an element at a specific index (returns a new array)
np_array = np.insert(np_array, 0, 0)
print("After np.insert at index 0:", np_array)

# 5. Using hstack() to add elements horizontally (returns a new array)
np_array = np.hstack((np_array, [11, 12]))
print("After np.hstack:", np_array)

# 6. Using vstack() to stack as new rows (creates 2D array)
# يجب التأكد أن طول المصفوفتين متساوي
row_to_stack = np.array([13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
# ضبط طول np_array ليطابق طول row_to_stack
if np_array.shape[0] != row_to_stack.shape[0]:
    np_array = np.resize(np_array, row_to_stack.shape[0])
np_array_2d = np.vstack((np_array, row_to_stack))
print("After np.vstack (2D array):\n", np_array_2d)

# 7. Using resize() to increase size and assign new values
np_array = np.resize(np_array, np_array.size + 2)
np_array[-2:] = [25, 26]
print("After np.resize and assign:", np_array)
# tuple
print ("*"*20, "tuple " , "*"*20)

# Tuples are immutable, so you cannot add elements directly.
# But you can create a new tuple by concatenation:

# 1. Using + operator to add a single element (as a tuple)
mytuple = mytuple + ("orange",)
print("After adding one item:", mytuple)

# 2. Using + operator to add multiple elements (as a tuple)
mytuple = mytuple + ("grape", "melon")
print("After adding multiple items:", mytuple)

# 3. Using unpacking to add elements at a specific position
mytuple = mytuple[:1] + ("kiwi",) + mytuple[1:]
print("After inserting at index 1:", mytuple)

# 4. Converting to list, adding, then converting back to tuple
temp = list(mytuple)
temp.append("pear")
mytuple = tuple(temp)
print("After append using list conversion:", mytuple)

# 5. Using tuple unpacking to merge tuples
mytuple = (*mytuple, "plum")
print("After unpacking and adding one item:", mytuple)

# 6. Using sum() to concatenate tuples (not common, but possible)
mytuple = sum([(mytuple), ("mango",)], ())
print("After using sum to add one item:", mytuple)

#dict 
print ("*"*20, "dict " , "*"*20)

# 1. Using assignment to add a new key-value pair
mydict["country"] = "USA"
print("After assignment:", mydict)

# 2. Using update() to add one or more key-value pairs
mydict.update({"email": "john@example.com"})
print("After update with one item:", mydict)

# 3. Using update() with multiple items
mydict.update({"phone": "123456", "gender": "male"})
print("After update with multiple items:", mydict)

# 4. Using setdefault() to add a key with a default value if it doesn't exist
mydict.setdefault("nickname", "Johnny")
print("After setdefault (new key):", mydict)

# 5. Using dictionary unpacking (Python 3.5+)
mydict = {**mydict, "hobby": "reading"}
print("After unpacking:", mydict)

# 6. Using the | operator (Python 3.9+)
mydict = mydict | {"status": "active"}
print("After using | operator:", mydict)

# sit 
print ("*"*20, "set " , "*"*20)

# 1. Using add() to add a single element
myset.add("orange")
print("After add:", myset)

# 2. Using update() to add multiple elements from an iterable (list, tuple, set)
myset.update(["grape", "melon"])
print("After update with list:", myset)

myset.update(("kiwi", "pear"))
print("After update with tuple:", myset)

myset.update({"plum", "mango"})
print("After update with another set:", myset)

# 3. Using |= operator to add elements from another set
myset |= {"papaya", "peach"}
print("After |= operator:", myset)

# 4. Using union() to create a new set with added elements (does not modify original)
newset = myset.union(["cherry", "banana"])
print("After union (original set unchanged):", myset)
print("New set after union:", newset)

# 5. Using unpacking to merge sets (Python 3.5+)
myset = { *myset, "apricot", "fig" }
print("After unpacking:", myset)

