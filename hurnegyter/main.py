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
print("Feladat 0315")
print("Húrnégyszög terület számítás")
print("-------------------------------------------")

a=int(input("Oldal1: "))
b=int(input("Oldal2: "))
c=int(input("Oldal3: "))
d=int(input("Oldal4: "))
import math
terulet=math.sqrt((a+b+c+d)/2)
print("Trapéz területe: ",terulet)

