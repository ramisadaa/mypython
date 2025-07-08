import os

def clear_terminal():
    # لمسح الشاشة في أنظمة Windows
    if os.name == 'nt':
        os.system('cls')
    # لمسح الشاشة في أنظمة Unix/Linux/Mac
    else:
        os.system('clear')

# مثال على الاستخدام:
clear_terminal()
print ("*********************************************************************")
NAME = input (" ENTER YOR NAME : \n\t ")
print (f"***********************   WELLCOME BACK MR. {NAME}   *************************\n")
from IPython.display import display
import math
from ipywidgets import interact, FloatSlider, IntSlider, Output

output = Output()

def interactive_math_demo(x=1.0, y=2.0, n=5):
    output.clear_output()
    with output:
        
        print("=== الثوابت ===")
        print(f"math.pi = {math.pi}")  # يطبع قيمة باي 
        print(f"math.e = {math.e}")     #يطبع قيمة e
        print(f"math.tau = {math.tau}") # يطبع قيمه e مضعفة 
        print(f"math.inf = {math.inf}")     # ما لا نهاية 
        print(f"math.isnan(math.nan) = {math.isnan(math.nan)}\n") # الغير معرف - غير رقمي 

        print("=== حسابات عامة ===")
        print(f"sqrt({x}) = {math.sqrt(x)}") # 
        print(f"pow({x}, {y}) = {math.pow(x, y)}")
        print(f"exp({x}) = {math.exp(x)}")
        print(f"log({x}) = {math.log(x)}")
        print(f"log10({x}) = {math.log10(x)}")
        print(f"log2({x}) = {math.log2(x)}\n")

        print("=== دوال مثلثية ===")
        print(f"cos({x}) = {math.cos(x)}")
        print(f"sin({x}) = {math.sin(x)}")
        print(f"tan({x}) = {math.tan(x)}")
        print(f"degrees({x}) = {math.degrees(x)}")
        print(f"radians({x}) = {math.radians(x)}\n")

        print("=== دوال تقريب ===")
        print(f"ceil({x}) = {math.ceil(x)}")
        print(f"floor({x}) = {math.floor(x)}")
        print(f"trunc({x}) = {math.trunc(x)}")
        print(f"fabs({x}) = {math.fabs(x)}\n")

        print("=== مقارنة وأرقام خاصة ===")
        print(f"isclose({x}, {y}) = {math.isclose(x, y)}")
        print(f"isfinite({x}) = {math.isfinite(x)}")
        print(f"isinf({x}) = {math.isinf(x)}\n")

        print("=== توافقيات ===")
        print(f"factorial({n}) = {math.factorial(n)}")
        print(f"comb({n}, 3) = {math.comb(n, 3)}")
        print(f"perm({n}, 3) = {math.perm(n, 3)}\n")

        print("=== أخرى ===")
        print(f"gamma({x}) = {math.gamma(x)}")
        print(f"lgamma({x}) = {math.lgamma(x)}")
        print(f"fsum([0.1]*10) = {math.fsum([0.1]*10)}")
        print(f"prod([1, 2, 3, 4]) = {math.prod([1, 2, 3, 4])}")
        print(f"modf({x}) = {math.modf(x)}")
        print(f"frexp({x}) = {math.frexp(x)}")
        print(f"ldexp({x}, 3) = {math.ldexp(x, 3)}")

interact(
    interactive_math_demo,
    x=FloatSlider(min=0.1, max=10.0, step=0.1, value=1.0, description='x'),
    y=FloatSlider(min=0.1, max=10.0, step=0.1, value=2.0, description='y'),
    n=IntSlider(min=1, max=10, step=1, value=5, description='n')
)

display(output)