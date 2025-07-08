
import os; os.system('cls' if os.name == 'nt' else 'clear')
# لمسح الشاشة في أنظمة Windows


x = input ("enter any char or number or name : ")
y = input ("enterany char or number or name :  ")

if x==y:
    print (f"{x} = {y} is true statmant ")
else:
    print (f"{x} = {y} is false statmant ")

if x!=y:
        print (f"{x} != {y} is true statmant ")
else:
    print (f"{x} != {y} is false statmant ")

if x<y:
     print ("f{x} < {y} is true statmant ")
else:
    print (f"{x} < {y} is false statmant ")

if x<=y:
     print (f"{x} <= {y} is true statmant ")
else:
    print (f"{x} <= {y} is false statmant ")

if x>y:
     print (f"{x} > {y} is true statmant ")
else:
    print (f"{x} > {y} is false statmant ")

if x>=y:
     print (f"{x} >= {y} is true statmant ")
else:
    print (f"{x} >= {y} is false statmant ")

game1 = True
game2 = False

print (f"   *******       {game1}        {game2}         *******")
if game1 and game2:
     print ("all True ")
if game1 or game2:
     print ("one or all is true ")

n = 0 
x = "m"
while x !="s":
    n+=1
    print (n)
    x = input ("Enter your choice : ")
    