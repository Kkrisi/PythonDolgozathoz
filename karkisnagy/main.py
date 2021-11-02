#coding=utf-8
# File: main.py
# Auth: Kádár Kristóf
# Copyright: 2021, Kádár Kristóf
# Group: IFRA
# Date: 2021-11-02
# Github: https://github.com/Kkrisi
# Licenc: GNU GPL

print("Kádár Kristóf, Rendszergazda")
print("2021-11-02")
print("Feladat 0717")
print("Angol ábc bekérése, majd kis és nagybetűk megszámolása")
print("-------------------------------------------")

import string 
abc=string.ascii_lowercase
abclista=list(abc)
betuk=input("Csak nagol ábc betűt írjon: ")
if betuk.isalpha() is False:
    kisbetuk=0
    nagybetuk=0
    for i in betuk:
        if(i.islower()):
            kisbetuk=kisbetuk+1
        elif(i.isupper()):
            nagybetuk=nagybetuk+1
    print("Kisbetűk száma:",kisbetuk)
    print("Nagybetűk száma:",nagybetuk)
    #betuk+=1
else:
    while(betuk in abclista):
        betuk=input("Csak nagol ábc betűt írjon: ")
