#coding=utf-8
# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0301")
print("Kör alapú kúp térfogat számítás")

sugar=int(input("Alap sugár hossza: "))
magassag=int(input("Kúp magassága: "))
import math
terfogat=(1/3)*math.pow(sugar, 2)*math.pi*magassag
print("A kúp térfogata: %.2f" %terfogat)
