# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0304")
print("Egy hónapban egy autóval mennyibe kerül 1km megtétele")
print("-------------------------------------------")

allkolt=int(input("Állandó költségek(adó,garázs,stb): "))
javkolt=int(input("Javítási költségek: "))
benzkolt=int(input("Benzinköltségek: "))
megtettkm=int(input("Megtett km-ek száma: "))

honap=allkolt+javkolt+benzkolt
print("Havi autó költség: ",honap, "Ft")
