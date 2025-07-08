import os 
import math
import time

os.system ('cls')

to_d =  (6 , 7 , 2025)
print (" And today is   " , to_d)

print (f"{'*'*20} WELLCOME  {'*' *20} ")
s = input ("Enter your bairth day : ")
s = s.split ('/')
# t = input ("Enter your date today  : ")
# t = to_day.split ('/')
# print (to_day)


# print (type (to_d))


dd_b = int (s[0])
mm_b = int (s[1])
yy_b = int (s[2])
dd_t = int (to_d[0])
mm_t = int (to_d[1])
yy_t = int (to_d[2])
dd_n = 0
mm_n = 0
yy_n = 0

print (f"{dd_t}   {mm_t}    {yy_t}")
print (f"{dd_b}   {mm_b}    {yy_b}")
print ("----------------------------")
if (yy_b> yy_t):
    print ("wrong date ")
elif (yy_b == yy_t) & (mm_b > mm_t):
    print ("wrong date ")
elif ( mm_b == mm_t) & (dd_b > dd_t):
    print ("wrong date ")
else :
    print ("********* WELLCOME  ******* ")
    if (dd_t>= dd_b) :
        dd_n = dd_t - dd_b
    else :
        dd_n =  (dd_t+30 ) - dd_b
        mm_t-=1 
    if (mm_t>= mm_b) :
        mm_n = mm_t - mm_b
    else :
        mm_n = (mm_t+12) -mm_b
        yy_t -=1
    
    yy_n = yy_t - yy_b 
    # print (f"{dd_n}   {mm_n}   {yy_n}")
    print (f"your age is {yy_n} years , {mm_n} month and {dd_n} days ")
