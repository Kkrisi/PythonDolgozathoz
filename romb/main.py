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
print("Feladat 0310")
print("Rombusz kerület és terület számítás")
print("-------------------------------------------")

oldal=int(input("Rombusz oldal hossza: "))
szog=int(input("Rombusz alfa szöge: "))
import math
m1=math.degrees(180)+math.degrees(szog)
m2=oldal*math.sin(m1)
terulet=oldal*m2
kerulet=4*oldal
print("A rombusz területe: %.2f"%terulet)
print("A rombusz kerülete: %.2f"%kerulet)
