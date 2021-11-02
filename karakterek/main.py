# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-10-19
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-10-19")
print("Feladat 0705")
print("karakterei")
print("-------------------------------------------")

szamlalo=1
for i in range(97, 123):
	print(chr(i) , end=" ")
	if szamlalo % 5 == 0:
		print()
	szamlalo += 1
