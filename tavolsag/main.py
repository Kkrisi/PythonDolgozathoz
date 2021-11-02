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
print("Feladat 0349")
print("Távolság számítás")
print("-------------------------------------------")

import math
magassag=int(input("Épület magassága: "))
szog=int(input("Épület bezárt szöge: "))
tavolsag=magassag/math.sin(szog)
print("Távolság: %.2f"%tavolsag)
