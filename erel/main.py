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
print("Feladat 0325")
print("Ellenállás számítás")
print("-------------------------------------------")

e=int(input("Elektromos térerősséget (E): "))
j=int(input("Elektromos áramsűrűséget (J): "))
l=int(input("Vezető hossza: "))
a=int(input("Vezető keresztmetszete: "))
ellenallas=(e/j)*(l/a)
print("Ellenállás értéke: ",ellenallas)
