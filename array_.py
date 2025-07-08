from array import array
import os

os.system ('cls')

s= array ('i',[1,2,3,4,5,6,7,8,9])

print (s)
print (type(s))
print (s[0])
## oparation

s.append (10)
print (s)

s.insert (100, 11)
print (s[10])
print (s)

s.extend([100 , 200, 300 , 400])
print (s)


s.clear ()
print (s)
s.append (90)
s.append (90)
s.append (90)

print (s)

s.extend([10,20,30,40,50,60,70,80,90])
print (s)

s.pop(0)
print (s)

s.remove(10)
print (s)

del s[3:5]
print (s)

print (max (s))
print (min (s))
print (sorted(s))

print ( sorted(s , reverse= True))
print (s.count (90))

print (s.index (60)) # ترجع الموقع للعنصر المختار 
