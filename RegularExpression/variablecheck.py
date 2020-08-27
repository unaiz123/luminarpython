from  re import *
rule='[a-k][369][a-z]*'

var=input("Enter variable name : ")
matcher=fullmatch(rule,var)

if matcher !=None :
    print("Valid")
else:
    print("Invalid")