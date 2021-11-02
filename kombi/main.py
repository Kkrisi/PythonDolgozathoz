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
print("Feladat 0328")
print("Lehetséges kombinációk számítása")
print("-------------------------------------------")

elemek=int(input("Halmaz elemeinek száma: "))
kivalasztott=int(input("Kiválasztott elemek száma: "))
import math
kombinaciok=(math.factorial(elemek))/(math.factorial(kivalasztott)*math.factorial(elemek-kivalasztott))
print("Ennyi kombináció lehetséges: ",kombinaciok)
