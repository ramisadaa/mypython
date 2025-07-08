# ========================= Object Attributes =========================
import datetime
import os

os.system("cls")

class All_Data():
        
    def __init__(self):
        self.id = (str(datetime.datetime.now()).replace("-","").replace(" ","").replace("/","").replace(":","").replace(".",""))
        x= self.id

    
class User(All_Data):
    
    def __init__(self, fn, ln, email, phone):
        self.first_name = fn
        self.last_name = ln
        self.email = email
        self.phone = phone
        print(x)
# class Std():
#     print ("that is student : ")

# class Stf():
#     print ("that is teatcher : ")


user_1 = User("Yehya", "Ali", "ya@yahoo.com", "123456789")

user_2 = User("Ahmad", "Omar", "ao@yahoo.com", "987654321")


print(user_1.first_name, user_1.last_name, user_1.email, user_1.phone )

print( user_2.first_name, user_2.last_name, user_2.email, user_2.phone )

