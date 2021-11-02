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
print("Feladat 0351")
print("Napi kalória szükséglet számítás")
print("-------------------------------------------")

testtomeg=int(input("Testtömege(kg): "))
magassag=int(input("Magassága(cm): "))
eletkor=int(input("Életkora: "))
nkaloria=9.247*testtomeg+3.098*magassag-4.330*eletkor+447.593
fkaloria=13.397*testtomeg+4.799*magassag-5.667*eletkor+88.362
nemvalasztas=str(input("Férfi esetén f, nő esetén n: "))
f=0
n=0
if (nemvalasztas==f):
    print("Napi szükséges kalória: ",fkaloria)
else:
    print("Napi szükséges kalória: ",nkaloria)
    

