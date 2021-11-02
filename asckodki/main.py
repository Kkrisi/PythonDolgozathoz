# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0714")
print("Ascii és hozzájuk tartozó kódok kiírása")
print("-------------------------------------------")

lista1=[]
for i in range(65,127):
    lista1.append(chr(i))
print (lista1)

lista2=[]
for k in range(65,127):
    lista2.append(ord(k))
print (lista2)
