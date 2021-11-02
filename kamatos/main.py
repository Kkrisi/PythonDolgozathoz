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
print("Feladat 0313")
print("Kamatos kamat számítás")
print("-------------------------------------------")

betet=int(input("Betét: "))
tokesites_szam=int(input("Betét évenkénti tőkesítés száma: "))
nevleges=int(input("Névleges kamat (%): "))
import math
tenyleges=((math.pow((1+(nevleges/(100*tokesites_szam))), tokesites_szam))-1)*betet
print("Tényleges kamat 1 évre: ",tenyleges)
