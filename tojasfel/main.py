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
print("Feladat 0338")
print("Ellipszoid felszín számítás")
print("-------------------------------------------")

a=int(input("Első tengely: "))
b=int(input("Második tengely: "))
c=int(input("Harmadik tengely: "))
import math
felszin=math.pow(((math.pow((a*b), 1.6)+math.pow((a*c), 1.6)+math.pow((b*c), 1.6))/3), 0.625)*4*math.pi
print("Az ellipszoid felszíne: %.2f"%felszin)
