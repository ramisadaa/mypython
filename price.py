import os
os.system("cls")

menu = {"pizza": 3.00,
"nachos": 4.50,
"popcorn": 6.00,
"fries": 2.50,
"chips": 1.00,
"pretzel": 3.50,
"soda": 3.00,
"lemonade": 4.25}
cart = []
total = 0

print ("Welcome to the snack bar!") 
print ("Here is the menu:" )
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")  
while True:
    s = input ("enter your food  [z, n - pp - f - c - p - s - l ] : ")
    
    if s == 'z' :
        cart.append(menu["pizza"])
    elif s == 'n' :
        cart.append(menu["nachos"])
    elif s == 'pp' :
        cart.append(menu["popcorn"])
    elif s == 'f' :
        cart.append(menu["fries"])
    elif s == 'c' :
        cart.append(menu["chips"])
    elif s == 'p' :
        cart.append(menu["pretzel"])
    elif s == 's' :
        cart.append(menu["soda"])
    elif s == 'l' :
        cart.append(menu["lemonade"])
    elif s == 'q':
        break
    else : 
        print ("invalid input, try again")
        continue        
print ("Your cart: ", cart)
for i in range(len(cart)) :
    total += cart[i]
print ( "total cost = ", total)

    