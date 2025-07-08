from array import array
import numpy as np  
import os


listcolor = ["red", "green", "blue", "yellow", "black", "white"]
listinlist  = [ 0 ,  ['a' , 'b' , 'c'] , [1 , 2, 3 , 4 ] ,  [True , False ] , 'm'] 

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

print("00- type(variable):", type(listinlist[1]))
if isinstance(listinlist[1], tuple):
    print("01- variable is a tuple")
else : 
    print ("01- variable is not a tuple")

# 1. استخدام isinstance للفحص مع شرط
print("1- isinstance(listcolor, list):", isinstance(listcolor, list))
print("2- isinstance(s_array, array):", isinstance(s_array, array))
print("3- isinstance(np_array, np.ndarray):", isinstance(np_array, np.ndarray))
print("4- isinstance(mytuple, tuple):", isinstance(mytuple, tuple))
print("5- isinstance(mydict, dict):", isinstance(mydict, dict))
print("6- isinstance(myset, set):", isinstance(myset, set))
