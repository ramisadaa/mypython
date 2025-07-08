import os
os.system('cls')

temp = int (input ("enter the temputer : "))
if temp < 0:
    print ("freezing weather")
elif temp < 10:
    print ("very cold weather")
elif temp < 20: 
    print ("cold weather")
elif temp < 30:
    print ("normal in temp")
elif temp < 40:
    print ("its hot")
elif temp <= 50:
    print ("its very hot")
else :
    print (" you are in hell")