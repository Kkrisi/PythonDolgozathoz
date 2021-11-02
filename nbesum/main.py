# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0711")
print("")
print("-------------------------------------------")

lista=[]
n=int(input("Kérek egy számot: "))
for i in range(n):
	bekeres=int(input("Még egyet: "))
	lista.append(bekeres)
osszeg=sum(lista)
print("Számok összege: ", osszeg)
