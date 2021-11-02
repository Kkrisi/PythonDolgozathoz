# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0709")
print("Faktoriális kiírás")
print("-------------------------------------------")

n=input("Kérek egy számot: ")
factorial=1
if int(n)>=1:
    for i in range (1,int(n)+1):
        factorial=factorial*i
print(n, "faktoriálsa: ",factorial)
