import numpy as np
import os 
os.system ('cls')
# 1. Initialize with zeros
x1 = np.zeros((2, 3))
print("Zeros (x1, np.zeros):\n", x1)

# 2. Initialize with ones
x2 = np.ones((2, 3))
print("Ones (x2, np.ones):\n", x2)

# 3. Initialize with a constant value
x3 = np.full((2, 3), 7)
print("Full (x3, np.full):\n", x3)

# 4. Initialize with random integers
x4 = np.random.randint(0, 10, (2, 3))
print("Random Integers (x4):\n", x4)

# 5. Initialize with random floats
x5 = np.random.rand(2, 3)
print("Random Floats (x5):\n", x5)

# 6. Initialize with arange
x6 = np.arange(6).reshape(2, 3)
print("Arange (x6):\n", x6)

# 7. Initialize with linspace
x7 = np.linspace(0, 1, 6).reshape(2, 3)
print("Linspace (x7):\n", x7)

# 8. Initialize as identity matrix
x8 = np.eye(3)
print("Identity (x8):\n", x8)

# 9. Initialize from a Python list
x9 = np.array([[1, 2, 3], [4, 5, 6]])
print("From List (x9):\n", x9)

x = np.zeros((2, 3), dtype=float)
print("Zeros (x):\n", x)

x = np.full((4, 4), False)
x.ravel()[:8] = True
print("Boolean Array (x):\n", x)

# 1. Initialize 3D array with zeros
x3d_zeros = np.zeros((2, 3, 4))
print("3D Zeros (x3d_zeros):\n", x3d_zeros)

# 2. Initialize 3D array with ones
x3d_ones = np.ones((2, 3, 4))
print("3D Ones (x3d_ones):\n", x3d_ones)

# 3. Initialize 3D array with a constant value
x3d_full = np.full((2, 3, 4), 7)
print("3D Full (x3d_full):\n", x3d_full)

# 4. Initialize 3D array with random integers
x3d_randint = np.random.randint(0, 10, (2, 3, 4))
print("3D Random Integers (x3d_randint):\n", x3d_randint)

# 5. Initialize 3D array with random floats
x3d_rand = np.random.rand(2, 3, 4)
print("3D Random Floats (x3d_rand):\n", x3d_rand)

# 6. Initialize 3D array with arange
x3d_arange = np.arange(24).reshape(2, 3, 4)
print("3D Arange (x3d_arange):\n", x3d_arange)

# 7. Initialize 3D array with linspace
x3d_linspace = np.linspace(0, 1, 24).reshape(2, 3, 4)
print("3D Linspace (x3d_linspace):\n", x3d_linspace)

# 8. Initialize 3D identity-like array (not standard, but using eye in 3D)
x3d_eye = np.eye(4)[None, :, :]
print("3D Identity-like (x3d_eye):\n", x3d_eye)

# 9. Initialize 3D array from a Python list
x3d_list = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
])
print("3D From List (x3d_list):\n", x3d_list)

#    ********************************************    #
# indexing 

input ("press any key to cont........")
os.system ('cls')
print ("<<<<<        x6[0]       >>>>\n", x6)
print ("<<<<<      x6[1][2]      >>>>\t\t ", x6[1][ 1: :2])

print("3D From List (x3d_list):\n", x3d_list)
print("3D From List (x3d_list.shape):\n", x3d_list.shape) # الابعاد 
print("3D From List (x3d_list.size):\n", x3d_list.size) # عدد العناصر 
print("3D From List (x3d_list.shape):\n", x3d_list[0][0][0])
print("3D From List (x3d_list.shape):\n", x3d_list[1][1][1])


# Initialize a 3x3x3 numpy array with Arab city names

input ("enter any key........")
os.system("cls")

arab_cities = np.array([
    [
        ["Cairo", "Riyadh", "Dubai"],
        ["Beirut", "Amman", "Baghdad"],
        ["Damascus", "Tunis", "Algiers"]
    ],
    [
        ["Khartoum", "Doha", "Muscat"],
        ["Tripoli", "Rabat", "Kuwait City"],
        ["Manama", "Jeddah", "Sharjah"]
    ],
    [
        ["Alexandria", "Marrakesh", "Sanaa"],
        ["Gaza", "Homs", "Basra"],
        ["Mosul", "Fez", "Salalah"]
    ]
])
print("3x3x3 Arab Cities Array:\n", arab_cities)
print("Shape:", arab_cities.shape)

print ( arab_cities.size)
print ( arab_cities[0][0][0])
print ( arab_cities[1][1][1])
print ( arab_cities[2][2][2])

m = arab_cities[2][2][1]
print (m)


# Iterate over all elements in arab_cities and print them
# شرح الكود وبالأخص np.nditer
# np.nditer هي دالة في مكتبة numpy تتيح لك المرور (iteration) على جميع عناصر المصفوفة بغض النظر عن أبعادها.
# في هذا المثال، arab_cities عبارة عن مصفوفة ثلاثية الأبعاد (3x3x3) تحتوي على أسماء مدن عربية.
# عند استخدام np.nditer(arab_cities)، سيتم المرور على كل عنصر (اسم مدينة) واحدًا تلو الآخر بشكل تسلسلي.
# في كل دورة من الحلقة، elem يمثل عنصرًا واحدًا (اسم مدينة) من المصفوفة.
# الطباعة ستظهر كل اسم مدينة في سطر منفصل.

# for elem in np.nditer(arab_cities):
#     print(elem)


a = np.array([[1, 2], [3, 4], [5,6]])

for x in np.nditer(a):
    print(x, end="_"*10)
print ()

arr = np.random.choice(np.arange( 10), size=(2, 3, 4), replace=False)
print(arr.size) 
print(arr)