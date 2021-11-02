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
print("Feladat 0348")
print("Ikozagon terület számítás")
print("-------------------------------------------")

import math
oldal=int(input("Ikozagon oldalhossz: "))
terulet=math.pow(oldal,2)*5*(1+math.sqrt(5)+math.sqrt(5+2*math.sqrt(5)))
print("Az ikozagon területe: %.2f"%terulet)
