# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0708")
print("0 végjelig bekérés, majd azok átlaga kiírása")
print("-------------------------------------------")

szam = -1
osszeg = 0
while szam != 0:
	szam = int(input("Kérek egy számot:"))
	osszeg = osszeg + szam
print("Összeg:", osszeg)

