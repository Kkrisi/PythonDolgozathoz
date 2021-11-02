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
print("Feladat 0344")
print("Köralapú henger térfogat számítás")
print("-------------------------------------------")

sugar=int(input("Henger sugara: "))
magassag=int(input("Henger magassága: "))
import math
terfogat=math.pi*math.pow(sugar, 2)*magassag
print("A henger térfogata: %.2f"%terfogat)
