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
print("Feladat 0345")
print("Jármű fogyasztás számítás")
print("-------------------------------------------")

k1=int(input("Kilométeróra állás: "))
l=int(input("Újra tankolt mennyiség: "))
k2=int(input("Kilométeróra állás méréskor: "))
fogyasztas=l/((k2-k1)*100)
print("Fogyasztás: ",fogyasztas)
