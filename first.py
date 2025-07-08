print ("wellcom back Mr rami ")
import os 

# def clear():
#     os.system ('cls')

# clear()
# print (type (clear))
# print ("now its clean ")


# # Example: Define a function that adds two numbers
# def add(a, b):
#     return a + b

# result = add(5, 3)
# print("The sum is:", result)

# # Example: Function with default argument
# def greet(name="Guest"):
#     print("Hello,", name)

# greet("Rami")
# greet()



# def mod_dict ():

#     name_ = input   ("Enter the name :") 
#     age_ = input ("enter the age : ")
#     skill_ = input ("enter the skill : ")
#     global dict_no
#     global dict_order
#     dict_order[dict_no] = {
#       "name_" : name_ , 
#       "age " : age_ ,
#       "skill_" : skill_ 

#                           }
#     dict_no += 1
# while True:
#     if (input("press [s] to stop  or [] the loop :" )) == 's':
#         for mk, mv in dict_order.items():
#             print (f"<<< =======   {mk}  ====== >>>>>")
#             for sk , sv in dict_order[mk].items():
#                 print (sk , "====== >> > " , sv )
#             print ("<<< ==================== >>>>>")
#         break
#     else :
#         mod_dict()

# print (dict_order)

# # x = input ("enter your choise : ")
# # if x.lower =='y':
# #     mod_dict()

# name = input ("Enter tha mane : ")
# def clr_name_m(name):
#     # """
#     # Removes consecutive duplicate characters from the input string and returns the cleaned string.
#     # """
#     # if not name:
#     #     return ""
#     result = [name[0]]
#     for char in name[1:]:
#         if char != result[-1]:
#             result.append(char)
#     return ''.join(result)

# print(clr_name_m(name))


# name = ['r', 'a' , 'm' , 'y']
# print("".join(name))


# def my_function(fname, lname= None):
#   print(fname + " " + lname)

# my_function("rami")

def my_function(*, x):
  print(x)

my_function(x = 3)


def my_function2(a, b, /, *, c, d):
  print(a + b + c + d)

my_function2(5, 6, c = 7, d = 8)

print("***********************************************")
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 30)  # المعامل "Alice" يذهب إلى المعامل "name"، والمعامل "30" إلى المعامل "age"

print("*********************222**************************")
def greet2(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet2(name="Bob", age=25)  # هنا، يُحدد اسم المعامل (name و age) وقيمته
greet2(age=25 , name="Bob")  # 



print("*********************33**************************")

def flexible_function(*args, **kwargs):
    print("not named ", args)
    print("named :", kwargs)
flexible_function(1, 2, 3, 5 , 7 , name="Charlie", age=20, sex = 'male')