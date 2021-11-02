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
print("Feladat 0332")
print("Kamatos kamatot számítás (többszöri tőkésítési lehetőséggel)")
print("-------------------------------------------")

betet=int(input("Betét: "))
kamat=int(input("Éves kamat(%): "))
tokesites=int(input("Évenkénti tőkésítések száma: "))
ev=int(input("Évek száma: "))
import math
jovoertek=math.pow(((kamat/(100*tokesites))+1), ev*tokesites)
print("Jövőérték: %.2f"%jovoertek)
