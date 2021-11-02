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
print("Feladat 0335")
print("Aranytéglalap számítás")
print("-------------------------------------------")

a=int(input("A-oldal: "))
b=int(input("B-oldal: "))
elso=a/b
masodik=b/(a-b)
if (elso==masodik):
	print("Ez egy aranytéglalap.")
else:
	print("Ez nem egy aranytéglalap.")
