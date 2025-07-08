import os 
import keyboard 
os.system ("cls")


x= list ()
print (x)

while True :
    temp = input ("enter your value : ")
    x.insert (len(x),temp)
    if keyboard.is_pressed ('esc'):
        break   

print (x)
