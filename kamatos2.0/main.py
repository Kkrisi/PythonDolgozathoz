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
print("Feladat 0331")
print("Kamatos kamat számítás 2.0")
print("-------------------------------------------")

betet=int(input("Betét: "))
nevleges=int(input("Névleges kamat(%): "))
tokesites_szam=int(input("Évenkénti tőkesítés száma: "))
ev=int(input("Évek száma: "))
import math
tenyleges=(math.pow(((nevleges/100*tokesites_szam)+1), ev)-1)*betet
print("Tényleges éves kamat: %.2f"%tenyleges)

