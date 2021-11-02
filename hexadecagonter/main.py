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
print("Feladat 0317")
print("Hexadecagon terület számítás")
print("-------------------------------------------")

a=int(input("Oldalhossz: "))
import math
terulet=4*(math.pow(a, 2))*(1/(math.tan(math.pi/16)))
print("Hexadecagon területe: %.2f"%terulet)
