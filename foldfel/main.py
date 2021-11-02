# coding=utf-8
# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0341")
print("Orsószferoid felszín számítás")
print("-------------------------------------------")

a=int(input("Első tengely: "))
b=int(input("Második tengely: "))
import math

if (a <= b):
    print("A második számnak túl kicsit számot adtál meg, nem létezik ilyen geometriai alakzat.        Kezd elölről!")
    
while a <= b:
    a=int(input("Első tengely: "))
    b=int(input("Második tengely: "))
    if (a>b):
        break

felszin=2*math.pi*b*(b+(math.pow(a,2)/(math.sqrt(math.pow(a,2)-math.pow(b,2)))))*math.asin(math.sqrt(math.pow(a, 2)-(math.pow(b, 2)))/a)
print("Az orsószferoid felszine: %.2f"%felszin)
