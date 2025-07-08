import os
os.system("cls")

class Std:
    std_num = 0
    std_year = 2025
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Std.std_num +=1
    




std1 = Std("rami", 20)
std2 = Std("sami", 30)
std3= Std("mamy", 40)
std4 = Std("tami", 20)
std5 = Std("dami", 30)
std6 = Std("fami", 40)
std7 = Std("gami", 20)
std8 = Std("hami", 30)
std9 = Std("jami", 40)


print (std1.name, std1.age, Std.std_num)
print (std2.name, std2.age, std2.std_num)
print (std3.name, std3.age, std3.std_num)
print (std4.name, std4.age, std4.std_num)
print (std5.name, std5.age, std5.std_num)
print (std6.name, std6.age, std6.std_num)
print (std7.name, std7.age, std7.std_num)
print (std8.name, std8.age, std8.std_num)
print (std9.name, std9.age, std9.std_num)

print("Total number of students:", Std.std_num)

