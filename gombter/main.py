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
print("Feladat 0330")
print("Gömb térfogat és felszín számítás")
print("-------------------------------------------")

atmero=int(input("Gömb átmérője: "))
import math
terfogat=(4*(math.pow(atmero, 3))*math.pi)/3
felszin=4*math.pi*math.pow(atmero, 2)
print("A gömb térfogata: %.2f"%terfogat)
print("A gömb felszine: %.2f"%felszin)
