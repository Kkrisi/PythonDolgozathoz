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
print("Feladat 0319")
print("Tórusz térfogat számítás")
print("-------------------------------------------")

r=int(input("Kör sugara: "))
R=int(input("Forgástengely és a kör középpontjának távolsága: "))
import math
terfogat=(math.pi*(math.pow(r, 2)))*(2*math.pi*R)
print("Tórusz térfogata: ",terfogat)
