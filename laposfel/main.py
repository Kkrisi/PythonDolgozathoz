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
print("Feladat 0342")
print("Lencseszferoid felszín számítás")
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
    
iksz=(math.sqrt(math.pow(a, 2)-(math.pow(b, 2)))/a)    
e = 2.718281
kicsi=math.log(e, (iksz+math.sqrt(math.pow(iksz,2)+1)))      

nagyfele=a+(math.pow(a,2)/(math.sqrt(math.pow(a,2)-math.pow(b,2))))

felszin=2*math.pi*a*(nagyfele)*kicsi
print("Az orsószferoid felszine: %.2f"%felszin)
