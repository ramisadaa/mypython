import os ; os.system("cls")

print ("*******************************************************")
print ("***************     B     M     I       ***************")

weaight = float ( input (" enter your weight in kg : "))
height = float ( input (" enter your height in cm : "))
bmi = (weaight / ((height * height)/10000)) 

if bmi < 18.5:
    print (f"your bmi is {bmi:.2f} and you are underweight")        
elif bmi >= 18.5 and bmi <= 24.9:
    print (f"your bmi is {bmi:.2f} and you are normal weight")          
elif bmi >= 25 and bmi <= 29.9:
    print (f"your bmi is {bmi:.2f} and you are overweight")         
elif bmi >= 30:
    print (f"your bmi is {bmi:.2f} and you are obese")
elif bmi >40:
    print (f"your weight is undefined ")            
else:
    print ("your bmi is invalid")

print ("done ")
# that program use to calculate the body mass index (BMI)

