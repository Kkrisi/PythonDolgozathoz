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
print("Feladat 0352")
print("Napi kalória szükséglet számítás")
print("-------------------------------------------")

testtomeg=int(input("Testtömege(kg): "))
testzsir=int(input("Testzsírszázalék: "))
kaloria=370+21.6*(1-testzsir)*testtomeg
print("Napi szükséges kalória: ",kaloria)


