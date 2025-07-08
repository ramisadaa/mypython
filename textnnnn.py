# -*- coding: utf-8 -*-

import os
import time 
os.system('cls')
print ("************************************************************\n\n")
import random
import math
while True :
    os.system('cls')
    x = int(input ("enter the number [1 ... 52 ]"))
    x-=1
    
    print("****************     Random calcalator      ****************\n\n")
    print("\t\t\t\t     ", x, "\n\n")

    if x == 0:
        print("Function is :  acos(n) ----> [take n ( -1 : 1 )]")
        print ("\t Returns the arc cosine of a number")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.acos(n))

    elif x == 1:
        print("function is :  acosh(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.acosh(n))

    elif x == 2:
        print("function is :  asin(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.asin(n))

    elif x == 3:
        print("function is :  asinh(n)----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.asinh(n))

    elif x == 4:
        print("function is :  atan(n)----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.atan(n))

    elif x == 5:
        print("function is :  atan2(y, x)----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        y = float(input("Enter the 1st number :   "))

        x = float(input("Enter the 2nd number :   "))

        print("The result :", math.atan2(y, x))

    elif x == 6:
        print("function is :  atanh(n)----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.atanh(n))

    elif x == 7:
        print("function is :  ceil(n)----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.ceil(n))

    elif x == 8:
        print("function is :  comb(n, k)----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = int(input("Enter the number :   "))

        k = int ("Enter the number :   ")
        print("The result :", math.comb(n, k))

    elif x == 9:
        print("function is :  copysign(x, y) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        x =float(input("Enter the number :   "))

        y =float(input("Enter the number :   "))

        print("The result :", math.copysign(x, y))

    elif x == 10:
        print("function is :  cos(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.cos(n))

    elif x == 11:
        print("function is :  cosh(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.cosh(n))

    elif x == 12:
        print("function is :  degrees(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.degrees(n))

    elif x == 13:
        print("function is :  dist(p, q) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        p = [float(input("Enter the p1 number :   ")), float(input("Enter the p2 number :   "))]
        q = [float(input("Enter the q1 number :   ")), float(input("Enter the q2 number :   "))]
        print("The result :", math.dist(p, q))

    elif x == 14:
        print("function is :  erf(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.erf(n))

    elif x == 15:
        print("function is :  erfc(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.erfc(n))

    elif x == 16:
        print("function is :  exp(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.exp(n))

    elif x == 17:
        print("function is :  expm1(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.expm1(n))

    elif x == 18:
        print("function is :  fabs(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.fabs(n))

    elif x == 19:
        print("function is :  factorial(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = int(input("Enter the number :   "))
        print("The result :", math.factorial(n))

    elif x == 20:
        print("function is :  floor(n)----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.floor(n))

    elif x == 21:
        print("function is :  fmod(x, y) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        x = float(input("Enter the 1st number :   "))
        y = float(input("Enter the 2nd number :   "))
        print("The result :", math.fmod(x, y))

    elif x == 22:
        print("function is :  frexp(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.frexp(n))

    elif x == 23:
        print("function is :  fsum(iterable) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        iterable = list(map(float, input("Enter the number :   ").split()))
        print("The result :", math.fsum(iterable))

    elif x == 24:
        print("function is :  gamma(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.gamma(n))

    elif x == 25:
        print("function is :  gcd(a, b) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        a = int(input("Enter the 1st number :   "))
        b = int(input("Enter the 2nd number :   "))
        print("The result :", math.gcd(a, b))

    elif x == 26:
        print("function is :  hypot(x, y) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        x = float(input("Enter the 1st number :   "))
        y = float(input("Enter the 2nd number :   "))
        print("The result :", math.hypot(x, y))

    elif x == 27:
        print("function is :  isclose(a, b) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        a = float(input("Enter the 1st number :   "))
        b = float(input("Enter the 2nd number :   "))
        print("The result :", math.isclose(a, b))

    elif x == 28:
        print("function is :  isfinite(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.isfinite(n))

    elif x == 29:
        print("function is :  isinf(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.isinf(n))

    elif x == 30:
        print("function is :  isnan(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.isnan(n))

    elif x == 31:
        print("function is :  isqrt(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = int(input("Enter the number :   "))
        print("The result :", math.isqrt(n))

    elif x == 32:
        print("function is :  ldexp(x, i) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        x = float(input("Enter the number :   "))

        i = int(input("Enter the number :   "))
        print("The result :", math.ldexp(x, i))

    elif x == 33:
        print("function is :  lgamma(n) ----> [take n ( >=1 )]")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.lgamma(n))

    elif x == 34:
        print("function is :  log(n, base) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        base = float(input("Enter the base number :   "))
        print("The result :", math.log(n, base))

    elif x == 35:
        print("function is :  log10(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.log10(n))

    elif x == 36:
        print("function is :  log1p(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.log1p(n))

    elif x == 37:
        print("function is :  log2(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.log2(n))

    elif x == 38:
        print("function is :  modf(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.modf(n))

    elif x == 39:
        print("function is :  nextafter(x, y) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        x = float(input("Enter the 1st number :   "))
        y = float(input("Enter the 2nd number :   "))
        print("The result :", math.nextafter(x, y))

    elif x == 40:
        print("function is :  perm(n, k) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = int(input("Enter the 1st number :   "))
        k = int(input("Enter the 2nd number :   "))
        print("The result :", math.perm(n, k))

    elif x == 41:
        print("function is :  pow(x, y) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        x =float(input("Enter the number :   "))

        y =float(input("Enter the number :   "))

        print("The result :", math.pow(x, y))

    elif x == 42:
        print("function is :  prod(iterable) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        iterable = list(map(float, input("Enter the number with space :   ").split()))
        print("The result :", math.prod(iterable))

    elif x == 43:
        print("function is :  radians(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.radians(n))

    elif x == 44:
        print("function is :  remainder(x, y =) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        x = float(input("Enter the 1st number :   "))
        y = float(input("Enter the 2nd number :   "))
        print("The result :", math.remainder(x, y))

    elif x == 45:
        print("function is :  sin(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.sin(n))

    elif x == 46:
        print("function is :  sinh(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.sinh(n))

    elif x == 47:
        print("function is :  sqrt(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.sqrt(n))

    elif x == 48:
        print("function is :  tan(n) ----> [take n ( >=1 )") 
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.tan(n))

    elif x == 49:
        print("function is :  tanh(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.tanh(n))

    elif x == 50:
        print("function is :  trunc(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.trunc(n))

    elif x == 51:
        print("function is :  ulp(n) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = float(input("Enter the number :   "))
        print("The result :", math.ulp(n))

    elif x == 52:
        print("function is :  comb(n, k) ----> [take n ( >=1 )")
        print ("\t ")
        print ("*******************************************\n\n")
        n = int(input("Enter the 1st number :   "))
        k = int(input("Enter the 2nd number :   "))
        print("The result :", math.comb(n, k))

    x= input ("\n\n Do you want to calc agine :  [ Y , N ] ")
    if x == 'y':
        print ("wellcom balck")
    elif x == 'n':
        print ('bye bye ')
        break
    else :
        print ('wrong char ')
        time.sleep(2)

