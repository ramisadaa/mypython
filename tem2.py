import os 
os.system("cls")

x = float( input ("enter the temperatute in celesius  :"))
y = (x * 9/5) + 32

if x<20:
    print (f"the temperature is {x} C & {y} F and it is cold")
elif x>=20 and x<=30:
    print (f"the temperature is {x} C & {y} F and it is warm")
elif x>30:
    print (f"the temperature is {x} C & {y} F and it is hot")
else:
    print ("the temperature is invalid")
print ("done ")
# that program use to convert the temperature from celsius to faherenheit
#and also check the temperature if it is hot or cold or warm 
