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
print("Feladat 0324")
print("Belső megtérülés ráta számítás")
print("-------------------------------------------")

evek=int(input("Hány évre szeretné betenni a tőkéjét: "))
mennyi=int(input("Mennyi tőkét szeretne betenni: "))
vissza=int(input("Mennyit kapna vissza: "))
import math
rata=(math.pow(vissza/mennyi, (1/evek)))
print("Megtérülési ráta: ",rata)
