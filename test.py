import os 
class Car():
    counter = 0
    @staticmethod
    def clear():
        return os.system("cls")
    
    @staticmethod
    def intro():
        print ("-"*50)

    @classmethod
    def total(cls):
        return f"you have asses {Car.counter} in the system"
        

    def __init__(self, name , model , color , sale):
        self.car_name = name
        self.car_model = model
        self.car_color = color
        self.car_forsale = sale
        Car.counter +=1
    
    def hi(self):
        print ("hello my frind")
    
    def drive(self):
        return "is driving "
    
    def stop(self):
        return "is stoping"

car1 = Car('suparo', 2000 , 'wite', True)
car2 = Car('volvo', 2010 , 'black', False)
car3 = Car('nesain', 2020 , 'red', True)
 


Car.clear()
Car.intro()

car1.hi()
# print (car1.car_name)
print ("***********")
print (car1.car_name , " >>>> ", car1.drive())
print ("***********")

print ( )
# car2.hi()
# print(car2.car_name , "is for sale : ", car2.car_forsale)
print ("***********")
print (car2.car_name, " <<<< ", car1.stop())
print ("***********")

car3.hi()
print(car3.car_name , car3.car_color ,car3.car_model)

print ("-"*50 )
print (Car.total())
print ("-"*50 )


# n = input ("Enter name  : ")
# m = input ("Enter the model : ")
# c = input ("Enter the color : ")
# s = input ("Enter for sale [y - n ]: ")

# car4 = Car(n, m , c, s)

# print ("------------------------------------------------" )
# car4.hi()
# print(car4.car_name , "is for sale : ", car4.car_forsale)
# print(car4.car_name , car4.car_color ,car4.car_model)