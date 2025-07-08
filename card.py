import os
os.system("cls")

class Card():
    u_count = 0
    
    @classmethod
    def showuser(cls):
        return f"you have {cls.u_count} in the system "
    
    @staticmethod 
    def gree():
        print("-"*50)
        print("-"*50)
        print ("wellcome to our program ")
    
    def __init__(self, fn , ln, mn ,t , j , w, h_email , w_email ):
        self.fname = fn
        self.lname = ln
        self.mname = mn
        self.tel = t 
        self.jawwal = j
        self.wataneya = w 
        self.home_email = h_email
        self.work_email = w_email
        Card.u_count +=1
    
    def empty (self):
        return f"{self.fname} is emputy acount "
    def full (self):
        return f"{self.fname} is full acount  "

user1 = Card( "rami" , "sadaa", "F." , "2060780" , "0599626669" , "056752059710", "rami.sadaa@gmail.com" , "r.sadaa@unrwa.org" )
user2 = Card( "sami" , "sadaa", "j.." ,"2066114" , "0599625895" , "065784215404", "s.Jaasa@gmail.com" , "s.Jaasa@unrwa.org" )
user2 = Card( "rema" , "sadaa", "R.." ,"00000" , "059999999" , "05688888", "rema.rami@gmail.com" , "s.Jaasa@unrwa.org" )

Card.gree()


full_name1 =  user1.fname +" "+ user1.mname +" "+ user1.lname
full_name2 =  user2.fname +" "+ user2.mname +" "+ user2.lname

os.system("cls")
print (full_name1 , " 🔐" , user1.empty())
print (full_name2 , " 🔓" , user2.full())

print (Card.u_count)

print (Card.showuser())