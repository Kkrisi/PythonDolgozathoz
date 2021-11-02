# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0710")
print("0-ig bekérés, majd legnagyobb,legkisebb szám kiírása")
print("-------------------------------------------")

lista=[]
i=-1
while (i!=0):
    i=int(input("Kérek egy számot: "))
    lista.append(i)
print("Legnagyobb szám: ",max(lista))
print("Legkisebb szám: ",min(lista))	
