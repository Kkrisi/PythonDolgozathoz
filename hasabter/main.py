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
print("Feladat 0329")
print("Hasáb térfogat számítás")
print("-------------------------------------------")

a1=int(input("Első hasáb hossza: "))
b1=int(input("Első hasáb magassága: "))
c1=int(input("Első hasáb szélessége: "))

a2=int(input("Második hasáb hossza: "))
b2=int(input("Második hasáb magassága: "))
c2=int(input("Második hasáb szélessége: "))

a3=int(input("Haramdik hasáb hossza: "))
b3=int(input("Harmadik hasáb magassága: "))
c3=int(input("Harmadik hasáb szélessége: "))

terfogat1=a1*b1*c1
terfogat2=a2*b2*c2
terfogat3=a3*b3*c3
print("Az első hasáb térfogata: ",terfogat1)
print("A második hasáb térfogata: ",terfogat2)
print("A harmadik hasáb térfogata: ",terfogat3)
osszeg=terfogat1+terfogat2+terfogat3
print("Összegük: ",osszeg)
