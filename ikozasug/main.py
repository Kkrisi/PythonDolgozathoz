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
print("Feladat 0343")
print("Ikozaéder sugár számítás")
print("-------------------------------------------")

elhossz=int(input("Élhossz: "))
import math
ksugar=(elhossz/4)*math.sqrt(10+2*math.sqrt(5))
print("Az ikozaéder köré írható gömb sugara: %.2f"%ksugar)
