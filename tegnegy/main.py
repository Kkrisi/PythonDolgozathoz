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
print("Feladat 0336")
print("Téglalap kerület és terület számítás")
print("-------------------------------------------")

a1=int(input("A1-oldal: "))
b1=int(input("B1-oldal: "))

a2=int(input("A2-oldal: "))
b2=int(input("B2-oldal: "))

kerulet1=2*(a1+b1)
terulet1=a1*b1

kerulet2=2*(a2+b2)
terulet2=a2*b2

print("Első téglalap területe és kerülete: ",kerulet1,"|",kerulet2)
print("Második téglalap területe és kerülete: ",terulet2,"|",kerulet2)
