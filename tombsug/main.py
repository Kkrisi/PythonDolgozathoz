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
print("Feladat 0312")
print("Rombuszba írható kör sugár számítása")
print("-------------------------------------------")

oldal=int(input("Oldal hossza: "))
alfaszog=int(input("Alfa szög nagysága: "))
import math
sugar=(1/2)*oldal*(math.sin(alfaszog))
print("A rombuszba írható kör sugara: %.2f"%sugar)
