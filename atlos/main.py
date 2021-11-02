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
print("Feladat 0334")
print("Téglalap átló számítás")
print("-------------------------------------------")

import math
a=int(input("A-oldal: "))
b=int(input("B-oldal: "))
atlo=math.sqrt(math.pow(a,2)+math.pow(b,2))
print("A téglalap átlója: %.2f"%atlo)
