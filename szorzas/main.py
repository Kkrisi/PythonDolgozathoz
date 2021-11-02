# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-10-19
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-10-19")
print("Feladat 0701")
print("A 0 végkjelig bekért számokat összeadjuk")
print("-------------------------------------------")

szam = -1
szorzat = 1
while szam != 0:
	szam = int(input("Kérek egy számot:"))
	if szam != 0:
		szorzat = szorzat * szam

print("Összeg:", szorzat)

