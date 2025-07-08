import os
os.system("cls")


class user:
    u_count = 0
    
    @staticmethod
    def wellcom():
        return f"hello and ya Welcome" 
    

    @classmethod
    def show(cls):
        return f"we have {cls.u_count} in the system "

    def __init__(self,fname,lname, email, tel):
       self.first_name = fname
       self.last_name = lname
       self.email = email
       self.tel =   tel
       user.u_count +=1

    def login(self):
        return f"{self.first_name} ,{self.last_name} User logged in  😁"
    def logout(self):
        return f"{self.first_name} ,{self.last_name} User logged out 😷"
    

user1 = user("rami"     , 'sadaa' , "rami.sadaa@gmail.com"      ,599626669)
print(user1.first_name , user1.last_name , user1.email , user1.last_name)
print (user1.login())


user2 = user("ahmad"    , 'sadaa' , "ahmad.sadaa@gmail.com "    ,599626668)
print(user2.first_name , user2.last_name , user2.email , user2.last_name)
print (user2.logout())

# user3 = user("mohammad" , 'sadaa' , "mohammed.sadaa@gmail.com " ,599626667)
# user4 = user("yousef"   , 'sadaa' , "yousef.sadaa@gmail.com "   ,599626666)
# user5 = user("mahammod" , 'sadaa' , "mahammod.sadaa@gmail.com " ,599626665)    
# user6 = user("mohaneed" , 'sadaa' , "mohaneed.sadaa@gmail.com"  ,599626664)


print (user.u_count)

print (user.show())

print(user.wellcom())



# for i in range(1,7):
#     nstr = "user" + str(i)
#     print (eval(nstr).first_name, eval(nstr).last_name, eval(nstr).email, eval(nstr).tel)
# print ()

