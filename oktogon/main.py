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
print("Feladat 0346")
print("Oktogon terület számítás")
print("-------------------------------------------")

a=int(input("Oktogon oldalhossza: "))
import math
terulet=2*(1+math.sqrt(2))*math.pow(a, 2)
print("Oktogon területe: %.2f"%terulet)
