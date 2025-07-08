def print_list (*args):
    for elem in args:
        elem *=2
        print (elem , end= "    ")

def print_address( ** kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



print_address(street="123 Fake St.",
    apt="100",
    city="Detroit",
    state="MI",
    zip="54321")

mydict1 = {"name": "rami", 
        "age" : 25 , 
        "avg" : 1.5
        }
print (mydict1)
print (type(mydict1))
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_list(mylist)
print_address()


