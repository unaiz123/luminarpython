from re import *

rule='[Kk][Ll][0-9]{2}[a-z]{1,2}\d{4}'

regno=input("Enter variable reg no : ")
matcher=fullmatch(rule,regno)

if matcher !=None :
    print("Valid")
else:
    print("Invalid")