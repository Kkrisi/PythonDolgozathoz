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
print("Feladat 0327")
print("Ellipszis alapú kúp térfogat számítása")
print("-------------------------------------------")

magassag=int(input("Kúp magassága: "))
r1=int(input("Első sugara: "))
r2=int(input("Második sugara: "))
import math
terfogat=1/3*math.pi*r1*r2*magassag
print("Térfogat: %.2f"%terfogat)
