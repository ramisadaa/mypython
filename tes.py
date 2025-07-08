import random as R
import os
os.system("cls")


a = R.randint(5,10)
b = R.randrange(10,20)
c = R.random ()
tempset = set()
tempset.add (a)
tempset.update((b, c))
b = R.randrange(10,20)
c = R.random ()
tempset.update([b, c])


print (a, "   " , b , "   " , c , "   ")
print ("tempset : ", tempset)

a = R.randint(10,100)
b = R.randrange(20,100)
c = R.random ()

newset = set()
newset.add (a)
newset.add (b)
newset.add (c)

print (a, "   " , b , "   " , c , "   ")

tempset |= newset
print ("tempset : ", tempset)
print ("R.choice(tempset)",R.choice(list(tempset)))


mylist = [1 , 2 , 5 , "s" , True , "raa" , ]
a1 =[]
print (mylist)
s_set = {1}
print (s_set)

s_set.add(4)
print (s_set)

m = R.randint (1, 10)
s_set.add(m)
print (s_set)

s = R.randrange(1,100)
e = R.randrange(1,100)
s_set.update([s, e])
print (s_set)
# a0 = R.choice(mylist)

print ("a1befor : ", a1)
a1.extend (a1)
print("a1 = ", a1)

#print (help(R))
# print (a0)
# print (a1)
# print (R.randint(1, 100))
# print (R.random())
# print (R.randrange(1, 10, 5))
# print (R.sample([1, 2, 3, 4, 5], 4))
# R.seed(1)
# print("seed(42): Random generator initialized.")

# x= [1, 2 , "a" , "b" , True , False , 10.0 , "rami"]
# print (x)
# R.shuffle(x)
# print (x)

# print(R.uniform(2, 3))