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
print("Feladat 0323")
print("Testtömegindex számítás")
print("-------------------------------------------")

tomeg=int(float(input("Testtömeg(kg): ")))
magassag=int(float(input("Testmagasság(cm): ")))
import math
eredmeny=tomeg/(math.pow((magassag), 2))*10000
print("Testtömegindex: %.2f"%eredmeny)
