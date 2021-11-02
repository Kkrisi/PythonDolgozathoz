# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0716")
print("Fordított piramis ábrázolása")
print("-------------------------------------------")

sorok=5
for i in range(sorok,0,-1):
    for j in range(sorok-i):
        print("  ", end='')
    
    for j in range(2*i-1):
        print("@ ",end='')
    print()

