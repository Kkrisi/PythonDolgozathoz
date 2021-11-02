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
print("Feladat 0318")
print("Kör alapú henger felszín számítása")
print("-------------------------------------------")

sugar=int(input("Sugár hossza: "))
hossz=int(input("Hossza:"))
import math
felszin=2*math.pi*(math.pow(sugar, 2))+2*math.pi*sugar*hossz
print("Kör alapú henger felszíne: ",felszin)
