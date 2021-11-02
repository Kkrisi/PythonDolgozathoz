# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0306")
print("Háromszög terület számítása, a háromszög egy oldalából, és hozzátartozó magasságból")
print("-------------------------------------------")

oldal=int(input("Oldal hossza: "))
magassag=int(input("Hozzátartozó magasság: "))
terulet=(oldal*magassag)/2
print("A háromszög területe: ",terulet)
