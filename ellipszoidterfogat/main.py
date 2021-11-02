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
print("Feladat 0337")
print("Ellipszoid térfogat számítás")
print("-------------------------------------------")

a=int(input("Első tengely: "))
b=int(input("Második tengely: "))
c=int(input("Harmadik tengely: "))
import math
terfogat=(4/3)*math.pi*a*b*c
print("Az ellipszoid térfogata: %.2f"%terfogat)
