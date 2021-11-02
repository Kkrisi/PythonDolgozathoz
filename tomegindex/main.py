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
print("Feladat 0333")
print("Oxford típusú testtömegindex számítás")
print("-------------------------------------------")

testtomeg=int(input("Testtömeg(kg): "))
magassag=int(input("Magasság(cm): "))
import math
index=((1.3*testtomeg)/(math.pow(magassag, 2.5)))*100000
if (index<16):
	print("súlyos soványság")
elif (16<=index<=16.9):
	print("mérsékelt soványság")
elif (17<=index<=18.49):
	print("enyhe sovány")
elif (18.5<=index<=24.9):
	print("egészséges")
elif (25<=index<=29.9):
	print("túlsúlyos")
elif (30<=index<=34.9):
	print("I.fokú elhízás")
elif (35<=index<=39.9):
	print("II.fokú elhízás")
else:
	print("III.fokú súlyos elhízás")
print("Testtömegindex: %.2f"%index)

