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
print("Feladat 0353")
print("Maximális pulzus számítás")
print("-------------------------------------------")

eletkor=int(input("Életkora: "))
nyugpulzus=int(input("Nyugalmi pulzusa: "))
edzes=int(input("Hány százalékosan szeretnénk edzeni: "))

if (edzes<50):
	print("kezdő edzés")
elif (50<=edzes<=60):
	print("regeneráló edzés")
elif (60<=edzes<=70):
	print("zsírégető edzés")
elif (70<=edzes<=85):
	print("aerob kapacítás fejlesztése")
elif (85<=edzes<=95):
	print("anaerob állóképesség fejlesztése")
elif (95<=edzes<=100):
	print("gyorsaság, robbanékonyság fejlesztése")
else:
    print("vadállat edzés")

maxpulzus=220-eletkor
ajanlpulzus=(maxpulzus-nyugpulzus)*edzes+nyugpulzus
print("A pulzus, amivel ajánlott edzeni adott intenzitás mellett: ",ajanlpulzus)
