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
print("Feladat 0347")
print("Pentagon terület számítás")
print("-------------------------------------------")

a=int(input("Pentagon oldalhossza: "))
import math
terulet=(math.pow(a, 2)*math.sqrt(25+10*math.sqrt(5)))/4
print("Pentagon területe: %.2f"%terulet)
