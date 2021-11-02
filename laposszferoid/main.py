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
print("Feladat 0340")
print("Lencseszferoid térfogat számítás")
print("-------------------------------------------")

a=int(input("Első tengely: "))
b=int(input("Második tengely: "))
import math
terfogat=((4*math.pi)/3)*a*math.pow(b, 2)
print("Az orsószferoid térfogata: %.2f"%terfogat)
